#
# File: esercizio8.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/28
#
# Version: 1.0
#
# Description: risoluzione esercizio 8
#

import json
import random

# Scrivo il programma con un approccio totalmente LBYL

def gioco_impiccato_lbyl():
    '''Esegue una partita al gioco dell'impiccato utilizzando la logica LBYL.'''
    print("--- IMPICCATO (versione LBYL) ---")

    with open("parole.json", "r") as f:                 # apro il file json
        parole = json.load(f)

    # prima di scegliere la parola, controllo che il file non sia vuoto (LBYL)
    if len(parole) == 0:
        print("Errore: la lista delle parole è vuota.")
        return

    parola_segreta = random.choice(parole).lower()      # selezione casuale della parola segreta
    lettere_provate = []
    tentativi_rimasti = 6

    while tentativi_rimasti > 0:
        # costruisco la stringa con i trattini
        parola_visualizzata = " "

        for lettera in parola_segreta:
            # controllo se la lettera è nella lista prima di mostrarla (LBYL)
            if lettera in lettere_provate:
                parola_visualizzata = parola_visualizzata + lettera + " "

            else:
                parola_visualizzata = parola_visualizzata + "_ "

        print(f'\nParola: {parola_visualizzata.strip()}. Tentativi: {tentativi_rimasti}.')

        # condizione di vittoria classica 
        if "_" not in parola_visualizzata:
            print(f'Hai vinto! La parola era: {parola_segreta}.')
            break

        tentativo = input("Inserisci una lettera o indovina la parola: ").strip().lower()

        # prima controllo se l'input è vuoto (LBYL) 
        if len(tentativo) == 0:
            print("Non hai inserito nulla!")
            continue

        # controllo se è un tentativo di indovinare tutta la parola (LBYL) 
        if len(tentativo) > 1:
            if tentativo == parola_segreta:
                print(f"Hai indovinato l'intera parola: {parola_segreta}!")
                break

            else: 
                print(f"Sbagliato! '{tentativo}' non è la parola segreta.")
                tentativi_rimasti = tentativi_rimasti - 1
                continue

        # controllo se è una lettera valida (alfabetica) (LBYL)
        if not tentativo.isalpha():
            print("Inserisci solo lettere dell'alfabeto.")
            continue

        # controllo se la lettere è già stata usata (LBYL)
        if tentativo in lettere_provate:
            print("Hai già provato questa lettera!")
            continue

        lettere_provate.append(tentativo)                  # aggiungo alla lista delle provate

        # controllo se la lettera è nella parola segreta
        if tentativo in parola_segreta:
            print("Lettera corretta!")

        else:
            print("Lettera errata!")
            tentativi_rimasti = tentativi_rimasti - 1

    else:
        print(f"\nGAME OVER! La parola era: '{parola_segreta}'.")


# Scrivo il programma con un approccio totalmente EAFP

def gioco_impiccato_eafp():
    '''Esegue una partita al gioco dell'impiccato utilizzando la logica EAFP.'''
    print("--- IMPICCATO (versione EAFP) ---")

    # provo ad aprire il file senza controllare se esista (EAFP)
    try:
        with open("parole.json", "r") as f:
            parole = json.load(f)
    except FileNotFoundError:
        print("Errore: il file 'parole.json' non esiste. Chiusura gioco.")
        return

    # provo a scegliere una parola; se la lista è vuota darà IndexError
    try:
        parola_segreta = random.choice(parole).lower()
    except IndexError:
        print("Errore: la lista delle parole nel JSON è vuota.")
        return

    lettere_provate = []
    tentativi_rimasti = 6

    while tentativi_rimasti > 0:
        parola_visualizzata = " "

        for lettera in parola_segreta:

            # provo a cercare la posizione della lettera nella lista usando .index() 
            # se la lettera non è in lista ho un ValueError (EAFP)
            try: 
                lettere_provate.index(lettera)
                parola_visualizzata = parola_visualizzata + lettera + " "
            except ValueError:
                parola_visualizzata = parola_visualizzata + "_ "

        print(f'\nParola: {parola_visualizzata.strip()}. Tentativi: {tentativi_rimasti}.')

        # per controllare se ho vinto uso .index() per ccercare un "_"
        try:
            parola_visualizzata.index("_")
        # se ottengo ValueError significa che non ci sono "_" e quindi ho vinto
        except ValueError:
            print(f'Hai vinto! La parola era: {parola_segreta}.')

        tentativo = input("Inserisci una lettera o indovina la parola: ").strip().lower()

        # per verificare se ho inseritio una parola intera provo ad accedere alla seconda lettera 
        # se ottengo IndexError è una lettera singola (EAFP)
        try:
            _ = tentativo[1]

            # se è una parola intera vengono lette le istruzioni che seguono
            try: 
                # assert verifica se una condizione è vera. Se è falsa ottengo un AssertionError
                assert tentativo == parola_segreta
                print(f"Hai indovinato l'intera parola: {parola_segreta}!")
                break
            except AssertionError:
                print(f"Sbagliato! '{tentativo}' non è la parola segreta.")
                tentativi_rimasti = tentativi_rimasti - 1
                continue
        
        # se ottengo IndexError ho inserito 1 o 0 lettere 
        except IndexError: 
            try:
                _ = tentativo[0]
            # se la parola è lunga 0 (input vuoto), si ha un IndexError
            except IndexError:
                print("Non hai inserito nulla!")
                continue

            # controllo se la lettera è già stata inserita (EAFP)
            try:
                lettere_provate.index(tentativo)
                print("Hai già provato questa lettera!")
                continue
            # se dà ValueError, la lettera è nuova
            except ValueError:
                lettere_provate.append(tentativo)

            # controllo se è una lettera valida (alfabetica) (EAFP)
            try: 
                assert tentativo.isalpha()
            except AssertionError:
                print("Inserisci solo lettere dell'alfabeto.")
                continue

            # controllo se la lettera è contenuta nella parola segreta (EAFP)
            try:
                parola_segreta.index(tentativo)
                print("Lettera corretta!")
            except ValueError:
                print("Lettera errata!")
                tentativi_rimasti = tentativi_rimasti - 1

    # le istruzioni seguenti vengono eseguite se il ciclo while finisce i tentativi 
    try:
        assert tentativi_rimasti > 0
    except AssertionError:
        print(f"\nGAME OVER! La parola era: '{parola_segreta}'.")

gioco_impiccato_eafp()
                

