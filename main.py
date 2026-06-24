from src.simulation.hospital_simulator import HospitalSimulator


def main():

    simulator = HospitalSimulator()

    results = simulator.simulate(20)

    total_storage = 0

    print("\nDNA Healthcare Archive Simulator\n")

    for row in results:

        total_storage += row["storage_tb"]

        print(
            f"Year {row['year']:2d} | "
            f"Patients: {row['patients']:8,d} | "
            f"New Data: {row['storage_tb']:8.2f} TB | "
            f"Cumulative: {total_storage:10.2f} TB"
        )


if __name__ == "__main__":
    main()