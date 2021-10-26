class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0
    
    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()
    
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()

class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)

class InventoryExamer(ConsoleObserver):
    def __call__(self):
        if len(self.inventory.product) > 10:
            print("Examer Error: ", "name is too lengthy, hard to check")
        elif self.inventory.quantity < 10:
            print("Examer Error: ", "dangerous inventory water line")
        else:
            print("Examer Info: ","good")

if __name__ == "__main__":
    i = Inventory()
    c1 = ConsoleObserver(i)
    print("::going to be attach::")
    i.attach(c1)

    # specify if you need to exam the inventory
    c2 = InventoryExamer(i)
    i.attach(c2)

    print("::updating product::")
    i.product = "Widget not only good, but good good"
    print('::updating quantity::')
    i.quantity = 5
    i.product = "Widget"
    i.quantity = 100