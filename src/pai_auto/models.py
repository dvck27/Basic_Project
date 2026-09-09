from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime
from hashlib import sha256
import json


@dataclass(frozen=True, slots=True)
class ApplicationRecord:
    source_row: int
    document_type: str
    document_number: str
    vaccination_date: date
    vaccinator: str
    biologic_code: str
    biologic_name: str
    dose: str
    lot: str
    syringe_lot: str = ""
    diluent_lot: str = ""
    biologic_type: str = ""
    observation: str = ""

    @property
    def fingerprint(self) -> str:
        canonical = "|".join(
            [
                self.document_type.strip().upper(),
                self.document_number.strip().upper(),
                self.vaccination_date.isoformat(),
                self.biologic_code.strip().upper(),
                self.biologic_type.strip().upper(),
                self.dose.strip().upper(),
                self.lot.strip().upper(),
            ]
        )
        return sha256(canonical.encode("utf-8")).hexdigest()

    def as_json(self) -> str:
        payload = asdict(self)
        payload["vaccination_date"] = self.vaccination_date.isoformat()
        return json.dumps(payload, ensure_ascii=False, sort_keys=True)


@dataclass(frozen=True, slots=True)
class ImportIssue:
    source_row: int
    code: str
    message: str


@dataclass(slots=True)
class ImportResult:
    source_name: str
    total_source_rows: int
    records: list[ApplicationRecord]
    issues: list[ImportIssue]

    @property
    def valid_rows(self) -> int:
        return len({record.source_row for record in self.records})


@dataclass(frozen=True, slots=True)
class RuntimeDefaults:
    units: str = ""
    anatomical_site: str = ""
    application_type: str = ""
    economic_sector: str = ""


@dataclass(frozen=True, slots=True)
class WriteResult:
    remote_ref: str
    detail: str = ""


@dataclass(slots=True)
class RunSummary:
    run_id: str
    started_at: datetime
    finished_at: datetime | None = None
    total: int = 0
    succeeded: int = 0
    skipped: int = 0
    failed: int = 0
