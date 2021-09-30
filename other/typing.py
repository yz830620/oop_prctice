from typing import List


class Contact:
    """class of contact"""
    all_contacts: List['Contact'] = []

    def __init__(self, name: 'str', phone:'str'):
        """init the class"""
        self.name = name
        self.phone = int(phone)
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        "redefine print"
        return (f"""{self.__class__.__name__}(
            {self.name!r}, {self.phone!r}
        )"""
        )
