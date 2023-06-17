from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

machineOn = True


def check_resources(chosen_drink):
    """Returns True when order can be made, False when ingredients are not sufficient"""
    return my_coffee_maker.is_resource_sufficient(chosen_drink)
        

while machineOn:
    options = my_menu.get_items()
    userInput = input(f'What would you like? ({options})')

    if userInput == 'off':
        machineOn = False
        print('Turning off machine.')
        break 

    elif userInput == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    
    else:
        chosen_drink = my_menu.find_drink(userInput)
        if check_resources(chosen_drink) and my_money_machine.make_payment(chosen_drink.cost):
            my_coffee_maker.make_coffee(chosen_drink)