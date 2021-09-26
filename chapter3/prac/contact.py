from __future__ import annotations
from typing import List, Protocol


class ContactList(list["Contact"]):
    def search(self, name: str) -> list["Contact"]:
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    # all_contacts = ()
    all_contacts = ContactList()
    # if this is immutable. It will be different

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Contact.all_contacts += (self,)
        self.all_contacts.append(self)

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"name: {self.name!r}, {self.email!r}"
                ")"
            )

class Emailable(Protocol):
    email: str


class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        print(f"Sending mail to {self.email=}")
        # Add e-mail logic here


class EmailableContact(Contact, MailSender):
    pass


class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )

if __name__ == "__main__":
    even = Contact("even","even@apple.com")
    strong = Contact("strong","strong@apple.com")
    asker = Supplier("asker","asker@apple.com")
    print(even.all_contacts)
    asker.order('apple')

    even_mail = EmailableContact("even","even@apple.com")
    even_mail.send_mail("this is cool huh?")