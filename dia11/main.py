import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
pc_cards = []

for i in range(2):
    player_cards.append(random.choice(CARDS))
    pc_cards.append(random.choice(CARDS))

print(f"PC CARDS: {pc_cards}")
print(f"PLAYER CARDS: {player_cards}")

if sum(player_cards) == 21:
    print("Has ganado")
elif sum(pc_cards) == 21:
    print("La computadora gana")
