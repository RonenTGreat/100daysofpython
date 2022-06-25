from pprint import pprint


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Data for Cost
cost_espresso = MENU["espresso"]["cost"]
cost_latte = MENU["latte"]["cost"]
cost_cappuccino = MENU["cappuccino"]["cost"]

# Data for Water
water_espresso = MENU["espresso"]["ingredients"]["water"]
water_latte = MENU["latte"]["ingredients"]["water"]
water_cappuccino = MENU["cappuccino"]["ingredients"]["water"]

# Data for Coffee
coffee_espresso = MENU["espresso"]["ingredients"]["coffee"]
coffee_latte = MENU["latte"]["ingredients"]["coffee"]
coffee_cappuccino = MENU["cappuccino"]["ingredients"]["coffee"]

# Data for Milk
milk_latte = MENU["latte"]["ingredients"]["milk"]
milk_cappuccino = MENU["cappuccino"]["ingredients"]["milk"]



# Resources
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

change = 0
profit = 0


coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

print("Please insert coins.")
number_of_quarters = int(input("how many quarters?: "))
number_of_dimes = int(input("how many dimes?: "))
number_of_nickles = int(input("how many nickles?: "))
number_of_pennies = int(input("how many pennies? "))

money = (number_of_quarters * 0.25) + (number_of_dimes * 0.10) + (number_of_nickles * 0.50) + (number_of_pennies * 0.10)
print(money)
print(cost_latte)

if coffee_choice == 'espresso':
    if money < cost_espresso:
        print("Sorry that's not enough money. Money refunded.")
    elif water < water_espresso:
        print("Sorry there is not enough water.")
    elif coffee < coffee_espresso:
        print("Sorry there is not enough coffee.")
    elif money >= cost_espresso and water >= water_espresso and coffee >= coffee_espresso:
        change = money - cost_espresso
        resources["water"] = water - water_espresso
        resources["coffee"] = coffee - coffee_espresso
        coffee
        profit += cost_espresso
        print(f"Here is ${change} in change.")
        print("Here is your latte ☕️. Enjoy!")

    


