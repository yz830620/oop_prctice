from typing import Union

def funny_division(divisor: float) -> Union[str, float]:
    try:
        return 100 / divisor
    except ZeroDivisionError:
        return "Zero is not a good idea"

if __name__ == "__main__":
    print(funny_division(1.4))
    print(funny_division(0))
    print(funny_division("3.2"))
    # cannot operate both int and str
    