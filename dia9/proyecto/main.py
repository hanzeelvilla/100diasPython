print("Bievenido a la subasta secreta 🥶")

compradores = {}
agregarOtroComprador = True

while agregarOtroComprador:
    nombre = input("Nombre: ")
    dinero = int(input("Cuánto money? $"))
    compradores[nombre] = dinero

    opcion = input("Hay otro comprador? 'si' 'no': ").lower()

    if opcion == 'no':
        agregarOtroComprador = False

    print("\n" * 50)

max_dinero = -1
ganador = ""
for key in compradores:
    if compradores[key] > max_dinero:
        ganador = key
        max_dinero = compradores[key]

print(f"El ganador es: {ganador} con {max_dinero}")