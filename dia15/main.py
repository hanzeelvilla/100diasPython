from menu import MENU

VAL_QUARTER = .25
VAL_DIME = 0.10
VAL_NICKLE = 0.05
VAL_PENNY = 0.01

def hay_recursos(ingredientes):
    for key in ingredientes:
        if RECURSOS[key] < ingredientes[key]:
            return False
    
    return True

def procesar_monedas(quarters, dimes, nickles, pennies, precio_cafe):
    TOTAL_QUARTERS = quarters * VAL_QUARTER
    TOTAL_DIMES = dimes * VAL_DIME
    TOTAL_NICKLES = nickles * VAL_NICKLE
    TOTAL_PENNIES = pennies * VAL_PENNY

    TOTAL = TOTAL_QUARTERS + TOTAL_DIMES + TOTAL_NICKLES + TOTAL_PENNIES
    print(f"Dinero ingresado: {TOTAL}")

    if TOTAL == precio_cafe:
        return True
    elif TOTAL > precio_cafe:
        CAMBIO = TOTAL - precio_cafe
        print(f"Toma tu cambio: {CAMBIO}")
        return True
    else:
        RESTANTE = precio_cafe - TOTAL
        print(f"Dinero insuficiente, hacen falta {RESTANTE}")
        return False


RECURSOS = {
    "agua": 300,
    "leche": 200,
    "cafe": 100,
    "dinero": 0
}

maquina_encendida = True

while maquina_encendida:
    res = input("Qué quieres ordenar? (expresso/latte/capuccino): ").lower()

    if res == "reporte":
        for key in RECURSOS:
            print(f"{key}: {RECURSOS[key]}")
    elif res == "off":
        print("Apagando máquina")
        maquina_encendida = False
    elif res == "expresso" or res == "latte" or res == "capuccino":
        cafe = MENU[res]
        ingredientes_cafe = cafe["ingredientes"]

        if hay_recursos(ingredientes_cafe):
            precio_cafe = cafe["precio"]

            print(f"Ingresa tus monedas, el {res} cuesta ${precio_cafe}")
            quarters = int(input("Cuántos quarters? "))
            dimes = int(input("Cuántos dimes? "))
            nickles = int(input("Cuántos nickles? "))
            pennies = int(input("Cuántos pennies? "))

            procesar_monedas(quarters, dimes, nickles, pennies, precio_cafe)

        else:
            print(f"No hay suficientes recursos para hacer un {res}")
    else:
        print("Opción no válida")