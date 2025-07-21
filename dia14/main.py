import random
from game_data import data

def comparar_seguidores(persona1, persona2):
    if(persona1["seguidores"] > persona2["seguidores"]):
        return "A"
    elif(persona2["seguidores"] > persona1["seguidores"]):
        return "B"
    else:
        "igual"

persona1 = random.choice(data)
persona2 = random.choice(data)

print("Bienvenido a Higher or Lower edición chafa\n")
print("Quién tiene más seguidores?")
print(f"A: {persona1["nombre"]} {persona1["descripcion"]} De {persona1["pais"]}")
print(f"B: {persona2["nombre"]} {persona2["descripcion"]} De {persona2["pais"]}")

res = input("Elije 'A' o 'B': ").upper()
persona_con_mas_seguidodres = comparar_seguidores(persona1, persona2)

if res == persona_con_mas_seguidodres :
    print("Has adivinado")
elif persona_con_mas_seguidodres == "igual":
    print("Tienen los mismos")
else:
    print("Has perdido")

print(f"{persona1["nombre"]}: {persona1["seguidores"]} seguidores")
print(f"{persona2["nombre"]}: {persona2["seguidores"]} seguidores")