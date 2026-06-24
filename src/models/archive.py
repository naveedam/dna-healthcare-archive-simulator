from dataclasses import dataclass


@dataclass
class ArchiveStatus:
    active_tb: float = 0
    dna_tb: float = 0

    @property
    def total_tb(self):
        return self.active_tb + self.dna_tb