import pandas as pd

class AnalysisAgent:
    """
    Performs deterministic computations on sales data.
    This is CRITICAL: no hallucination, only real calculations.
    """

    def total_revenue(self, df):
        return df["revenue"].sum()

    def top_product(self, df):
        return df.groupby("product")["revenue"].sum().idxmax()

    def monthly_trend(self, df):
        df["date"] = pd.to_datetime(df["date"])
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
        return monthly.to_dict()

    def compute_all(self, df):
        return {
            "total_revenue": self.total_revenue(df),
            "top_product": self.top_product(df),
            "monthly_trend": self.monthly_trend(df)
        }