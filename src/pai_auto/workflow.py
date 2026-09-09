from __future__ import annotations

from dataclasses import dataclass

from .db import Database
from .gateways import Gateway
from .models import ApplicationRecord, RuntimeDefaults


@dataclass(frozen=True, slots=True)
class WorkflowResult:
    run_id: str
    total: int
    succeeded: int
    skipped: int
    failed: int


class WorkflowEngine:
    def __init__(self, db: Database):
        self.db = db

    def run(
        self,
        *,
        source_name: str,
        records: list[ApplicationRecord],
        batch_size: int,
        mode: str,
        gateway: Gateway,
        defaults: RuntimeDefaults,
    ) -> WorkflowResult:
        run_id = self.db.create_run(source_name, mode, batch_size)
        succeeded = skipped = failed = 0
        state = "DONE"
        try:
            gateway.start()
            for record in records:
                if self.db.was_processed(record.fingerprint):
                    skipped += 1
                    self.db.add_item(run_id, record, "SKIPPED", message="Ya procesado: idempotencia local.")
                    continue
                try:
                    result = gateway.write(record, defaults)
                    if not gateway.verify(record, result):
                        raise RuntimeError("La verificación posterior no confirmó el registro.")
                    self.db.mark_processed(record, result.remote_ref)
                    self.db.add_item(run_id, record, "SUCCESS", remote_ref=result.remote_ref, message=result.detail)
                    succeeded += 1
                except Exception as exc:  # una fila no detiene el lote
                    failed += 1
                    self.db.add_item(run_id, record, "FAILED", message=str(exc))
            return WorkflowResult(run_id, len(records), succeeded, skipped, failed)
        except Exception:
            state = "ABORTED"
            raise
        finally:
            try:
                gateway.close()
            finally:
                self.db.finish_run(run_id, state)
