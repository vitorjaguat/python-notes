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
    "money": 0
}

machineOn = True


def check_resources(chosen_drink):
    for key, value in MENU[chosen_drink]["ingredients"].items():
        if value > resources[key]:
            return f"Sorry, there is not enough {key}."
        else:
            return "ok"


while machineOn:
    userInput = input('What would you like? (espresso/latte/cappuccino)')

    if userInput == 'off':
        machineOn = False
        print('Turning off machine.')
        break 
    
    if userInput == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')

    else:
        response = check_resources(userInput)
        if response == "ok":
            print('Now insert the coins!')
            quarters_in = int(input('Quarters inserted: '))
            dimes_in = int(input('Dimes inserted: '))
            nickles_in = int(input('Nickles inserted: '))
            pennies_in = int(input('Pennies inserted: '))
            total_in = quarters_in * 0.25 + dimes_in * 0.1 + nickles_in * 0.05 + pennies_in * 0.01
            if total_in < MENU[userInput]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                resources["money"] += MENU[userInput]["cost"]
                for ingredient, quantity in MENU[userInput]["ingredients"].items():
                    print(ingredient)
                    resources[ingredient] -= quantity
                if total_in > MENU[userInput]["cost"]:
                    print(f"Here is ${total_in - MENU[userInput]['cost']} dollars in change.")
                print(f'Here is your {userInput}. Enjoy!')

        else:
            print(response)
