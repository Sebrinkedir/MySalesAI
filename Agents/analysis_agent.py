import pandas as pd

class AnalysisAgent:
    """
    Performs deterministic computations on sales data.
    No hallucinations — only verified calculations.
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

    def compute_all(self, df):
        return {
            "total_revenue": self.total_revenue(df),
            "top_product": self.top_product(df),
            "monthly_trend": self.monthly_trend(df),
            "monthly_percentage_change": self.monthly_percentage_change(df)
        }