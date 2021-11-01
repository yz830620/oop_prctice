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
    x = yield from example3(1048)
    print('all sum: x:', x)
...

for i in example4():
    print('i:', i)