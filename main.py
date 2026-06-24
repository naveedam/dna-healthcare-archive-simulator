from src.simulation.hospital_simulator import HospitalSimulator


def main():

    simulator = HospitalSimulator()

    yearly_data = simulator.simulate(20)

    results = simulator.calculate_storage_tiers(yearly_data)

    print("\nDNA Healthcare Archive Simulator\n")

    print(
        f"{'Year':<6}"
        f"{'Patients':<12}"
        f"{'Active TB':<15}"
        f"{'DNA TB':<15}"
        f"{'Total TB':<15}"
    )

    print("-" * 63)

    for row in results:

        print(
            f"{row['year']:<6}"
            f"{row['patients']:<12,d}"
            f"{row['active_tb']:<15.2f}"
            f"{row['dna_tb']:<15.2f}"
            f"{row['total_tb']:<15.2f}"
        )


if __name__ == "__main__":
    main()
