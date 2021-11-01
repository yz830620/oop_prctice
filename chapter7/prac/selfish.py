"""for better understanding yield and yield from, write some testcase"""


def selfish_guy(num: int) -> int:
    i = 0
    while i < num:
        yield i
        i += 1


self_10 = selfish_guy(10)

print(self_10)