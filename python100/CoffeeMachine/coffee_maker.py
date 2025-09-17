class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        if self.resources["water"] < drink.water:
            print("Sorry there is not enough water.")
            return False
        if self.resources["milk"] < drink.milk:
            print("Sorry there is not enough milk.")
            return False
        if self.resources["coffee"] < drink.coffee:
            print("Sorry there is not enough coffee.")
            return False
        return True

    def make_coffee(self, drink):
        self.resources["water"] -= drink.water
        self.resources["milk"] -= drink.milk
        self.resources["coffee"] -= drink.coffee
        print(f"Here is your {drink.name}. Enjoy!")
