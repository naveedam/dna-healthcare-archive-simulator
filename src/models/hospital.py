from dataclasses import dataclass


@dataclass
class Hospital:
    """
    Represents a healthcare institution within a regional network.
    """

    name: str

    initial_patients: int

    annual_growth_rate: float

    description: str