# Nome: Matteo Borgio
# Partner: /

import random as r
import dice as d

turno = 0

armate_giocatore1 = int(input("inserisci le armate del giocatore 1 (indica un numero tra 7 e 12): "))
armate_giocatore2 = int(input("inserisci le armate del giocatore 2 (indica un numero tra 7 e 12):"))

while armate_giocatore1 < 7 or armate_giocatore2<7 or armate_giocatore1>12 or armate_giocatore2>12:
        print("Il numero di armate inserite non è valido. Inserisci un numero tra 7 e 12.")
        armate_giocatore1 = int(input("inserisci le armate del giocatore 1 (indica un numero tra 7 e 12): "))
        armate_giocatore2 = int(input("inserisci le armate del giocatore 2 (indica un numero tra 7 e 12): "))

while True:

    turno += 1
    
    print(f"Turno {turno} \n")

    print(f"Il giocatore 1 ha {armate_giocatore1} armate.")
    print(f"Il giocatore 2 ha {armate_giocatore2} armate.\n")

    dadi_attacco = []
    dadi_difesa = []

    armate_attacco = int(input("Con quante armate vuoi attaccare (massimo 3)? "))

    armate_difesa = int(input("Con quante armate vuoi difendere (massimo 3)? "))

    while armate_attacco > 3 or armate_difesa > 3 or armate_attacco <0 or armate_difesa < 0:
        print("Hai inserito un numero di armate non valido.")
        armate_attacco = int(input("Con quante armate vuoi attaccare (massimo 3)? "))
        armate_difesa = int(input("Con quante armate vuoi difendere(massimo 3)? "))

    while armate_attacco > armate_giocatore1:
        print("Non puoi attaccare con più armate rispetto a quelle che possiedi.")
        armate_attacco = int(input("Con quante armate vuoi attaccare (massimo 3)? "))

    while armate_difesa > armate_giocatore2:
        print("Non puoi difendere con più armate rispetto a quelle che possiedi.")
        armate_attacco = int(input("Con quante armate vuoi difendere (massimo 3)? "))

    for i in range(armate_attacco):
        dado = d.roll()
        dadi_attacco.append(dado)
    
    for i in range(armate_difesa):
        dado = d.roll()
        dadi_difesa.append(dado)

    dadi_difesa.sort(reverse = True)
    dadi_attacco.sort(reverse = True)
    
    print(f"I dadi dell'attacco sono: {dadi_attacco}")
    print(f"I dadi del difesa sono: {dadi_difesa} \n")

    if len(dadi_attacco) > len(dadi_difesa):
        lista_corta = dadi_difesa
    elif len(dadi_difesa) > len(dadi_attacco):
        lista_corta = dadi_attacco
    else:
        lista_corta = dadi_attacco

    for i in range(len(lista_corta)):
        if dadi_attacco[i] > dadi_difesa[i]:
            armate_giocatore2 -= 1
            print(f"Il giocatore 2 perde un'armata.\n")
        elif dadi_difesa[i] > dadi_attacco[i]:
            armate_giocatore1 -= 1
            print(f"Il giocatore 1 perde un'armata.\n")
        else: 
            armate_giocatore1 -= 1
            print(f"Il giocatore 1 perde un'armata. \n")

        if armate_giocatore1 == 0 and armate_giocatore2 > 0:
            print(f"Il giocatore 1 ha perso tutte le sue armate.\n")
            print("Il giocatore 2 ha vinto! \n")
            break
        elif armate_giocatore2 == 0 and armate_giocatore1 > 0:
            print(f"Il giocatore 2 ha perso tutte le sue armate.\n")
            print("Il giocatore 1 ha vinto! \n")
            break
        elif armate_giocatore1 == 0 and armate_giocatore2 == 0:
            print("Pareggio! \n")
            break
    
    if armate_giocatore1 == 0 or armate_giocatore2 == 0:
        print("partita finita!")
        break
    
        



            
    
    

    
        


   

                
        

        



    

    





