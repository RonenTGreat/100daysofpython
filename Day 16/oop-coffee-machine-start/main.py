from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



coffee_make = CoffeeMaker()
money_report = MoneyMachine()
menu = Menu()

is_running = True


while is_running:
  option = menu.get_items()
  choice = input(f"What would you like? ({option}) ")

  if choice == "off":
    is_running = False
  elif choice == "report":
    coffee_make.report()
    money_report.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_make.is_resource_sufficient(drink) and money_report.make_payment(drink.cost):
      coffee_make.make_coffee(drink)
