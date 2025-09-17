## Create a coffee machine program that can make different types of coffee based on user input.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
            "sugar": 0
        },
        "price": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
            "sugar": 100
        },
        "price": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
            "sugar": 0
        },
        "price": 3.0
    }
}

## Resources in the coffee machine
resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "sugar": 100
}

profit = 0.0

def is_ingredients_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(profit, drink):
    """Deduct the required ingredients from the resources."""
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    profit += drink["price"]


## prompt user by asking "What would you like? (espresso/latte/cappuccino):"
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Sugar: {resources['sugar']}g")
        print(f"Money: ${profit}")
    else:
        if choice in MENU:
            drink = MENU[choice]
            if is_ingredients_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["price"]):
                    make_coffee(profit, drink)
                    change = round(payment - drink["price"], 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    print(f"Here is your {choice}. Enjoy!")