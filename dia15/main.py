recursos = {
    "agua": 100,
    "leche": 50,
    "dinero": 0
}

res = input("Qué quieres ordenar? (expresso/latte/capuccino): ").lower()

if res == "reporte":
    for key in recursos:
        print(f"{key}: {recursos[key]}")