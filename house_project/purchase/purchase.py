"""class for defining purchase type, two standerd type as shown below"""
from house_project.propety.propety import get_valid_input
from house_project.propety.propety import House, Apartment


class Purchase:
    "buy it directly"
    def __init__(self, price="", taxex="", **kwargs):
        self.price = price
        self.taxex = taxex
    
    def display(self):
        super().display()
        print("PURCHASE DETAIL")
        print(f"selling price: {self.price}")
        print(f"estimated  taxes: {self.taxex}")

    @staticmethod
    def prompt_init():
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What is the estimated taxes? ")
        )


class Rental:
    "rent it instead of buy"
    def __init__(self, rent='', furnished='', utilities='', **kwargs):
        self.rent = rent
        self.furnished = furnished
        self.utilities = utilities

    def display(self):
        super().display()
        print("PURCHASE DETAIL")
        print(f"rent: {self.rent}")
        print(f"furnished: {self.furnished}")
        print(f"utilities: {self.utilities}")

    @staticmethod    
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What is the estimated utilities? "),
            furnished=get_valid_input("Is it property furnished? ", ('yes', 'no'))
        )
