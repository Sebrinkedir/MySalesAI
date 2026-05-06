import pandas as pd

class DataAgent:
    """
    Responsible for loading and validating sales data.
    """

    def load_data(self, file_path):
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")

        return self.validate(df)

    def validate(self, df):
        # Basic validation rules
        if df.empty:
            raise ValueError("Dataset is empty")

        df = df.dropna(how="all")
        return df