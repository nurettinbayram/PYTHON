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

profit=0


def check_resources_sufficient(order_ingredients):
    """makinadaki yeterli malzeme olma durumunu kontrol eder."""
    for i in order_ingredients:
        if order_ingredients[i]>resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True

def calculate_coins():
    """Return coins calculate"""
    print("Please insert coins..")
    total = int(input("how many quarters : "))*0.25
    total += int(input("how many dimes : "))*0.10
    total += int(input("how many nickles : "))*0.05
    total += int(input("how many pennies : "))*0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received>=drink_cost:
        change = round(money_received-drink_cost,2) #iki karakter desimal yazar
        print(f"Here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print(f"Sorry that's not enough money.Money refunded.")
        return False

def report_resources():
    print("----------------------------")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit}")

def make_coffee(drink_name, order_inredients):
    for item in order_inredients:
        resources[item]-=order_inredients[item]
    print(f"Here your {drink_name}. Enjoy")




is_on=True



while is_on:
    choice = input("Prompt user by asking What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        is_on=False
    elif choice == "report":
        report_resources()

    else:
        drink=MENU[choice]
        sufficient = check_resources_sufficient(drink["ingredients"])

        if sufficient:
            paymet=calculate_coins()
            if is_transaction_successful(paymet, drink["cost"]):
                make_coffee(choice, drink["ingredients"])






