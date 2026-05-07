class InsightAgent:
    """
    Converts numerical analysis into human-readable business insights.
    """

    def generate_insight(self, analysis_results):

        total_revenue = analysis_results["total_revenue"]
        top_product = analysis_results["top_product"]
        trend = analysis_results["monthly_trend"]

        insight = f"""
=== SALES INSIGHTS ===

Total Revenue:
{total_revenue}

Top Performing Product:
{top_product}

Monthly Revenue Trend:
{trend}

Interpretation:
- The business generated a total revenue of {total_revenue}.
- The best-performing product was {top_product}.
- Monthly trends show how revenue evolved over time.

Further anomaly detection can improve strategic insights.
"""

        return insight