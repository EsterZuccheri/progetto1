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

######

def main():
    numero = int( input('Dammi un numero: ') )  # casting a intero del numero dato dall'utente

    print(type(numero))                             

    result = is_pari(numero)

    print(result)

main()


# Risolvendo parte 2 esercizio 1 

def chiedi_intero():
    """Chiede all'utente un numero intero positivo e assicurarsi che lo sia"""

    numero_intero = 0        # inizializzo a 0 la variabile numero_intero per entrare subito nel ciclo

    while numero_intero <= 0:                            
        numero_intero = int( input('Dammi un numero intero positivo: '))

        if numero_intero <= 0:
            print("Attenzione: devi inserire un numero intero positivo.")
        
    return numero_intero

######

def main():
    numero_scelto = chiedi_intero() 

    print(f"Hai scelto il numero: {numero_scelto}")

main()


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

#####

def main():
    numero_scelto = chiedi_intero() 
    
    sequenza = genera_lista(numero_scelto)

    print(sequenza)

main()


# Risolvendo parte 4 esercizio 1 

def analizza_sequenza(lista):
    """Restituisce valore massimo, lunghezza e somma di tutti i numeri della lista generata nel punto 3"""

    






# Risolvendo parte 5 esercizio 1 (in classe, è collegato a punto 3 e 4)

def ricerca(lista):
    for i in lista: 
        if i % 5 == 0:
            print(i)
    
        else: 
            print("Non ci sono numeri divisibili per 5.")
