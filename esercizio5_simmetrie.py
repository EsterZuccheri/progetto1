#
# File: esercizio5_simmetrie.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/20
#
# Version: 1.0
#
# Description: risoluzione punto 7 esercizio 5
#


#
# File: Otto_regine.py
#
# Author: E.Romelli, D.Tavagnacco
#
# Date: 2026/04/14
#
# Version: 1.0
#
# Description: Example program to solve 8 queen-like problem 
#              using brute force + random approach
#


def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale" '''

    # distanza lungo y
    dy = abs(y1 - y0)
    
    # distanza lungo x
    dx = abs(x1 - x0) 

    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy     


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):     
        # la coordinata X (la riga) è indice (c) 
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True  
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne        
    return False   


def soluzione_ok(soluzione_posizioni):
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni 
       (colonne dela permatazione) ogni colonna incrocia la diagonale
       di qualche altra posizione
    '''

    for col in range(1, len(soluzione_posizioni)):
        # verifica se incrocia
        #if incrocia_colonne(soluzione_posizioni, col) == True:
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False 

    # Se non è ritornato prima, 
    # allora nessun incrocio trovato: posizioni della soluzione valide 
    return True 

# Risolvendo parte 7 esercizio 5

def ruota_90(soluzione):
    '''Prende una soluzione (lista) e la ruota di 90 gradi in senso orario'''
    N = len(soluzione)
    ruotata = [0] * N                # creo lista lunga N contenete solo zeri

    for r in range(N):
        # la nuova riga è 'c'; la nuova colonna è 'N - 1 - r'
        c = soluzione[r]
        ruotata[c] = (N - 1) - r 

    return ruotata

def genera_famiglia_simmetrica(soluzione):
    '''Genera la lista con le 4 rotazioni (0°, 90°, 180°, 270°)'''
    r_90 = ruota_90(soluzione)
    r_180 = ruota_90(r_90)
    r_270 = ruota_90(r_180)

    # ritorno le 4 soluzioni sotto forma di tuple 
    # uso le tuple perchè nei st posso inserire solo oggetti immutabili (come le tuple)
    return [tuple(soluzione), tuple(r_90), tuple(r_180), tuple(r_270)]

import random
import time

def main():
    random_generator = random.Random()
    scacchiera = list(range(8))

    tutte_le_viste = set()               # creo set in cui salvare sia le configurazioni originali che le loro rotazioni
    famiglie_uniche_trovate = []         # lista dove salvo le 5 famiglie trovate 

    start_time = time.time()
    tentativi = 0

    # cerco esattamente 5 famiglie uniche
    while len(famiglie_uniche_trovate) < 5:

        random_generator.shuffle(scacchiera)
        tentativi = tentativi + 1 

        # controllo se la soluzione è valida 
        if soluzione_ok(scacchiera):

            scacchiera_tupla = tuple(scacchiera)

            # controllo che la soluzione sia nuova e non sia la rotazione di un'altra
            if scacchiera_tupla not in tutte_le_viste:
                
                famiglia = genera_famiglia_simmetrica(scacchiera)     # genero le sue 4 rotazioni
                famiglie_uniche_trovate.append(famiglia)              # salvo la famiglia nella lista

                # aggiungo tutte e 4 le rotazioni al set "tutte_le_visite"
                for variante in famiglia:
                    tutte_le_viste.add(variante)

                print(f'Trovata famiglia {len(famiglie_uniche_trovate)} in {tentativi} tentativi.')
                tentativi = 0        # reset contatore tentativi per la prossima ricerca

    print(f'\nTempo totale: {time.time() - start_time} s.')
    print(f'\nEcco le 5 soluzioni uniche con le loro rotazioni: ')

    # uso enumerate() per avere automaticamente un contatore (indice) mentre scorro la lista
    for indice, famiglia in enumerate(famiglie_uniche_trovate):
        print(f'\nFAMIGLIA {indice + 1}: ')
        print(f' Originale (0°): {famiglia[0]}')
        print(f' Ruotata di 90°: {famiglia[1]}')
        print(f' Ruotata di 180°: {famiglia[2]}')
        print(f' Ruotata di 270°: {famiglia[3]}')

main()

