from copy import deepcopy

from src.simulation.hospital_simulator import HospitalSimulator


class ScenarioEngine:
    """
    Runs multiple simulation scenarios using different
    DNA storage assumptions.
    """

    def __init__(self):

        self.scenarios = [
            {
                "name": "Baseline",
                "compression": 100,
                "active_cost": 220,
                "dna_cost": 35,
            },
            {
                "name": "Future DNA Technology",
                "compression": 250,
                "active_cost": 220,
                "dna_cost": 25,
            },
            {
                "name": "Lower Storage Costs",
                "compression": 100,
                "active_cost": 150,
                "dna_cost": 30,
            },
            {
                "name": "High Growth Planning",
                "compression": 100,
                "active_cost": 220,
                "dna_cost": 35,
                "growth_rate": 0.12,
            },
        ]

    def run(self):

        results = []

        for scenario in self.scenarios:

            simulator = HospitalSimulator()

            simulator.dna_storage.compression_ratio = scenario["compression"]
            simulator.dna_storage.active_storage_cost_per_tb = scenario["active_cost"]
            simulator.dna_storage.dna_archive_cost_per_tb = scenario["dna_cost"]

            if "growth_rate" in scenario:
                simulator.growth_rate = scenario["growth_rate"]

            yearly = simulator.simulate(20)

            tiers = simulator.calculate_storage_tiers(yearly)

            final = deepcopy(tiers[-1])

            final["scenario"] = scenario["name"]

            results.append(final)

        return results