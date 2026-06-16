from data.data_loader import DataLoader


def main():

    loader = DataLoader("data/sample_stock.csv")

    market_data = loader.load_data()

    print("\nMarket Data:\n")
    print(market_data)

    print("\nColumns:")
    print(market_data.columns)

    print("\nShape:")
    print(market_data.shape)
    
    print("\nFirst 3 rows:")
    print(market_data.head())

    print("\nLast 2 rows:")
    print(market_data.tail())

    print("\nColumns:")
    print(market_data.columns)

    print("\nShape:")
    print(market_data.shape)

    print("\nData types:")
    print(market_data.dtypes)
    print("Closing prices\n")
    print(market_data["Close"])
if __name__ == "__main__":
    main()