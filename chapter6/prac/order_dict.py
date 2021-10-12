from collections import KeysView, ItemsView, ValuesView


class DictSorted(dict):
    "dict class with insertion order option"
    def __new__(*args, **kwargs):
        new_dict = dict.__new__(*args, **kwargs)
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, value):
        "self[key] = value syntax"
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        super().__setitem__(key, value)

    def setdefault(self, key, value):
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        return super().setdefault(key, value)

    def key(self):
        return KeysView(self)

    def values(self):
        return ValuesView(self)

    def items(self):
        return ItemsView(self)

    def __iter__(self):
        "for x in self syntax"
        return self.ordered_keys.__iter__()


#test
if __name__ == "__main__":
    od = DictSorted()
    od['fruit'] = 'apple'
    od.setdefault('stock', 'msft')
    od.setdefault('stock', 'mitfy')
    od.setdefault('shark', 'mr.shark')
    od.setdefault('love_one', 'oh my god')
    print(od.ordered_keys)
    for k, v in od.items():
        print(k, v)