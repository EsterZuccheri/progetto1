#
# File: esercizio1.py
#
# Author: Ester Zuccheri
#
# Date: 2026/04/26
#
# Version: 1.0
#
# Description: risoluzione esercizio 1 
#

# Risolvendo parte 1 esercizio 1

def is_pari(n):
    """Ritorna vero se "n" è pari, se no ritorna falso"""
    
    risultato = False 

    if n % 2 == 0:         # se il risultato della divisione tra "n" e 2 è 0 
        risultato = True

    return risultato

# Risolvendo parte 2 esercizio 1 

def chiedi_intero():
    """Chiede all'utente un numero intero positivo e assicurarsi che lo sia"""

    numero_intero = 0        # inizializzo a 0 la variabile numero_intero per entrare subito nel ciclo

    while numero_intero <= 0:                            
        numero_intero = int( input('Dammi un numero intero positivo: '))  # casting a intero del numero dato dall'utente

        if numero_intero <= 0:
            print("Attenzione: devi inserire un numero intero positivo.")
        
    return numero_intero

# Risolvendo parte 3 esercizio 1 

def genera_lista(numero):
    """Genera lista a partire da un numero dato dall'utente seguendo regole specifiche"""

    lista_risultati =[numero]                            # inizializzo una lista contenete il numero di partenza dato dall'utente 

    while numero != 1 and len(lista_risultati) <= 100:   # inserisco elementi in lista finchè arrivo a 1 o la lista ha più di 100 numeri 
        
        if numero % 2 == 0:
            numero = numero // 2

        else:
            numero = numero * 3 + 1

        lista_risultati.append(numero)                   # aggiungo il nuovo numero alla lista

    return lista_risultati

# Risolvendo parte 4 esercizio 1 

def analizza_sequenza(lista):
    """Restituisce valore massimo, lunghezza e somma di tutti i numeri della lista generata nel punto 3"""

    # trovo il massimo
    massimo = lista[0]        # suppongo che il massimo sia il primo elemento della lista
    
    for numero in lista:
        if numero > massimo:
            massimo = numero 

    # trovo la somma
    somma = 0 
    
    for numero in lista:
        somma = somma + numero 
        
    #trovo la lunghezza
    lunghezza = len(lista)
        
    return massimo, lunghezza, somma

# Risolvendo parte 5 esercizio 1 

def ricerca(lista):
    """Scorre la lista e stampa solo i numeri divisibili per 5"""

    trovato = False                     # supponiamo inizialmente di non aver trovato nulla 

    for i in lista: 
        if i % 5 == 0:
            print(i)

            trovato = True
    
    if trovato == False:                # se la lista non contiene nessun multiplo di 5
        print("Non ci sono numeri divisibili per 5.")


######

# Parte 6

def main():
    quantità = int( input('Quanti numeri vuoi testare? '))     # chiedo quanti numeri testare 

    # variabili per tenere traccia del record assoluto
    lunghezza_massima = 0
    numero_vincente = 0

    for i in range(quantità):
        print(f"TEST NUMERO {i+1}")

        # Parte 2
        numero_scelto = chiedi_intero() 

        print(f"Hai scelto il numero: {numero_scelto}")

        # Parte 1                            
        result = is_pari(numero_scelto)

        print(result)

        # Parte 3
        sequenza = genera_lista(numero_scelto)

        print(sequenza)

        # Parte 4
        massimo, lunghezza, somma = analizza_sequenza(sequenza)

        print(f"Massimo: {massimo}, Lunghezza: {lunghezza}, Somma: {somma}")

        # Parte 5
        ricerca(sequenza)

        # aggiorno i record
        if lunghezza > lunghezza_massima:
            lunghezza_massima = lunghezza
            numero_vincente = numero_scelto

    # stampo il riepilogo
    print(f"Il numero che ha generato la sequenza più lunga è {numero_vincente} con {lunghezza_massima} numeri generati")

main()
