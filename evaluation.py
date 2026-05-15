import csv
import os
from datetime import datetime

from Agents.coordinator import Coordinator
from Agents.single_agent import SingleAgent


TEST_QUESTIONS = [
    "Why did revenue decrease in March?",
    "Which product performed best?",
    "What is the monthly revenue trend?"
]


GROUND_TRUTH = {
    "total_revenue": 1000,
    "top_product": "B",
    "monthly_trend": {
        "2024-01": 300,
        "2024-02": 450,
        "2024-03": 250
    },
    "monthly_percentage_change": {
        "2024-01": None,
        "2024-02": 50.0,
        "2024-03": -44.44
    }
}


UNSUPPORTED_TERMS = [
    "competition",
    "competitor",
    "seasonal",
    "seasonality",
    "marketing",
    "promotion",
    "customer behavior",
    "customer feedback",
    "inventory",
    "stock",
    "pricing",
    "supply chain",
    "market conditions"
]


def calculate_accuracy(analysis):
    correct = 0
    total = 0

    for key, true_value in GROUND_TRUTH.items():
        if key in analysis:
            total += 1

            if analysis[key] == true_value:
                correct += 1

    if total == 0:
        return None

    return round((correct / total) * 100, 2)


def calculate_hallucination_score(insights):
    insights_lower = insights.lower()

    flagged_terms = []

    for term in UNSUPPORTED_TERMS:
        if term in insights_lower:
            flagged_terms.append(term)

    hallucination_count = len(flagged_terms)

    return hallucination_count, flagged_terms


def save_result(
    mode,
    question,
    analysis,
    insights,
    latency,
    accuracy,
    hallucination_count,
    flagged_terms
):
    file_path = "logs/automated_evaluation.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "mode",
                "question",
                "analysis",
                "insights",
                "latency_seconds",
                "accuracy_percent",
                "hallucination_count",
                "flagged_terms"
            ])

        writer.writerow([
            datetime.now(),
            mode,
            question,
            analysis,
            insights,
            latency,
            accuracy,
            hallucination_count,
            flagged_terms
        ])


def evaluate_result(mode, question, result):
    accuracy = calculate_accuracy(result["analysis"])

    hallucination_count, flagged_terms = calculate_hallucination_score(
        result["insights"]
    )

    save_result(
        mode,
        question,
        result["analysis"],
        result["insights"],
        result.get("latency_seconds"),
        accuracy,
        hallucination_count,
        flagged_terms
    )


def run_evaluation():
    file_path = "data/sample.csv"

    multi_agent = Coordinator()
    single_agent = SingleAgent()

    for question in TEST_QUESTIONS:
        print(f"\nEvaluating question: {question}")

        multi_result = multi_agent.run(file_path, question)
        evaluate_result("multi_agent", question, multi_result)

        single_result = single_agent.run(file_path, question)
        evaluate_result("single_agent", question, single_result)

    print("\nAutomated evaluation completed.")
    print("Results saved to logs/automated_evaluation.csv")


if __name__ == "__main__":
    run_evaluation()