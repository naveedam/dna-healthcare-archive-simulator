from src.models.record import RecordType
from src.models.dna_storage_model import DNAStorageModel


class HospitalSimulator:

    def __init__(self):

        self.initial_patients = 100000
        self.growth_rate = 0.08

        # DNA storage assumptions
        self.dna_storage = DNAStorageModel()

        self.record_types = [
            RecordType("EHR", 2, 5, 7),
            RecordType("MRI", 500, 0.15, 3),
            RecordType("CT", 1000, 0.10, 3),
            RecordType("XRAY", 50, 0.40, 3),
            RecordType("LAB", 1, 8, 5),
        ]

    def simulate(self, years=20):

        yearly_data = []

        patients = self.initial_patients

        for year in range(1, years + 1):

            record_storage = {}
            total_tb = 0

            for record in self.record_types:

                records_created = patients * record.annual_rate

                mb_generated = records_created * record.size_mb

                tb_generated = mb_generated / 1024 / 1024

                record_storage[record.name] = tb_generated

                total_tb += tb_generated

            yearly_data.append(
                {
                    "year": year,
                    "patients": int(patients),
                    "storage_tb": total_tb,
                    "record_storage": record_storage
                }
            )

            patients *= (1 + self.growth_rate)

        return yearly_data

    def calculate_storage_tiers(self, yearly_data):

        results = []

        for current_year_data in yearly_data:

            current_year = current_year_data["year"]

            active_tb = 0
            dna_tb = 0

            for historical_year in yearly_data:

                historical_year_number = historical_year["year"]

                if historical_year_number > current_year:
                    continue

                age = current_year - historical_year_number

                for record in self.record_types:

                    storage = historical_year["record_storage"][record.name]

                    if age >= record.retention_years:
                        dna_tb += storage
                    else:
                        active_tb += storage

            # ---------------------------------
            # DNA Compression
            # ---------------------------------

            physical_dna_tb = self.dna_storage.physical_storage_required(dna_tb)

            dna_media_units = self.dna_storage.dna_media_units(
                physical_dna_tb
            )

            # ---------------------------------
            # Economics
            # ---------------------------------

            active_cost = (
                active_tb *
                self.dna_storage.active_storage_cost_per_tb
            )

            dna_cost = (
                dna_tb *
                self.dna_storage.dna_archive_cost_per_tb
            )

            total_cost = active_cost + dna_cost

            all_active_cost = (
                (active_tb + dna_tb) *
                self.dna_storage.active_storage_cost_per_tb
            )

            savings = all_active_cost - total_cost

            results.append(
                {
                    "year": current_year,
                    "patients": current_year_data["patients"],

                    "active_tb": active_tb,
                    "dna_tb": dna_tb,
                    "physical_dna_tb": physical_dna_tb,
                    "dna_media_units": dna_media_units,

                    "total_tb": active_tb + dna_tb,

                    "active_cost": active_cost,
                    "dna_cost": dna_cost,
                    "total_cost": total_cost,
                    "all_active_cost": all_active_cost,
                    "savings": savings
                }
            )

        return results