#
# File: esercizio5.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/18
#
# Version: 1.0
#
# Description: risoluzione punti 1, 2, 3, 4 esercizio 5
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
        # if incrocia_colonne(soluzione_posizioni, col) == True:
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False 

    # Se non è ritornato prima, 
    # allora nessun incrocio trovato: posizioni della soluzione valide 
    return True 

# Risolvendo parte 1, 2, 3, 4 esercizio 5
# per risolvere parte 2 aggiungo contatore 'tentativi'
# per risolvere parte 3 aggiungo secondo if e sfrutto il dizionario conteggio_soluzioni
# per risolvere parte 4 aggiungo condizione di else

import random
import time 

def main():

    random_generator = random.Random()         # inizializzo generatore permutazioni

    scacchiera = list(range(8))                # preparo la "possibile soluzione" con posizoni da testare
               
    solutions = 0                              # conto le soluzioni trovate, inizio da 0                
    
    start_time = time.time()                   # misuro il tempo di partenza per la ricerca della soluzione
    
    tempo_totale_iniziale = time.time()        # creo un contatore che non viene azzerato
    
    tentativi = 0                              # creo contatore che tenga traccia del numero di tentativi 
                                               # necessari per trovare soluzione valida

    conteggio_soluzioni = {}                   # creo un dizionario vuoto per contare soluzioni ripetute

    # loop finchè non trovo una soluzione; 
    # per risolvere il punto 1 ho bisogno di trovare 10 soluzioni quindi il loop continua fino a quando trovo 10 soluzioni
    while solutions < 10:             
    
        # permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera) 
        
        # mescolando la scacchiera ho fatto un primo tentativo 
        tentativi = tentativi + 1 
        
        # verifica se la permutazione casuale è soluzione 
        # if soluzione_ok(scacchiera) == True: 
        if soluzione_ok(scacchiera): 

            scacchiera_tupla = tuple(scacchiera)       # trasformo scacchiera in una tupla perchè le liste non possono 
                                                       # essere usate come chiavi di un dizionario

            if scacchiera_tupla not in conteggio_soluzioni:           
            
                print(f'Found solution {scacchiera_tupla} in {time.time() - start_time} s. (Tentativi: {tentativi})')
            
                solutions = solutions + 1                    # incremento contatore soluzioni trovate (condizione stop loop)
                
                conteggio_soluzioni[scacchiera_tupla] = 1    # aggiungo la soluzione al dizionario partendo da 1
        
                start_time = time.time()                     # reset timer ricerca soluzione

                tentativi = 0                                # reset contatore tentativi per preparare ricerca prossima soluzione
            
            else:
                conteggio_soluzioni[scacchiera_tupla] = conteggio_soluzioni[scacchiera_tupla] + 1

    #calcolo il tempo totale impiegato per trovare le 10 soluzioni
    tempo_totale = time.time() - tempo_totale_iniziale
    
    #calcolo la media tra i tempi
    print(f'Il tempo medio per trovare una soluzione è: {tempo_totale/10} s.')
    
    print(f'Le soluzioni sono ripetute: {conteggio_soluzioni}')

# chiamo la funzione principale 
main()
