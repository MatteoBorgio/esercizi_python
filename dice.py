import random

def roll(sides: int = 6) -> int:
    """
    Roll a single dice. Default is 6
    :param sides: The number of sides of the dice
    :return: A random number between 1 and sides
    """
    return random.randint(1, sides)

def lista_dadi(n, m):
    lista = []
    for i in range(n):
        dado = random.randint(1, m)
        lista.append(dado)

    return lista

def lista_dadi_ndm(ndm):
    lista = []
    x = ndm.split("d")
    n = int(x[0])
    m = int(x[1])
    for i in range(n):
        dado = random.randint(1, m)
        lista.append(dado)

    return lista

def lancio_vantaggio(n, m):
    lista = []
    for i in range(n):
        dado = random.randint(1, m)
        lista.append(dado)
    return max(lista)

def lista_vantaggio(n, m):
    lista_vantaggi = []
    for i in range(n):
        dado = random.randint(1, m)
        dado2 = random.randint(1, m)
        vantaggio = max(dado, dado2)
        lista_vantaggi.append(vantaggio)
    return lista_vantaggi

def somma_vantaggio(n, m):
    somma = 0
    for i in range(n):
        dado = random.randint(1, m)
        dado2 = random.randint(1, m)
        vantaggio = max(dado, dado2)
        somma += vantaggio
    return somma

    
def lista_risultati(x, ndm):
    lista = []
    ndm_split = ndm.split("d")
    n = int(ndm_split[0])
    m = int(ndm_split[1])
    for i in range(x):
        for i in range(n):
            dado = random.randint(1, m)
            lista.append(dado)
    return lista

def lista_risultati_vantaggio(x, ndm):
    lista = []
    ndm_split = ndm.split("d")
    n = int(ndm_split[0])
    m = int(ndm_split[1])
    for i in range(x):
        for i in range(n):
            dado = random.randint(1, m)
            dado2 = random.randint(1, m)
            vantaggio = max(dado, dado2)
            lista.append(vantaggio)
    return lista



        