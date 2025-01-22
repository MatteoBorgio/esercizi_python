'''
Cognome: Borgio            Nome: Matteo
Classe: 3 A/INFO           Data: 18/12/2024
Livello: Base
'''

import random as r

lista_base = ["Tony Stark", "Steve Rogers", "Thor Odinson", "Henry Pym", "Bruce Banner", "Clint Barton", "Wanda Maximoff", "T'Challa", "Natasha Romanoff", "Henry McCoy", "Susan Carol", "Monica Rambeau"]
lista_avanzato = ["Victor Von Doom", "Norman Osborn", "Otto Octavius", "Erik Magnus", "William Baker", "Quentin Beck", "Loki"]

dizionario_abbinamenti = {}   
lista_nomi_assegnati = []

for partecipante in lista_base:
    while True:
        nome_casuale = r.choice(lista_base)
        if nome_casuale not in lista_nomi_assegnati and nome_casuale != partecipante:             # if che impedisce che un partecipante faccia due volte il regalo o che regali a se stesso
            lista_nomi_assegnati.append(nome_casuale) 
            dizionario_abbinamenti[partecipante] = nome_casuale
            print(f"{dizionario_abbinamenti[partecipante]} ha fatto il regalo a {partecipante}")   # abbinamento di due partecipanti
            break

