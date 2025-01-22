from random import randint

health_points = 30
turns = 0

while health_points > 0:
    if turns == 0:
        print(f"Initial health points: {health_points}")
    else:
        print(f"Remaining health is: {health_points}")
    turns += 1
    damage = randint(1, 6)
    print(f"Damage taken: {damage}.")
    health_points -= damage
    if health_points <= 0:
        health_points = 0
        print(f"Remaing health points: {health_points}")
        print("The character has been defeated.")
        print(f"{turns} turns was played.")