class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem("latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem("cappuccino", water=250, milk=100, coffee=24, cost=3.0)
        ]

    def get_items(self):
        return ", ".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None
