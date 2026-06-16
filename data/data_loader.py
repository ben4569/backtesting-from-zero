# data/data_loader.py

import pandas as pd


class DataLoader:
    """
    Loads OHLCV market data from CSV files.
    """

    REQUIRED_COLUMNS = [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    def __init__(self, filepath: str):
        """
        Initialize loader with CSV file path.
        """
        self.filepath = filepath

    def load_data(self) -> pd.DataFrame:
        """
        Load and clean market data.
        """

        # Read CSV
        df = pd.read_csv(self.filepath)

        # Validate required columns
        missing_columns = [
            col for col in self.REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        # Convert Date column to datetime
        df["Date"] = pd.to_datetime(df["Date"])

        # Sort data by time
        df = df.sort_values("Date")

        # Set Date as index
        df = df.set_index("Date")

        return df