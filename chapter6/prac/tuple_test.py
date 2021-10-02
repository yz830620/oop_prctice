if __name__ == "__main__":
    stock = "FB", 75.00, 75.03, 74.90
    print(stock)
    print(type(stock))
    print(len(stock))
    print(dir(stock))
    print(stock[1:])
    """
    if you try to overwrite any value in tuple
    you will get: 
    TypeError: 'tuple' object does not support item assignment
    """