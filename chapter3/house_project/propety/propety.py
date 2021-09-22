"""file define class which define propety"""


def get_valid_input(input_string, valid_options):
    response = input(f"{input_string}({', '.join(valid_options)})  ")
    while response.lower() not in valid_options:
        print(f"please choose within ({', '.join(valid_options)})  ")
        response = input(input_string)
    return response


class Propety:
    """class which define propety"""
    def __init__(self, square_feet='', num_bedroom='', num_bathroom='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedroom = num_bedroom
        self.num_bathroom = num_bathroom

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print(f"square footage: {self.square_feet}")
        print(f"bedrooms: {self.num_bedroom}")
        print(f"bathrooms: {self.num_bathroom}")
        print()

    @staticmethod
    def prompt_init():
        return dict(square_feet = input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))


class House(Propety):
    """class to describe house"""
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    def __init__(self, num_stories='', garage='', fenced_yard='', **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        super().display()
        print("House Details")
        print(f"number of stories: {self.num_stories}")
        print(f"garage: {self.garage}")
        print(f"fence yard: {self.fenced_yard}")
    
    @staticmethod
    def prompt_init():
        parent_init = Propety.prompt_init()
        num_stories = input("How many stories? ")
        fenced = get_valid_input("Is there yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        parent_init.update({"fenced": fenced,
                            "garage": garage,
                            "num_stories": num_stories
                            })
        return parent_init


class Apartment(Propety):
    """class to describe apartment"""
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("Apartment Details")
        print(f"balcony: {self.balcony}")
        print(f"has laundry: {self.laundry}")

    @staticmethod
    def prompt_init():
        parent_init = Propety.prompt_init()
        balcony = get_valid_input("Is there balcony? ", House.valid_fenced)
        laundry = get_valid_input("Is there a laundry? ", House.valid_garage)
        parent_init.update({"balcony": balcony,
                            "laundry": laundry
                            })
        return parent_init
