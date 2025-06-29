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
    "water": 600,
    "milk": 500,
    "coffee": 100,
}

money=0


def check_resources_sufficient(item):
    item = MENU[item]['ingredients']
    for i in item:
        if item[i]>resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True

def calculate_coins():
    total = money
    total += int(input("how many quarters : "))*0.25
    total += int(input("how many dimes : "))*0.10
    total += int(input("how many nickles : "))*0.05
    total += int(input("how many pennies : "))*0.01
    return total

def renew_resources(j):
    item = MENU[j]['ingredients']
    for i in item:
        resources[i]=resources[i]-item[i]

def report_resources(item):
    print("----------------------------")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")
    renew_resources(item)
    check_transaction(item)

def check_transaction(item):
    global money
    money -= MENU[item]['cost']






while True:
    order = input("Prompt user by asking What would you like? (espresso/latte/cappuccino):")

    if order == "off":
        break
    elif order == "report":
        report_resources(order)

    else:
        sufficient = check_resources_sufficient(order)
        money = calculate_coins()

        if sufficient and money <= MENU[order]['cost']:
            print(f"Sorry that's not enough money.{money} Money refunded.")
            money=0
        else:
            report_resources(order)
            print(f"Here is your {order}. Enjoy!")
            report_resources(order)




