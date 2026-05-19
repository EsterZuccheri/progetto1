#
# File: esercizio1.py
#
# Author: Ester Zuccheri
#
# Date: 2026/05/19
#
# Version: 1.0
#
# Description: risoluzione esercizio 8
#

import random 

def gioco_impiccato():
    '''Documentazione su cosa fa la funzione'''
    # Lista di parole possibili per il gioco
    parole = ["python", "programmazione", "computer", "sviluppatore", "algoritmo", "funzione"]
    
    # Selezione casuale della parola segreta
    parola_segreta = random.choice(parole).lower()
    
    # Inizializzazione delle lettere indovinate e dei tentativi
    lettere_indovinate = set()
    tentativi_rimasti = 6
    lettere_sbagliate = set()

    print("--- BENVENUTO AL GIOCO DELL'IMPICCATO! ---")
    
    while tentativi_rimasti > 0:
        # Mostra lo stato attuale della parola (es. p _ t h o n)
        parola_visualizzata = ""
        for lettera in parola_segreta:
            if lettera in lettere_indovinate:
                parola_visualizzata += lettera + " "
            else:
                parola_visualizzata += "_ "
        
        print(f"\nParola da indovinare: {parola_visualizzata.strip()}")
        print(f"Tentativi rimasti: {tentativi_rimasti}")
        if lettere_sbagliate:
            print(f"Lettere errate provate: {', '.join(sorted(lettere_sbagliate))}")

        # Controllo vittoria: se non ci sono più trattini, l'utente ha vinto
        if "_" not in parola_visualizzata:
            print(f"\nComplimenti! Hai indovinato la parola: '{parola_segreta}' 🎉")
            break

        # Input dell'utente con validazione speculare
        tentativo = input("Inserisci una lettera: ").lower().strip()

        # Validazione dell'input
        if len(tentativo) != 1 or not tentativo.isalpha():
            print("Per favore, inserisci una sola lettera valida.")
            continue
        
        if tentativo in lettere_indovinate or tentativo in lettere_sbagliate:
            print("Hai già provato questa lettera. Scegline un'altra.")
            continue

        # Verifica se la lettera è nella parola
        if tentativo in parola_segreta:
            print(f"Ottimo! La lettera '{tentativo}' è presente.")
            lettere_indovinate.add(tentativo)
        else:
            print(f"Peccato! La lettera '{tentativo}' non è presente.")
            lettere_sbagliate.add(tentativo)
            tentativi_rimasti -= 1

    else:
        # Questo blocco 'else' viene eseguito solo se il ciclo while termina naturalmente (tentativi finiti)
        print(f"\nHai esaurito i tentativi! Game Over. La parola era: '{parola_segreta}' 💀")


gioco_impiccato()


# al posto di if ... in, se devo usare try posso vedere se la lettera è contenuta nella lista usano .index() 
# come per esempio qui:
try:
    indice = lettere_indovinate.index(tentativo)
except ValueError:
    pass
else:
    print(f"Hai già provato la lettera '{tentativo}'")
    continue