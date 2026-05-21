import pandas as pd

from Agents.dataset_profiler import DatasetProfiler


class DataAgent:
    """
    Loads, validates, profiles, and standardizes business datasets.
    Supports real-world column names using advanced schema mapping.

    Standard internal schema:
    - date
    - product
    - revenue

    Note:
    In non-product datasets, product may represent another business entity
    such as store, branch, region, category, or department.
    """

    def load_data(self, file_path):
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Please upload CSV or Excel.")

        df = self.validate(df)

        profiler = DatasetProfiler()
        profile = profiler.profile(df)

        print("\n=== DATASET PROFILE ===")
        print(profile)

        df = self.standardize_columns(df)

        return df

    def validate(self, df):
        if df.empty:
            raise ValueError("Dataset is empty.")

        df = df.dropna(how="all")
        return df

    def normalize_column_name(self, column):
        return (
            column.lower()
            .strip()
            .replace(" ", "_")
            .replace("-", "_")
            .replace(".", "_")
        )

    def find_column(self, df, aliases, preferred_type=None):
        normalized_columns = {
            self.normalize_column_name(col): col
            for col in df.columns
        }

        for alias in aliases:
            if alias in normalized_columns:
                return normalized_columns[alias]

        for normalized, original in normalized_columns.items():
            for alias in aliases:
                if alias in normalized:
                    return original

        if preferred_type == "numeric":
            numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
            if numeric_columns:
                return numeric_columns[0]

        if preferred_type == "date":
            for col in df.columns:
                converted = pd.to_datetime(df[col], errors="coerce")
                if converted.notna().sum() >= max(1, len(df) * 0.6):
                    return col

        return None

    def standardize_columns(self, df):
        date_aliases = [
            "date",
            "order_date",
            "invoice_date",
            "transaction_date",
            "sale_date",
            "sales_date",
            "created_at",
            "timestamp",
            "purchase_date",
            "billing_date",
            "week",
            "month"
        ]

        product_aliases = [
            "product",
            "product_name",
            "product_line",
            "item",
            "item_name",
            "sku",
            "category",
            "description",
            "stock_code",
            "brand",
            "department",
            "segment",
            "store",
            "branch",
            "region",
            "city",
            "customer_type",
            "sales_channel"
        ]

        revenue_aliases = [
            "revenue",
            "sales",
            "sales_amount",
            "amount",
            "total",
            "total_sales",
            "income",
            "turnover",
            "price",
            "unit_price",
            "weekly_sales",
            "net_sales",
            "gross_sales",
            "value",
            "invoice_amount",
            "order_value",
            "profit"
        ]

        date_col = self.find_column(df, date_aliases, preferred_type="date")
        product_col = self.find_column(df, product_aliases)
        revenue_col = self.find_column(df, revenue_aliases, preferred_type="numeric")

        missing = []

        if date_col is None:
            missing.append("date")

        if product_col is None:
            missing.append("product/store/category")

        if revenue_col is None:
            missing.append("revenue/sales amount")

        if missing:
            raise ValueError(
                f"Could not identify required columns: {missing}. "
                f"Available columns: {list(df.columns)}"
            )

        df = df.rename(
            columns={
                date_col: "date",
                product_col: "product",
                revenue_col: "revenue"
            }
        )

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")

        df = df.dropna(subset=["date", "product", "revenue"])

        if df.empty:
            raise ValueError(
                "After cleaning, no valid rows remain. "
                "Please check date, product/store/category, and revenue columns."
            )

        return df