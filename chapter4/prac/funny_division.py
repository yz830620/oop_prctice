from typing import Union

def funniest_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise

if __name__ == "__main__":
    print(funniest_division(0))
    print(funniest_division('kkl'))
    funniest_division(13)