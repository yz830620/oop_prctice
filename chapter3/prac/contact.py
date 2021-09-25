class Contact:
    all_contacts = ()
    # if this is immutable. It will be different

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts += (self,)

    def __repr__(self):
        return f"{self.__class__}, name: {self.name}"

if __name__ == "__main__":
    even = Contact("even","apple@com")
    strong = Contact("strong","apple@com")
    print(even.all_contacts)