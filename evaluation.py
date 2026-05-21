import csv
import os
from datetime import datetime

from Agents.coordinator import Coordinator
from Agents.single_agent import SingleAgent
from Agents.data_agent import DataAgent


DATASETS = [
    "data/sample.csv",
    "data/real_sample.csv",
    "data/ecommerce_sales.csv",
    "data/retail_sales.csv",
    "data/supermarket_sales.csv"
]

TEST_QUESTIONS = [
    "Why did revenue decrease in March?",
    "Which product performed best?",
    "What is the monthly revenue trend?",
    "Provide an executive summary of business performance.",
    "Which product contributed most to revenue?",
    "Which month had the strongest performance?",
    "Which month had the worst performance?",
    "Did sales consistently improve over time?",
    "What are the major revenue trends in the business?"
]

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


def get_expected_keys(question):
    question = question.lower()

    if "product contributed" in question or "contribution" in question:
        return ["revenue_contribution_percent"]

    if "strongest performance" in question or "best month" in question:
        return ["best_month"]

    if "worst performance" in question or "worst month" in question:
        return ["worst_month"]

    if "consistently improve" in question or "trend direction" in question:
        return ["trend_direction"]

    if "executive summary" in question or "overall performance" in question:
        return [
            "total_revenue",
            "top_product",
            "monthly_trend",
            "best_month",
            "worst_month",
            "trend_direction"
        ]

    if "product" in question or "best" in question or "top" in question:
        return ["top_product"]

    if "trend" in question or "monthly" in question:
        return ["monthly_trend"]

    if (
        "decrease" in question
        or "increase" in question
        or "drop" in question
        or "decline" in question
    ):
        return ["monthly_trend", "monthly_percentage_change"]

    return ["total_revenue"]


def calculate_hallucination_score(insights):
    insights_lower = insights.lower()
    flagged_terms = []

    for term in UNSUPPORTED_TERMS:
        if term in insights_lower:
            flagged_terms.append(term)

    return len(flagged_terms), flagged_terms


def calculate_ground_truth(df):
    total_revenue = int(df["revenue"].sum())

    top_product = df.groupby("product")["revenue"].sum().idxmax()

    monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()

    monthly_trend = {
        str(month): int(value)
        for month, value in monthly.items()
    }

    pct_change = monthly.pct_change() * 100

    monthly_percentage_change = {
        str(month): round(value, 2) if value == value else None
        for month, value in pct_change.items()
    }

    best = monthly.idxmax()
    worst = monthly.idxmin()

    product_revenue = df.groupby("product")["revenue"].sum()
    total = product_revenue.sum()

    revenue_contribution_percent = {
        product: round(value, 2)
        for product, value in ((product_revenue / total) * 100).items()
    }

    if len(monthly) < 2:
        trend_direction = "Insufficient data"
    elif monthly.is_monotonic_increasing:
        trend_direction = "Consistently increasing"
    elif monthly.is_monotonic_decreasing:
        trend_direction = "Consistently decreasing"
    else:
        trend_direction = "Fluctuating"

    return {
        "total_revenue": total_revenue,
        "top_product": top_product,
        "monthly_trend": monthly_trend,
        "monthly_percentage_change": monthly_percentage_change,
        "best_month": {
            "month": str(best),
            "revenue": int(monthly.loc[best])
        },
        "worst_month": {
            "month": str(worst),
            "revenue": int(monthly.loc[worst])
        },
        "trend_direction": trend_direction,
        "revenue_contribution_percent": revenue_contribution_percent
    }


def calculate_accuracy(analysis, ground_truth, question):
    expected_keys = get_expected_keys(question)

    correct = 0
    total = len(expected_keys)

    for key in expected_keys:
        if key in analysis and analysis[key] == ground_truth[key]:
            correct += 1

    return round((correct / total) * 100, 2)


def save_result(
    dataset,
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
                "dataset",
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
            dataset,
            mode,
            question,
            analysis,
            insights,
            latency,
            accuracy,
            hallucination_count,
            flagged_terms
        ])


def evaluate_result(dataset, mode, question, result, ground_truth):
    hallucination_count, flagged_terms = calculate_hallucination_score(
        result["insights"]
    )

    accuracy = calculate_accuracy(
        result["analysis"],
        ground_truth,
        question
    )

    save_result(
        dataset,
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
    multi_agent = Coordinator()
    single_agent = SingleAgent()
    data_agent = DataAgent()

    for dataset in DATASETS:
        print(f"\n=== Evaluating Dataset: {dataset} ===")

        df = data_agent.load_data(dataset)
        ground_truth = calculate_ground_truth(df)

        for question in TEST_QUESTIONS:
            print(f"Question: {question}")

            multi_result = multi_agent.run(dataset, question)
            evaluate_result(
                dataset,
                "multi_agent",
                question,
                multi_result,
                ground_truth
            )

            single_result = single_agent.run(dataset, question)
            evaluate_result(
                dataset,
                "single_agent",
                question,
                single_result,
                ground_truth
            )

    print("\nAdvanced question-aware evaluation completed.")
    print("Results saved to logs/automated_evaluation.csv")


if __name__ == "__main__":
    run_evaluation() 