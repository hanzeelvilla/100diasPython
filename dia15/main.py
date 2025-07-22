from menu import MENU

def hay_recursos(tipo_cafe):
    ingredientes = tipo_cafe["ingredientes"]
    
    for key in ingredientes:
        if RECURSOS[key] < ingredientes[key]:
            return False
    
    return True

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
        hay_recursos(cafe)
        if hay_recursos(cafe):
            print("Hay suficientes recursos")
        else:
            print(f"No hay suficientes recursos para hacer un {res}")
    else:
        print("Opción no válida")