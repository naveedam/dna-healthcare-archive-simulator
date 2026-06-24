from src.models.record import RecordType


class HospitalSimulator:

    def __init__(self):

        self.initial_patients = 100000
        self.growth_rate = 0.08

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

            results.append(
                {
                    "year": current_year,
                    "patients": current_year_data["patients"],
                    "active_tb": active_tb,
                    "dna_tb": dna_tb,
                    "total_tb": active_tb + dna_tb
                }
            )

        return results
