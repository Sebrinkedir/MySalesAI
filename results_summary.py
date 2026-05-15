import pandas as pd


def main():
    file_path = "logs/automated_evaluation.csv"

    df = pd.read_csv(file_path)

    print("\n=== EVALUATION SUMMARY ===")

    grouped = df.groupby("mode")

    for mode, data in grouped:
        avg_latency = round(data["latency_seconds"].mean(), 2)
        avg_accuracy = round(data["accuracy_percent"].mean(), 2)
        avg_hallucination = round(data["hallucination_count"].mean(), 2)

        print(f"\nMODE: {mode}")
        print(f"Average Latency: {avg_latency} seconds")
        print(f"Average Accuracy: {avg_accuracy}%")
        print(f"Average Hallucination Count: {avg_hallucination}")


if __name__ == "__main__":
    main()