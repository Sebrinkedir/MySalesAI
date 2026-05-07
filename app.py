from Agents.coordinator import Coordinator

def main():
    print("MySalesAI starting...")

    coordinator = Coordinator()

    file_path = "data/sample.csv"

    result = coordinator.run(file_path)

    print("\n=== ANALYSIS RESULTS ===")
    print(result["analysis"])

    print("\n=== GENERATED INSIGHTS ===")
    print(result["insights"])


if __name__ == "__main__":
    main()