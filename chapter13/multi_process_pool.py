from __future__ import annotations
from math import sqrt, ceil
import random
from multiprocessing.pool import Pool

def prime_factors(value: int) -> list[int]:
    if value in {2, 3}:
        return [value]
    factors: list[int] = []
    for divisor in range(2, ceil(sqrt(value)) + 1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            factors.extend(prime_factors(divisor))
            factors.extend(prime_factors(quotient))
        else:
            factors = [value]
        return factors

if __name__ == "__main__":
    to_factor = [
        random.randint(100000000, 10000000000)
        for i in range(40960)
    ]
    with Pool() as pool:
        results = pool.map(prime_factors, to_factor)
    primes = [
        value
        for value, factor_list in zip(to_factor, results)
            if len(factor_list) == 1
    ]
    print(f"9-digit primes {primes}")