import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["#", "$", "%", "&"]

pswd = []

num_letters = int(input("Cuantas letras quieres? "))
num_numbers = int(input("Cuantos números quieres? "))
num_symbols = int(input("Cuantos símbolos quieres? "))

for num in range(0, num_letters):
    pswd.append(random.choice(letters))

for num in range(0, num_numbers):
    pswd.append(random.choice(numbers))

for num in range(0, num_symbols):
    pswd.append(random.choice(symbols))

random.shuffle(pswd)

print(f"Tu contraseña es: {"".join(pswd)}")