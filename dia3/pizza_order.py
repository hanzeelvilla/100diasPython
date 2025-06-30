print("Bienvenido a la picseria Hanzeel 😁")

size = input("Que tamaño de picsa queires? S, M o L: ")
peppe = input("Quieres pepperoni extra? Y o N: ")
cheese = input("Quieres queso extra? Y o N: ")

bill = 0

if size == "S":
    bill += 15

    if peppe == "Y":
        bill += 2

elif size == "M":
    bill += 20

    if peppe == "Y":
        bill += 3

elif size == "L":
    bill += 25

    if peppe == "Y":
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Tu cuenta es de: ${bill}")