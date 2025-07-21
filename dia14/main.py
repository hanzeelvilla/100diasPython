import random
from game_data import data

def comparar_seguidores(num1, num2):
    if(num1 > num2):
        return "A"
    elif(num2 > num1):
        return "B"
    else:
        return "igual"

def formatear_seguidores(num_seguidores):
    return "{:,}".format(num_seguidores)

jugar = True
score = 0

persona1 = random.choice(data)
persona2 = random.choice(data)

print("Bienvenido a Higher or Lower edición chafa\n")

while jugar:
    print("Quién tiene más seguidores?")
    print(f"A: {persona1["nombre"]} {persona1["descripcion"]} De {persona1["pais"]}")
    print(f"B: {persona2["nombre"]} {persona2["descripcion"]} De {persona2["pais"]}")

    res = input("Elije 'A' o 'B': ").upper()
    persona_con_mas_seguidodres = comparar_seguidores(persona1["seguidores"], persona2["seguidores"])

    print(f"{persona1["nombre"]}: {formatear_seguidores(persona1["seguidores"])} seguidores")
    print(f"{persona2["nombre"]}: {formatear_seguidores(persona2["seguidores"])} seguidores")

    if res == persona_con_mas_seguidodres or persona_con_mas_seguidodres == "igual":
        persona1 = persona2
        persona2 = random.choice(data)
        print("Correcto")
        score += 1

        print(f"Score: {score}")
    else:
        print("Has perdido")
        jugar = False

    print("-----------------------------------------------------------------------------------------------------------------------")

print(f"Score: {score}")