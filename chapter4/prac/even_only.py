from typing import List


class EvenOnly(List[int]):
    def append(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Only intergers can be added", "hahaha, let me laugh a while")
        if value % 2 != 0:
            raise ValueError("Onle even numbers can be added")
        super().append(value)

if __name__ == "__main__":
    even = EvenOnly([2,3,4])
    even.append(4)
    print(even)
    even.append("are you sure?")