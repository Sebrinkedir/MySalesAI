from Agents.coordinator import Coordinator
from Agents.single_agent import SingleAgent
from Agents.logger import Logger

def main():
    print("MySalesAI starting...")

    file_path = "data/sample.csv"
    logger = Logger()
    question = input("Ask a sales question: ")

    print("\nChoose system mode:")
    print("1. Multi-Agent System")
    print("2. Single-Agent Baseline")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        coordinator = Coordinator()
        result = coordinator.run(file_path, question)
        mode = "Multi-Agent System"

    elif choice == "2":
        single_agent = SingleAgent()
        result = single_agent.run(file_path, question)
        mode = "Single-Agent Baseline"

    else:
        print("Invalid choice.")
        return

    print(f"\n=== MODE: {mode} ===")

    print("\n=== ANALYSIS RESULTS ===")
    print(result["analysis"])

    print("\n=== GENERATED INSIGHTS ===")
    print(result["insights"])

    if "latency_seconds" in result:
        print("\n=== LATENCY ===")
        print(f'{result["latency_seconds"]} seconds')

    logger.log_run(
        mode=mode,
        question=question,
        analysis=result["analysis"],
        insights=result["insights"],
        latency=result.get("latency_seconds", None)
    )

    print("\nRun saved to logs/evaluation_log.csv")


if __name__ == "__main__":
    main()