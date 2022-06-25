MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_enough(order_ingredients):
    '''Returns True when orders can be made'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def is_money_enough(money, cost_of_drink):
    '''Return True if payment is money is enough and False is money is not enough for drink'''
    if money >= cost_of_drink:
        change = round(money - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost_of_drink 
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
        
def make_coffee(drink_name, order_ingredients):
    '''Deducts the required ingredients from the resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Here is your latte ☕️. Enjoy!")



def convert_money():
    '''Calculates and return the total of coins in dollars'''
    print("Please insert coins.")
    number_of_quarters = int(input("how many quarters?: "))
    number_of_dimes = int(input("how many dimes?: "))
    number_of_nickles = int(input("how many nickles?: "))
    number_of_pennies = int(input("how many pennies? "))
    total = (number_of_quarters * 0.25) + (number_of_dimes * 0.10) + \
        (number_of_nickles * 0.05) + (number_of_pennies * 0.01)
    return total

is_running = True

while is_running:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_running = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_enough(drink["ingredients"]):
            payment = convert_money() 
            if is_money_enough(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
