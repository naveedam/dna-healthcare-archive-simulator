from src.simulation.hospital_simulator import HospitalSimulator
from src.simulation.scenario_engine import ScenarioEngine
from src.simulation.healthcare_network import HealthcareNetwork


def print_annual_simulation(results):

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


def print_engineering_summary(simulator, final):

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


def print_scenarios():

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

        savings = f"${scenario['savings']:,.0f}"

        print(
            f"{scenario['scenario']:<30}"
            f"{savings:>18}"
            f"{scenario['physical_dna_tb']:>15.2f} TB"
        )

    print("=" * 65)


def print_network():

    network = HealthcareNetwork()

    hospitals = network.simulate()

    totals = network.totals()

    print()
    print("=" * 80)
    print("HEALTHCARE NETWORK SUMMARY")
    print("=" * 80)

    print(
        f"{'Hospital':<30}"
        f"{'Patients':>12}"
        f"{'Storage':>15}"
        f"{'Savings':>18}"
    )

    print("-" * 80)

    for hospital in hospitals:

        savings = f"${hospital['savings']:,.0f}"

        print(
            f"{hospital['hospital']:<30}"
            f"{hospital['patients']:>12,}"
            f"{hospital['total_tb']:>15.2f}"
            f"{savings:>18}"
        )

    print("-" * 80)

    print("\nNETWORK TOTALS\n")

    print(f"Total Patients              : {totals['patients']:,}")
    print(f"Total Active Storage        : {totals['active_tb']:.2f} TB")
    print(f"Total DNA Archive           : {totals['dna_tb']:.2f} TB")
    print(f"Physical DNA Required       : {totals['physical_dna_tb']:.2f} TB")
    print(f"Total Logical Storage       : {totals['total_tb']:.2f} TB")
    print(f"Annual Savings              : ${totals['savings']:,.2f}")

    print("\nNETWORK INSIGHTS\n")

    largest = max(hospitals, key=lambda x: x["patients"])
    biggest_storage = max(hospitals, key=lambda x: x["total_tb"])
    biggest_dna = max(hospitals, key=lambda x: x["dna_tb"])

    print(f"Largest Hospital            : {largest['hospital']}")
    print(f"Highest Storage             : {biggest_storage['hospital']}")
    print(f"Largest DNA Archive         : {biggest_dna['hospital']}")
    print(
        f"Average Hospital Size       : "
        f"{int(totals['patients']/len(hospitals)):,} patients"
    )

    print("=" * 80)


def main():

    simulator = HospitalSimulator()

    yearly = simulator.simulate(20)

    results = simulator.calculate_storage_tiers(yearly)

    print_annual_simulation(results)

    print_engineering_summary(
        simulator,
        results[-1]
    )

    print_scenarios()

    print_network()


if __name__ == "__main__":
    main()