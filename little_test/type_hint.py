def odd(n: int) -> bool:
    return n % 2 != 0

def main() -> None:
    "this will failed"
    print(odd("not good"))

if __name__ == "__main__":
    main()