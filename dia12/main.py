import random

INICIO = 1
FIN = 100

print("Adivina el número: El Juego")
print("Estoy pensando en un número entre 1 y 100")

dificultad = input("Elije una dificultad. Escribe'facil' 'dificil': ").lower()

intentos = 0

if dificultad == "facil":
    intentos = 10
elif dificultad == "dificil":
    intentos = 5

random_num = random.randint(INICIO, FIN)
num_usuario = -1

while intentos > 0 and num_usuario != random_num:
    print(f"Tienes {intentos} intentos")
    num_usuario = int(input("Adivina el número: "))

    if num_usuario > random_num:
        print("Menos")
    elif num_usuario < random_num:
        print("Más")

    intentos -= 1

if num_usuario == random_num:
    print(f"Has adivinado, la respuesta era {random_num}")
else:
    print(f"Perdiste, la respuesta era {random_num}")