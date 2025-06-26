print("Bienvenido a la calculadora de propinas ☝️ 🤓")
cuenta = float(input("Cuánto es el total de la cuenta? "))
propina = int(input("Cuánto porcentaje de propina quieren dejar? "))
personas = int(input("Entre cuentas personas se va a dividr la cuenta? "))

total = cuenta + propina / 100 * cuenta
pago_por_persona = total / personas
print(f"Cada persona debe pagar: ${round(pago_por_persona, 2)} para pagar ${round(total, 2)}")