from collections import namedtuple

if __name__ == "__main__":
    Stock = namedtuple("Stock", 'symbol current high low')
    stock = Stock("FB", 75.00, 75.03, 74.90)
    print(stock)
    print(type(stock))
    print(len(stock))
    print("stock highest price: ", stock.high)
    print("stock lowerest price: ", stock.low)
    print("index", str(stock.index))
    print(dir(stock))
    print(stock[1:])
    """
    if you try to overwrite any value in tuple
    you will get: 
    TypeError: 'tuple' object does not support item assignment
    """