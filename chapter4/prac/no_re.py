from typing import NoReturn


class IWantToSayAsMoreDetailException(Exception):
    pass


def never_returns() -> NoReturn:
    print("1. I am about to raise an exception")
    raise IWantToSayAsMoreDetailException("2. This is always raised")
    print("3. this will not run")
    return "4. Also woun't return"

def call_exceptor() -> None:
    print("call_exceptor starts here...")
    never_returns()
    print("an exception was raised...")
    print("...so these lines don't run")

if __name__ == "__main__":
    call_exceptor()