from dataclasses import dataclass


@dataclass
class RecordType:
    name: str
    size_mb: float
    annual_rate: float
    archive_after_years: int
