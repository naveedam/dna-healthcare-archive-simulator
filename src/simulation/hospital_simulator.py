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

            yearly_tb = 0

            for record in self.record_types:

                records_created = patients * record.annual_rate
                mb_generated = records_created * record.size_mb
                tb_generated = mb_generated / 1024 / 1024

                yearly_tb += tb_generated

            yearly_data.append(
                {
                    "year": year,
                    "patients": int(patients),
                    "storage_tb": yearly_tb
                }
            )

            patients *= (1 + self.growth_rate)

        return yearly_data

