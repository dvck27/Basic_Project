from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
import sqlite3
import threading
import uuid

from .models import ApplicationRecord


class Database:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self.init()

    @contextmanager
    def connection(self):
        with self._lock:
            con = sqlite3.connect(self.path)
            con.row_factory = sqlite3.Row
            try:
                yield con
                con.commit()
            finally:
                con.close()

    def init(self) -> None:
        with self.connection() as con:
            con.executescript(
                """
                CREATE TABLE IF NOT EXISTS runs (
                    id TEXT PRIMARY KEY,
                    source_name TEXT NOT NULL,
                    mode TEXT NOT NULL,
                    batch_size INTEGER NOT NULL,
                    started_at TEXT NOT NULL,
                    finished_at TEXT,
                    state TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS run_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    run_id TEXT NOT NULL,
                    fingerprint TEXT NOT NULL,
                    source_row INTEGER NOT NULL,
                    document_number TEXT NOT NULL,
                    biologic_name TEXT NOT NULL,
                    dose TEXT NOT NULL,
                    lot TEXT NOT NULL,
                    status TEXT NOT NULL,
                    message TEXT NOT NULL DEFAULT '',
                    remote_ref TEXT NOT NULL DEFAULT '',
                    payload_json TEXT NOT NULL,
                    FOREIGN KEY(run_id) REFERENCES runs(id)
                );
                CREATE TABLE IF NOT EXISTS processed (
                    fingerprint TEXT PRIMARY KEY,
                    remote_ref TEXT NOT NULL,
                    completed_at TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                """
            )

    def create_run(self, source_name: str, mode: str, batch_size: int) -> str:
        run_id = uuid.uuid4().hex[:12]
        now = datetime.now(timezone.utc).isoformat()
        with self.connection() as con:
            con.execute(
                "INSERT INTO runs(id, source_name, mode, batch_size, started_at, state) VALUES(?,?,?,?,?,?)",
                (run_id, source_name, mode, batch_size, now, "RUNNING"),
            )
        return run_id

    def finish_run(self, run_id: str, state: str = "DONE") -> None:
        with self.connection() as con:
            con.execute(
                "UPDATE runs SET state=?, finished_at=? WHERE id=?",
                (state, datetime.now(timezone.utc).isoformat(), run_id),
            )

    def was_processed(self, fingerprint: str) -> bool:
        with self.connection() as con:
            return (
                con.execute("SELECT 1 FROM processed WHERE fingerprint=?", (fingerprint,)).fetchone()
                is not None
            )

    def add_item(
        self,
        run_id: str,
        record: ApplicationRecord,
        status: str,
        *,
        message: str = "",
        remote_ref: str = "",
    ) -> None:
        with self.connection() as con:
            con.execute(
                """INSERT INTO run_items(
                    run_id,fingerprint,source_row,document_number,biologic_name,dose,lot,status,message,remote_ref,payload_json
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?)""",
                (
                    run_id,
                    record.fingerprint,
                    record.source_row,
                    record.document_number,
                    record.biologic_name,
                    record.dose,
                    record.lot,
                    status,
                    message,
                    remote_ref,
                    record.as_json(),
                ),
            )

    def mark_processed(self, record: ApplicationRecord, remote_ref: str) -> None:
        with self.connection() as con:
            con.execute(
                "INSERT OR REPLACE INTO processed(fingerprint,remote_ref,completed_at,payload_json) VALUES(?,?,?,?)",
                (
                    record.fingerprint,
                    remote_ref,
                    datetime.now(timezone.utc).isoformat(),
                    record.as_json(),
                ),
            )

    def recent_runs(self, limit: int = 12) -> list[dict]:
        with self.connection() as con:
            rows = con.execute(
                "SELECT * FROM runs ORDER BY started_at DESC LIMIT ?", (limit,)
            ).fetchall()
            return [dict(row) for row in rows]

    def run_items(self, run_id: str) -> list[dict]:
        with self.connection() as con:
            rows = con.execute(
                "SELECT * FROM run_items WHERE run_id=? ORDER BY id", (run_id,)
            ).fetchall()
            return [dict(row) for row in rows]
