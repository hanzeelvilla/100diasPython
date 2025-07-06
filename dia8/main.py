alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#texto = input("Escribe tu mensaje:\n").lower()
#desplazamiento = int(input("Cuánto desplazamiento? "))

def encriptar(texto, desplazamiento):
    texto_encriptado = ""

    for char in texto:
        char_index = alfabeto.index(char)
        new_char = alfabeto[char_index + desplazamiento]
        texto_encriptado += new_char
    
    print(texto_encriptado)

encriptar("hola", 1)