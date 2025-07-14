import random

CARTAS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cartas_jugador = []
cartas_pc = []

for i in range(2):
    cartas_jugador.append(random.choice(CARTAS))
    cartas_pc.append(random.choice(CARTAS))

score_jugador = sum(cartas_jugador)
score_pc = sum(cartas_pc)
nueva_carta = True

print(f"Cartas de la PC: [{cartas_pc[0]}, ?]")
print(f"Tus cartas: {cartas_jugador}")
print(f"Tu score: {score_jugador}")

while score_jugador < 21 and score_pc < 21 and nueva_carta:
    opcion = input("Quieres otra carta? 'si' o 'no': ").lower()

    if opcion == "no":
        nueva_carta = False
    else:
        cartas_jugador.append(random.choice(CARTAS))
        score_jugador = sum(cartas_jugador)
    
    print(f"Tus cartas: {cartas_jugador}")
    print(f"Tu score: {score_jugador}")

# Dar resultados del juego
if score_jugador == 21:
    print("Has ganado")
    print(f"Tus cartas: {cartas_jugador}")
elif score_pc == 21:
    print("La computadora gana")
    print(f"Cartas de la PC: {cartas_pc}")
elif score_jugador > 21:
    print("Te has pasado")
    #print(f"Tus cartas: {cartas_jugador}")
