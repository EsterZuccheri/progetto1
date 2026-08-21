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
    '''Genera la lista con le 4 rotazioni 