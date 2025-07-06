alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#texto = input("Escribe tu mensaje:\n").lower()
#desplazamiento = int(input("Cuánto desplazamiento? "))

def encriptar(texto, desplazamiento):
    texto_encriptado = ""

    for char in texto:
        if char in alfabeto:
            index_desplazado = alfabeto.index(char) + desplazamiento
            index_desplazado %= len(alfabeto)
            texto_encriptado += alfabeto[index_desplazado]
        else:
            texto_encriptado += char
    
    print(texto_encriptado)

encriptar("hola-nena-me-dicen-el-mike", 1)