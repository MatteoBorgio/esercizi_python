def gestione_spese(numero_categorie):
    categorie = []
    for i in range(numero_categorie):
        categoria = input(f"Inserisci una categoria: ")
        categorie.append(categoria)
    importi = []
    for i in range(len(categorie)):
        while True:
            try:
                importo = int(input(f"Inserisci l'importo per la categoria {categorie[i]}: "))
                if importo < 0:
                    print("L'importo non può essere negativo.")
                    continue
                break
            except ValueError:
                print("Devi inserire un numero valido.")
                continue
        importi.append(importo)
    totale_spese = sum(importi)
    spesa_maggiore = max(importi)
    spesa_minore = min(importi)
    categoria_maggiore = categorie[importi.index(spesa_maggiore)]
    categoria_minore = categorie[importi.index(spesa_minore)]

    return f"Il totale delle spese è {totale_spese}. La spesa maggiore è {spesa_maggiore}, nella categoria {categoria_maggiore}. La spesa minore è {spesa_minore}, nella categoria {categoria_minore}"

print(gestione_spese(2))