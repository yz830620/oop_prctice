from collections import defaultdict

num_items = 0

def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])


if __name__ == "__main__":
    d = defaultdict(tuple_counter)
    d['a'][1].append('hello')
    d['b'][1].append('world')
    d['b'][1].append('world')
    d['b'][1].append('kkk')
    d['apple'][1].append('0')
    d['ban'][1].append('0')
    d['dsa'][1].append('0')
    
    del d['a']
    d['dds'][1].append('0')
    print(d)
