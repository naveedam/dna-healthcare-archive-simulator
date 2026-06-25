from src.simulation.hospital_simulator import HospitalSimulator
from src.simulation.scenario_engine import ScenarioEngine


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

    for year in results:

        print(
            f"{year['year']:<6}"
            f"{year['patients']:<12,}"
            f"{year['active_tb']:<15.2f}"
            f"{year['dna_tb']:<15.2f}"
            f"{year['total_tb']:<15.2f}"
        )

    final = results[-1]

    print("\n")
    print("=" * 65)
    print("YEAR 20 ENGINEERING SUMMARY")
    print("=" * 65)

    print(f"Patients                    : {final['patients']:,}")

    print("\nStorage")
    print("-" * 65)
    print(f"Active Storage              : {final['active_tb']:.2f} TB")
    print(f"Logical DNA Archive         : {final['dna_tb']:.2f} TB")
    print(f"Physical DNA Required       : {final['physical_dna_tb']:.2f} TB")
    print(f"Estimated DNA Media Units   : {final['dna_media_units']}")
    print(f"Total Logical Storage       : {final['total_tb']:.2f} TB")

    print("\nEconomics (Annual)")
    print("-" * 65)
    print(f"Active Storage Cost         : ${final['active_cost']:,.2f}")
    print(f"DNA Archive Cost            : ${final['dna_cost']:,.2f}")
    print(f"Total Annual Cost           : ${final['total_cost']:,.2f}")
    print(f"All Active Storage Cost     : ${final['all_active_cost']:,.2f}")
    print(f"Estimated Annual Savings    : ${final['savings']:,.2f}")

    print("\nDNA Assumptions")
    print("-" * 65)
    print(
        f"Compression Ratio           : "
        f"{simulator.dna_storage.compression_ratio:.0f}:1"
    )
    print(
        f"DNA Unit Capacity           : "
        f"{simulator.dna_storage.dna_media_capacity_tb:.2f} TB"
    )

    print("=" * 65)

    #
    # Scenario Comparison
    #

    print()
    print("=" * 65)
    print("SCENARIO COMPARISON")
    print("=" * 65)

    print(
        f"{'Scenario':<30}"
        f"{'Savings':>18}"
        f"{'Physical DNA':>18}"
    )

    print("-" * 65)

    engine = ScenarioEngine()

    for scenario in engine.run():

        print(
            f"{scenario['scenario']:<30}"
            f"${scenario['savings']:>17,.0f}"
            f"{scenario['physical_dna_tb']:>17.2f} TB"
        )

    print("=" * 65)


if __name__ == "__main__":
    main()