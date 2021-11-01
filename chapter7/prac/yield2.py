def fib2(n):
    result = []
    i, a, b = 0, 0, 1
    while True:
        if n <= 0 or i == n:
            break
        a, b = b, a + b
        result.append(a)
        yield result
        i += 1

d = fib2(1000)
for i in range(30):
    print(next(d))
