alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(texto, desplazamiento, opcion):
    nuevo_texto = ""    

    if opcion == "desencriptar":
        desplazamiento *= -1

    for char in texto:
        if char in alfabeto:
            index_desplazado = alfabeto.index(char) + desplazamiento
            index_desplazado %= len(alfabeto)
            nuevo_texto += alfabeto[index_desplazado]
        else:
            nuevo_texto += char
    
    print(f"Resultado: {nuevo_texto}")

run = True

while run:
    direccion = input("Quieres 'encriptar' o 'desencriptar'? ").lower()
    texto = input("Escribe tu mensaje:\n").lower()
    desplazamiento = int(input("Cuánto desplazamiento? "))
    caesar(texto, desplazamiento, direccion)

    res = input("Quieres segir usando el programa? 'Si' o 'No': ").lower()

    if res == "no":
        run = False

print("Adios popó")