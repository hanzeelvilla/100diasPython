import random

inicio = 1
fin = 10

# Generar números aleatorios enteros 1 - 10
print(random.randint(inicio, fin))

# Generar números aleatorios float 0 - 1
print(random.random())

# Generar números aleatorios float 1 - 9
print(random.random() * 10)

# Generar números aleatorios float 1.00 - 9.00
print(round(random.random() * 10, 2))