def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir
}

operaciones_validas = ["+", "-", "*", "/"]
continuar = True
mismo_num = "no"

print("Bienvenido a la calculadora simple")

while continuar:
    if mismo_num != "si":
        numero1 = float(input("Primer número: "))
    else:
        numero1 = res

    operacion = input(
        "+\n"
        "-\n"
        "*\n"
        "/\n"
        "Elije una operación: "
    )
    numero2 = float(input("Segundo número: "))

    if(operacion in operaciones_validas):
        res = operaciones[operacion](numero1, numero2)
        print(f"{numero1} {operacion} {numero2} = {res}")
    else:
        print("La operación no es válida")
    
    mismo_num = input(f"Quieres usar {res} para otra operacion? 'si' o 'no': ").lower()
    
    if mismo_num != "si":
        decision = input("Quieres salir del programa? 'si' o 'no': ")
    
        if decision == "si":
            continuar = False

print("Adios popo")