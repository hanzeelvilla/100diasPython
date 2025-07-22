recursos = {
    "agua": 100,
    "leche": 50,
    "dinero": 0
}

maquina_encendida = True

while maquina_encendida:
    res = input("Qué quieres ordenar? (expresso/latte/capuccino): ").lower()

    if res == "reporte":
        for key in recursos:
            print(f"{key}: {recursos[key]}")
    elif(res == "off"):
        print("Apagando máquina")
        maquina_encendida = False
    else:
        print("Opción no válida")