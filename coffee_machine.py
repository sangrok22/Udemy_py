import math

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



should_continue = True

while should_continue:
    choose = input("What do you like? (espresso/latte/cappuccino): ")
    if choose == "off":
        break
    elif choose == "report":
        print(f"water: {resources['water']}m")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")

    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    pay= MENU[choose]["cost"]
    in_coin = (0.25*quarters)+(0.1*dimes)+(0.05*nickles)+(0.01*pennies)
    change = round(in_coin - pay ,2)
    if change < 0:
        print("Sorry that's not enough money")
        should_continue = False
    else:
        print(f"Here is ${change} in change.")