from src.models.hospital import Hospital
from src.simulation.hospital_simulator import HospitalSimulator


class HealthcareNetwork:

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

            final = results[-1]

            final["hospital"] = hospital.name

            network_results.append(final)

        return network_results