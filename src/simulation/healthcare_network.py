from src.models.hospital import Hospital
from src.simulation.hospital_simulator import HospitalSimulator


class HealthcareNetwork:
    """
    Simulates a regional healthcare network made up of
    multiple hospitals.
    """

    def __init__(self):

        self.hospitals = [

            Hospital(
                "Community Hospital",
                75000,
                0.06,
                "General regional care"
            ),

            Hospital(
                "Children's Hospital",
                60000,
                0.07,
                "Pediatric care"
            ),

            Hospital(
                "Cancer Center",
                45000,
                0.05,
                "Oncology and research"
            ),

            Hospital(
                "Trauma Center",
                90000,
                0.08,
                "Emergency medicine"
            ),

            Hospital(
                "Academic Medical Center",
                250000,
                0.10,
                "Teaching and tertiary care"
            ),
        ]

    def simulate(self):

        network_results = []

        for hospital in self.hospitals:

            simulator = HospitalSimulator()

            simulator.initial_patients = hospital.initial_patients
            simulator.growth_rate = hospital.annual_growth_rate

            yearly = simulator.simulate(20)

            results = simulator.calculate_storage_tiers(yearly)

            final = results[-1].copy()

            final["hospital"] = hospital.name
            final["description"] = hospital.description

            network_results.append(final)

        return network_results

    def totals(self):

        hospitals = self.simulate()

        totals = {
            "patients": 0,
            "active_tb": 0,
            "dna_tb": 0,
            "physical_dna_tb": 0,
            "total_tb": 0,
            "savings": 0,
        }

        for hospital in hospitals:

            totals["patients"] += hospital["patients"]
            totals["active_tb"] += hospital["active_tb"]
            totals["dna_tb"] += hospital["dna_tb"]
            totals["physical_dna_tb"] += hospital["physical_dna_tb"]
            totals["total_tb"] += hospital["total_tb"]
            totals["savings"] += hospital["savings"]

        return totals