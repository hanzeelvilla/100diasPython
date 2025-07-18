import random

CARTAS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cartas_jugador = []
cartas_pc = []

def calcular_score(cartas):
    score = sum(cartas)

    if 11 in cartas and score > 21:
        cartas.remove(11)
        cartas.append(1)
        score = sum(cartas)
    
    return score

for i in range(2):
    cartas_jugador.append(random.choice(CARTAS))
    cartas_pc.append(random.choice(CARTAS))

score_jugador = calcular_score(cartas_jugador)
score_pc = calcular_score(cartas_pc)
nueva_carta = True

print(f"Cartas de la PC: [{cartas_pc[0]}, ?]")
print(f"Tus cartas: {cartas_jugador}")
print(f"Tu score: {score_jugador}")
print("--------------------------")

while score_jugador < 21 and score_pc < 21 and nueva_carta:
    opcion = input("Quieres otra carta? 'si' o 'no': ").lower()

    if opcion == "no":
        nueva_carta = False
    else:
        cartas_jugador.append(random.choice(CARTAS))
        score_jugador = calcular_score(cartas_jugador)
    
    print(f"Tus cartas: {cartas_jugador} = {score_jugador}")
    print("--------------------------")

# Dar resultados del juego
if score_jugador == 21:
    print("Has ganado")
    print(f"Tus cartas: {cartas_jugador} = {score_jugador}")
elif score_jugador > 21:
    print("Te has pasado")
    print(f"Tus cartas: {cartas_jugador} = {score_jugador}")
else:
    print("Turno de la computadora")

    while score_pc < 17 and score_pc < 21:
        cartas_pc.append(random.choice(CARTAS))
        score_pc = calcular_score(cartas_pc)

    # Dar resultados del juego
    if score_pc == 21:
        print("La computadora gana")
    elif score_pc > 21:
        print("La computadora se ha pasado")
        print("Has ganado")
    elif score_pc > score_jugador:
        print("La computadora gana")
    elif score_jugador > score_pc:
        print("Has ganado")
    else:
        print("Empate")

    print(f"Cartas de la PC: {cartas_pc} = {score_pc}")
    print(f"Tus cartas: {cartas_jugador} = {score_jugador}")