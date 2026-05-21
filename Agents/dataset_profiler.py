import pandas as pd


class DatasetProfiler:

    def profile(self, df):

        profile = {
            "rows": len(df),
            "columns": list(df.columns),
            "date_columns": [],
            "numeric_metrics": [],
            "categorical_dimensions": [],
            "possible_revenue_columns": [],
            "possible_entity_columns": []
        }

        revenue_keywords = [
            "revenue",
            "sales",
            "amount",
            "total",
            "income",
            "turnover",
            "price",
            "profit",
            "value"
        ]

        entity_keywords = [
            "product",
            "item",
            "category",
            "store",
            "branch",
            "region",
            "city",
            "department",
            "segment",
            "customer"
        ]

        date_keywords = [
            "date",
            "time",
            "created",
            "invoice",
            "order"
        ]

        for col in df.columns:

            col_lower = (
                col.lower()
                .replace(" ", "_")
            )

            # -------- DATE DETECTION --------

            if (
                not pd.api.types.is_numeric_dtype(df[col])
                and any(keyword in col_lower for keyword in date_keywords)
            ):

                converted_date = pd.to_datetime(
                    df[col],
                    errors="coerce"
                )

                valid_ratio = (
                    converted_date.notna().sum() / max(1, len(df))
                )

                if valid_ratio >= 0.8:
                    profile["date_columns"].append(col)

            # -------- NUMERIC METRICS --------

            if pd.api.types.is_numeric_dtype(df[col]):

                profile["numeric_metrics"].append(col)

                if any(
                    keyword in col_lower
                    for keyword in revenue_keywords
                ):
                    profile["possible_revenue_columns"].append(col)

            # -------- CATEGORICAL DIMENSIONS --------

            if (
                df[col].dtype == "object"
                and col not in profile["date_columns"]
            ):

                unique_ratio = (
                    df[col].nunique() / max(1, len(df))
                )

                if unique_ratio <= 0.8:
                    profile["categorical_dimensions"].append(col)

                if any(
                    keyword in col_lower
                    for keyword in entity_keywords
                ):
                    profile["possible_entity_columns"].append(col)

        return profile