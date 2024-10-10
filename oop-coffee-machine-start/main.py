from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
# items_0n_menu = MenuItem()
coffee_machine = CoffeeMaker()
money_calculator = MoneyMachine()

is_on = True


def resources():
    coffee_machine.report()
    money_calculator.report()


while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options})\n")
    if choice == "off":
        is_on = False
        print("Turning off machine. Goodbye!")
    elif choice == "report":
        resources()
    else:
        drink = my_menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            money_calculator.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)