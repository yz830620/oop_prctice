import math
import random
from threading import Thread, Lock
import time

THE_ORDERS = [
    "Reuben",
    "Ham and Cheese",
    "Monte Cristo",
    "Tuna Melt",
    "Cuban",
    "Grilled Chess",
    "French Dip",
    "BLT",
]


class Chef(Thread):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        random.seed(42)
        self.total = 0

    def get_order(self) -> None:
        self.order = THE_ORDERS.pop(0)

    def prepare(self) -> None:
        """Simulate doing a lot of work with a BIG computation"""
        start = time.monotonic()
        target = start + 1 + random.random()
        for i in range(1000000000):
            self.total += math.factorial(i)
            if i%1000 == 0:
                print(self.name, 'busy on ', start, target , i)
            if time.monotonic() >= target:
                break
        print(f"{time.monotonic(): .3f} {self.name} made {self.order}")

    def run(self) -> None:
        while True:
            try:
                self.get_order()
                self.prepare()
            except IndexError:
                break

if __name__ == "__main__":
    Mo = Chef("Michael")
    Constanine = Chef("Constantine")

    Mo.start()
    Constanine.start()