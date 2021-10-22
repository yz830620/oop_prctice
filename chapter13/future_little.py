import concurrent.futures
 
FIBS = [28, 40, 20, 20, 23, 30, 10, 30]
 
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
 
 
def process():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, fib_value in zip(FIBS, executor.map(fib, FIBS)):
            print("%d's fib number is %d" % (number, fib_value))
 
if __name__ == '__main__':
    process()