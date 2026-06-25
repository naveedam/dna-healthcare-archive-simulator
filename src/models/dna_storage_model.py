from dataclasses import dataclass


@dataclass
class DNAStorageModel:
    """
    Configuration model for DNA archival storage assumptions.

    All values are configurable so future simulations can easily
    evaluate different DNA storage technologies and pricing models.
    """

    # Logical-to-physical compression ratio
    compression_ratio: float = 100.0

    # Physical capacity represented by one DNA storage unit (TB)
    dna_media_capacity_tb: float = 1.0

    # Annual storage costs (USD per TB)
    active_storage_cost_per_tb: float = 220.0
    dna_archive_cost_per_tb: float = 35.0

    def physical_storage_required(self, logical_tb: float) -> float:
        """
        Convert logical archive size into physical DNA storage required.
        """
        return logical_tb / self.compression_ratio

    def dna_media_units(self, physical_tb: float) -> int:
        """
        Estimate the number of DNA storage units required.
        """
        import math

        return math.ceil(physical_tb / self.dna_media_capacity_tb)