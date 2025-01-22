def trova_divisori(numero: int) -> list:
    """
    Questa funzione prende come argomento un numero intero positivo
    e restituisce una lista dei suoi divisori interi.
    """
    divisori = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisori.append(i)
    return f"I divisori di {numero} sono {divisori}"

def is_prime(numero: int) -> bool:
    """
    Questa funzione prende come argomento un numero intero positivo
    e restituisce True se il numero è primo, False altrimenti.
    """
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def trova_primi(numero: int) -> list:
    """
    Questa funzione prende come argomento un numero intero positivo
    e restituisce una lista dei numeri primi tra 2 e il numero.
    """
    primi = []
    for i in range(2, numero + 1):
        if is_prime(i):
            primi.append(i)
    return f"I numeri primi tra 2 e {numero} sono {primi}"

def trova_coprimi(primo_numero: int, secondo_numero: int) -> bool:
    """
    Questa funzione prende come argomenti due numeri interi positivi
    e restituisce True se i due numeri sono coprimi, False altrimenti.
    """
    coprimi = True
    for i in range(2, min(primo_numero, secondo_numero) + 1):
        if primo_numero % i == 0 and secondo_numero % i == 0:
            coprimi = False
            break
    return coprimi

def funzione_di_eulero(numero: int) -> int:
    """
    Questa funzione prende come argomento un numero intero positivo
    e restituisce il numero di coprimi presenti tra 1 e il numero.
    """
    numero_di_coprimi = 0
    for i in range(1, numero + 1):
        if trova_coprimi(i, numero):
            numero_di_coprimi += 1
    return numero_di_coprimi


























