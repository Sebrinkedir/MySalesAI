import pandas as pd


class AnalysisAgent:
    """
    Performs deterministic computations on sales data.
    Computes relevant metrics based on the user's question.
    """

    def total_revenue(self, df):
        return int(df["revenue"].sum())

    def top_product(self, df):
        return df.groupby("product")["revenue"].sum().idxmax()

    def monthly_trend(self, df):
        df["date"] = pd.to_datetime(df["date"])

        monthly = df.groupby(
            df["date"].dt.to_period("M")
        )["revenue"].sum()

        return {
            str(month): int(value)
            for month, value in monthly.items()
        }

    def monthly_percentage_change(self, df):
        df["date"] = pd.to_datetime(df["date"])

        monthly = df.groupby(
            df["date"].dt.to_period("M")
        )["revenue"].sum()

        pct_change = monthly.pct_change() * 100

        return {
            str(month): round(value, 2) if pd.notna(value) else None
            for month, value in pct_change.items()
        }

    def compute_all(self, df, question):
        question = question.lower()

        results = {}

        if "total" in question or "revenue" in question:
            results["total_revenue"] = self.total_revenue(df)

        if "top" in question or "best" in question or "product" in question:
            results["top_product"] = self.top_product(df)

        if "trend" in question or "month" in question or "monthly" in question:
            results["monthly_trend"] = self.monthly_trend(df)

        if (
            "decrease" in question
            or "increase" in question
            or "drop" in question
            or "decline" in question
            or "change" in question
        ):
            results["monthly_trend"] = self.monthly_trend(df)
            results["monthly_percentage_change"] = self.monthly_percentage_change(df)

        if not results:
            results = {
                "total_revenue": self.total_revenue(df),
                "top_product": self.top_product(df),
                "monthly_trend": self.monthly_trend(df),
                "monthly_percentage_change": self.monthly_percentage_change(df)
            }

        return results