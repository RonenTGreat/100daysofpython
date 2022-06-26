from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_running = True

coffee_make = CoffeeMaker()
money_report = MoneyMachine()
menu = Menu()
item = MenuItem()

while is_running:
  choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

  if choice == "off":
    is_running = False
  elif choice == "report":
    coffee_make.report()
    money_report.report()
