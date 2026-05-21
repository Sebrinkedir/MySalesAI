import pandas as pd


class AnalysisAgent:
    """
    Performs deterministic computations on sales data.
    Supports advanced business KPI analysis.
    """

    def total_revenue(self, df):
        return int(df["revenue"].sum())

    def top_product(self, df):
        return df.groupby("product")["revenue"].sum().idxmax()

    def monthly_trend(self, df):
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
        return {str(month): int(value) for month, value in monthly.items()}

    def monthly_percentage_change(self, df):
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
        pct_change = monthly.pct_change() * 100
        return {
            str(month): round(value, 2) if pd.notna(value) else None
            for month, value in pct_change.items()
        }

    def best_month(self, df):
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
        best = monthly.idxmax()
        return {
            "month": str(best),
            "revenue": int(monthly.loc[best])
        }

    def worst_month(self, df):
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
        worst = monthly.idxmin()
        return {
            "month": str(worst),
            "revenue": int(monthly.loc[worst])
        }

    def biggest_drop(self, df):
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
        pct_change = monthly.pct_change() * 100

        if pct_change.dropna().empty:
            return None

        drop_month = pct_change.idxmin()

        return {
            "month": str(drop_month),
            "percentage_change": round(pct_change.loc[drop_month], 2)
        }

    def revenue_contribution(self, df):
        product_revenue = df.groupby("product")["revenue"].sum()
        total = product_revenue.sum()

        contribution = (product_revenue / total) * 100

        return {
            product: round(value, 2)
            for product, value in contribution.items()
        }

    def average_monthly_revenue(self, df):
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
        return round(float(monthly.mean()), 2)

    def trend_direction(self, df):
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()

        if len(monthly) < 2:
            return "Insufficient data"

        if monthly.is_monotonic_increasing:
            return "Consistently increasing"

        if monthly.is_monotonic_decreasing:
            return "Consistently decreasing"

        return "Fluctuating"

    def compute_all(self, df, question):
        question = question.lower()
        results = {}

        if "total" in question:
            results["total_revenue"] = self.total_revenue(df)

        if "top" in question or "best product" in question or "product performed" in question:
            results["top_product"] = self.top_product(df)

        if "trend" in question or "monthly" in question or "over time" in question:
            results["monthly_trend"] = self.monthly_trend(df)
            results["trend_direction"] = self.trend_direction(df)

        if "decrease" in question or "increase" in question or "drop" in question or "decline" in question or "change" in question:
            results["monthly_trend"] = self.monthly_trend(df)
            results["monthly_percentage_change"] = self.monthly_percentage_change(df)
            results["biggest_drop"] = self.biggest_drop(df)

        if "best month" in question or "strongest month" in question or "highest month" in question:
            results["best_month"] = self.best_month(df)

        if "worst month" in question or "lowest month" in question:
            results["worst_month"] = self.worst_month(df)

        if "biggest drop" in question or "largest drop" in question:
            results["biggest_drop"] = self.biggest_drop(df)

        if "contribution" in question or "contributed" in question or "share" in question:
            results["revenue_contribution_percent"] = self.revenue_contribution(df)

        if "average" in question:
            results["average_monthly_revenue"] = self.average_monthly_revenue(df)

        if "summary" in question or "executive" in question or "overall performance" in question:
            results["total_revenue"] = self.total_revenue(df)
            results["top_product"] = self.top_product(df)
            results["monthly_trend"] = self.monthly_trend(df)
            results["monthly_percentage_change"] = self.monthly_percentage_change(df)
            results["best_month"] = self.best_month(df)
            results["worst_month"] = self.worst_month(df)
            results["trend_direction"] = self.trend_direction(df)
            results["revenue_contribution_percent"] = self.revenue_contribution(df)

        if not results:
            results = {
                "total_revenue": self.total_revenue(df),
                "top_product": self.top_product(df),
                "monthly_trend": self.monthly_trend(df),
                "monthly_percentage_change": self.monthly_percentage_change(df),
                "best_month": self.best_month(df),
                "worst_month": self.worst_month(df),
                "trend_direction": self.trend_direction(df),
                "revenue_contribution_percent": self.revenue_contribution(df)
            }

        return results 