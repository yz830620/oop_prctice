

if __name__ == "__main__":
    stocks = {
        "GOOG": (613.30, 625.86, 610.50),
        "MSFT": (30.25, 30.70, 30.19)
    }
    print(stocks["GOOG"])
    print(stocks.get("RIM", "Error: No stock <RIM> in database"))
    stocks.setdefault("GOOG", "NAN")
    print("GOOG", stocks["GOOG"])
    stocks.setdefault("BBRY", (10.5, 10.62, 10.39))
    print("BBRY", stocks["BBRY"])

    for stock, values in stocks.items():
        print(f"{stock} last value is {values[0]}")