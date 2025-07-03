import random

words = [
    "gato", "perro", "manzana", "zapato", "camisa", "libro", "ventana", "silla",
    "raton", "botella", "puerta", "carro", "mesa", "reloj", "camino", "luz",
    "sol", "luna", "estrella", "avion", "tren", "barco", "rio", "bosque", "cielo",
    "flor", "nube", "piedra", "fuego", "agua", "viento", "nieve", "trueno",
    "tormenta", "hoja", "arbol", "tierra", "montana", "playa", "arena", "mar",
    "isla", "cueva", "espada", "escudo", "pescado", "leche", "queso", "pan",
    "huevo", "sal", "azucar", "vino", "cuchara", "tenedor", "cuchillo", "plato",
    "vaso", "papel", "lapiz", "pluma", "cuaderno", "telefono", "pantalla",
    "teclado", "raton", "cable", "juego", "control", "pelota", "balon", "cancha",
    "bicicleta", "moto", "camion", "caja", "baul", "candado", "llave", "puente",
    "calle", "pared", "techo", "suelo", "espejo", "ropa", "sombrero", "zapato",
    "medias", "abrigo", "bufanda", "carpeta", "archivo", "carpintero", "doctor",
    "maestro", "ingeniero", "piloto", "soldado", "pintor", "cantante", "actor",
    "musico", "piano", "guitarra", "tambor", "violonchelo", "flauta", "trompeta",
    "orquesta", "danza", "teatro", "cine", "cuadro", "poesia", "cuento", "novela",
    "drama", "historia", "retrato", "escultura", "mapa", "globo", "mundo", "pais",
    "ciudad", "pueblo", "barrio", "familia", "padre", "madre", "hermano", "hermana",
    "tio", "tia", "primo", "prima", "abuelo", "abuela", "nino", "nina", "amigo",
    "vecino"
]
# 1. Seleccionar una palabra random
random_word = random.choice(words)
print(random_word)

# 2. El usuario hace un guess de una letra (transformarla a lowercase)
user_guess = input("Adivina una letra: ").lower()
print(user_guess)

# 3. Comprobar si la letra se encuentra en algun lugar de mi random word
def isLetterInWord(letter, word):
    res = []

    for char in word:
        res.append(letter == char.lower())
    
    return res

print(isLetterInWord(user_guess, random_word))