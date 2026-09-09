from datetime import date

from pai_auto.db import Database
from pai_auto.gateways import SimulatorGateway
from pai_auto.models import ApplicationRecord, RuntimeDefaults
from pai_auto.workflow import WorkflowEngine


def record():
    return ApplicationRecord(16, "CC", "123", date(2026, 9, 8), "Vacunador", "PAI_BCG", "BCG", "Única", "L1")


def test_end_to_end_simulator_and_idempotency(tmp_path):
    db = Database(tmp_path / "pai.db")
    engine = WorkflowEngine(db)
    first = engine.run(
        source_name="registro.xlsx",
        records=[record()],
        batch_size=1,
        mode="simulator",
        gateway=SimulatorGateway(),
        defaults=RuntimeDefaults(),
    )
    assert first.succeeded == 1
    assert first.failed == 0

    second = engine.run(
        source_name="registro.xlsx",
        records=[record()],
        batch_size=1,
        mode="simulator",
        gateway=SimulatorGateway(),
        defaults=RuntimeDefaults(),
    )
    assert second.succeeded == 0
    assert second.skipped == 1


def test_batch_size_counts_source_rows_not_applications():
    from pai_auto.importer import select_batch

    records = [
        ApplicationRecord(16, "CC", "1", date(2026, 9, 8), "V", "A", "A", "1", "L1"),
        ApplicationRecord(16, "CC", "1", date(2026, 9, 8), "V", "B", "B", "1", "L2"),
        ApplicationRecord(17, "CC", "2", date(2026, 9, 8), "V", "C", "C", "1", "L3"),
    ]
    chosen = select_batch(records, start_source_row=16, batch_size=1)
    assert len(chosen) == 2
    assert {record.source_row for record in chosen} == {16}
