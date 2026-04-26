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

    if n%2 == 0:
        risultato = True

    return risultato

######

def main():
    numero = int( input('Dammi un numero: ') )

    print(type(numero))

    result = is_pari(numero)

    print(result)

main()


#Risolvendo parte 2 esercizio 1 (DA SOLA)

def chiedi_intero():
    """Chiede all'utente un numero intero positivo e assicurarsi che lo sia"""

    while numero_intero <= 0:
        numero_intero = int( input('Dammi un numero intero: '))

        # aggiuntivo, non necessario, da decidere se lasciare
        if numero_intero <= 0:
            print("Attenzione: devi inserire un numero intero positivo.")
        
    return numero_intero

######

def main():
    numero_scelto = chiedi_intero()

    # valuta se continuare con quello che dice gemini ! verificare se lo abbiuamo fatto 
