
def find_insert_loc(li , num):
    hi = len(li)
    lo = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if num < li[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def find_insert_left(li , num):
    hi = len(li)
    lo = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if li[mid] < num:
            lo = mid + 1
        else:
            hi = mid
    return lo

def insert_new_num(li, num):
    loc = find_insert_loc(li, num)
    li.insert(loc, num)

def remove_old_num(li, num):
    loc = find_insert_left(li, num)
    del li[loc]


if __name__ == "__main__":
    list_a = [1, 4, 8]
    new_number_1 = 7
    new_number_2 = 8
    list_a.insert(2, new_number_1)
    print(list_a)
    # [1, 4, 7, 8]
    # how to know we should put 2