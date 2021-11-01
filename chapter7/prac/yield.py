def foo():
    print("start...")
    throw = 10
    while True:
        inp = yield throw
        if inp:
            try:
                inp = int(inp)
                throw += inp
            except ValueError:
                print("please input a int")
        print("throw:",throw)
g = foo()
print(next(g))
print("*"*20)
print(g.send(100))
print(g.send(30))
print(g.send(5))
print(next(g))
print(next(g))
print(next(g))
print(g.send('100'))