from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine = CoffeeMaker()
menu = Menu()

maquina_encendida = True

while maquina_encendida:
    res = input(f"Qué quieres ordenar? ({menu.get_items()}): ").lower()

    if res == "off":
        print("Apagando la máquina...")
        maquina_encendida = False

    if res == "reporte":
        coffe_machine.report()