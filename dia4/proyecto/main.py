import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
tijeras = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

opciones = [piedra, papel, tijeras]
pc_decision = random.randint(0, len(opciones) - 1)

print("Piedra, papel o tijera VS la PC")
user_decision = int(input('''
    Que elijes?
      1. Piedra
      2. Papel
      3. Tijeras
                      
    Respuesta: '''))

print("Tu elección:\n")
print(opciones[user_decision - 1])
print("Decisión de la PC:")
print(opciones[pc_decision])

if user_decision == 1: # piedra
    if pc_decision == 2:
        print("Tu ganas")
    elif pc_decision == 1:
        print("Pierdes")
    else:
        print("Empate")
elif user_decision == 2: # papel
    if pc_decision == 0:
        print("Tu ganas")
    elif pc_decision == 2:
        print("Pierdes")
    else:
        print("Empate")
elif user_decision == 3: # tijeras
    print("Tijeras")

    if pc_decision == 1:
        print("Tu ganas")
    elif pc_decision == 0:
        print("Pierdes")
    else:
        print("Empate")
else:
    print("Opción no válida")
