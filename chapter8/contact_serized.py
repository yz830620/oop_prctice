import json


class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return (f"{self.first} {self.last}")


class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return {
                'is_contact': True,
                'first': obj.first,
                'last': obj.last,
                'full': obj.full_name
            }
        return super().default(obj)


def decode_contact(dic):
    if dic.get('is_contact'):
        return Contact(dic['first'], dic['last'])
    else:
        return dic

if __name__ == "__main__":
    c = Contact("John", "Ros")
    print(json.dumps(c, cls=ContactEncoder))
    
    data = ('{"is_contact": true, "first": "John", "last": "Ros", "full": "John Ros"}')
    c1 = json.loads(data, object_hook=decode_contact)
    print(c.full_name)
    assert c.full_name == c1.full_name
    print('assertion passed')