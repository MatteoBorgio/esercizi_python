import dice as d
import random as r

attaccante = r.randint(5, 8)

difensore = r.randint(5, 8)

print(f"Il difensore inizia con {difensore} armate \n")
print(f"Attaccante inizia con {attaccante} armate \n")

turno = 0

while attaccante > 0 and difensore > 0:
    turno += 1
    print(f"Turno {turno} \n")
    lista_dadi_attaccante = []
    lista_dadi_difensore = []
    for i in range(3):
        armate_perse_difensore = 0
        armate_perse_attaccante = 0
        attacco = d.roll(6)
        lista_dadi_attaccante.append(attacco)
        difesa = d.roll(6)
        lista_dadi_difensore.append(difesa)

    if attaccante <= 0:
        attaccante = 0
    if difensore <= 0:
        difensore = 0

    print(f"In questo turno i risultati dei dado dell'attaccante sono stati: {lista_dadi_attaccante} \n")
    print(f"In questo turno i risultati dei dado del difensore sono stati: {lista_dadi_difensore} \n")

    if lista_dadi_attaccante[0] <= lista_dadi_difensore[0]:
        print("Dal primo lancio l'attaccante perde un'armata. \n")
        attaccante -= 1
        armate_perse_attaccante += 1
    else:
        difensore -= 1
        armate_perse_difensore += 1
        print("Dal primo lancio il difensore perde un'armata. \n")
    if lista_dadi_attaccante[1] <= lista_dadi_difensore[1]:
        print("Dal secondo lancio l'attaccante perde un'armata. \n")
        attaccante -= 1
        armate_perse_attaccante += 1
    else:
        print("Dal secondo lancio il difensore perde un'armata. \n")
        difensore -= 1
        armate_perse_difensore += 1
    if lista_dadi_attaccante[2] <= lista_dadi_difensore[2]:
        print("Dal terzo lancio l'attaccante perde un'armata. \n")
        attaccante -= 1
        armate_perse_attaccante += 1
    else:
        print("Dal terzo lancio il difensore perde un'armata. \n")
        difensore -= 1
        armate_perse_difensore += 1

    print(f"Alla fine del turno, all'attaccante rimangono {attaccante} armate \n")
    print(f"Alla fine del turno, al difensore rimangono {difensore} armate \n")

    if armate_perse_attaccante < armate_perse_difensore:
        print(f"L'attaccante ha vinto il turno {turno}! \n")
    else:
        print(f"Il difensore ha vinto il turno {turno}! \n")

    if attaccante <= 0 or difensore <= 0:
        print("Armate attaccante: 0 \n" if attaccante <= 0 else "Armate difensore: 0 \n")
        break

print("Il vincitore è:", "Attaccante \n" if attaccante > 0 else "Difensore \n")

if attaccante == 0 and difensore == 0: 
    print("Il gioco è finito in pareggio! \n")
      



