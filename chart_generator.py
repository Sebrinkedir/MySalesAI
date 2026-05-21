import os
from datetime import datetime

import matplotlib.pyplot as plt


def generate_revenue_chart(monthly_trend):
    os.makedirs("charts", exist_ok=True)

    months = list(monthly_trend.keys())
    revenues = list(monthly_trend.values())

    plt.figure(figsize=(8, 4))
    plt.plot(months, revenues, marker="o")

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    chart_path = (
        f"charts/revenue_chart_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path 