import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_evaluation_charts():
    os.makedirs("charts", exist_ok=True)

    df = pd.read_csv("logs/automated_evaluation.csv")

    summary = df.groupby("mode").agg({
        "latency_seconds": "mean",
        "accuracy_percent": "mean",
        "hallucination_count": "mean"
    })

    # Latency chart
    summary["latency_seconds"].plot(kind="bar", title="Average Latency by Mode")
    plt.ylabel("Seconds")
    plt.tight_layout()
    plt.savefig("charts/evaluation_latency.png")
    plt.close()

    # Accuracy chart
    summary["accuracy_percent"].plot(kind="bar", title="Average Accuracy by Mode")
    plt.ylabel("Accuracy (%)")
    plt.tight_layout()
    plt.savefig("charts/evaluation_accuracy.png")
    plt.close()

    # Hallucination chart
    summary["hallucination_count"].plot(kind="bar", title="Average Hallucination Count by Mode")
    plt.ylabel("Hallucination Count")
    plt.tight_layout()
    plt.savefig("charts/evaluation_hallucination.png")
    plt.close()

    print("Evaluation charts generated in charts folder.")


if __name__ == "__main__":
    generate_evaluation_charts() 