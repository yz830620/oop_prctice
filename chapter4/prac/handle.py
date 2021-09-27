from no_re import never_returns


def handler() -> None:
    try:
        never_returns()
        print("Never executed")
    except Exception as ex:
        print(f"!r: I caught an exception: {ex!r}")
        print(f"nothing: I caught an exception: {ex}")
        print(f"str: I caught an exception: {str(ex)}")
        print("Executed after the exception")


if __name__ == "__main__":
    handler()
