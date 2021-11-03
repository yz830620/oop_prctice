def example3(inp):
    result = [0, 1]
    for i in range(2, inp):
        print(i)
        result.append(result[-2] + result[-1])
        result = result[-2:]
        yield result[-1]
    return result[-1]
...

def example4():
    x = yield from example3(1)
    print("x is over")
    x1 = yield from example3(7)
    print('no there is another x1')
    x2 = yield from example3(8)
    print('no there is x2')
    x3 = yield from example3(9)
    print('I just know x3 is an logic option')
    y = yield from example3(12)
    print('all sum: x + y:', x + x1 + x2 + x3 + y)
...

for i in example4():
    print('i:', i)