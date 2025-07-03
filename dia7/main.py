import random

WORDS = [
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
    "tio", "tia", "primo", "prima", "abuelo", "abuela", "niño", "niña", "amigo",
    "vecino"
]

TITLE = "AHORCADO"

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']


# Seleccionar una palabra random
random_word = random.choice(WORDS)
#print(random_word)
#print(len(random_word))

# Ocultar la palabra
def hide_word(word):
    new_word = []
    for _ in word:
        new_word.append("_")
    
    return new_word

hidden_word_list = hide_word(random_word)
hidden_word_str = "".join(hidden_word_list)
guessed_letters = []

life_count = len(HANGMANPICS) # 7

print(TITLE + "\n")

while(life_count > 0 and hidden_word_str != random_word):
    hidden_word_change = False

    print(f"Palabra secreta: {hidden_word_str}")
    user_guess = input("Adivina una letra: ").lower()

    for i, char in enumerate(random_word):
        if user_guess == char and char not in guessed_letters:
            hidden_word_list[i] = char
            hidden_word_change = True
    
    guessed_letters.append(user_guess)
    
    if not hidden_word_change:
        print(HANGMANPICS[len(HANGMANPICS) - life_count])
        print("Ops letra equivocada")
        life_count -= 1

    print("\n")
    hidden_word_str = "".join(hidden_word_list)

if hidden_word_str == random_word:
    print("GANASE")
else:
    print("PERDISTE")

print(F"Palabra secreta: {random_word}")