from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

maquina_encendida = True

while maquina_encendida:
    res = input(f"Qué quieres ordenar? ({menu.get_items()}): ").lower()

    if res == "off":
        print("Apagando la máquina...")
        maquina_encendida = False

    if res == "reporte":
        coffe_machine.report()

    if res == "espresso" or res == "latte" or res == "cappuccino":
        drink = menu.find_drink(res)
        
        if coffe_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_machine.make_coffee(drink)
        else:
            print(f"No podemos hacer tu {res}")