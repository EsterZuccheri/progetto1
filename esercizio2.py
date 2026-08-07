#
# File: esercizio2.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/07
#
# Version: 1.0
#
# Description: risoluzione esercizio 2
#

testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

# Risolvendo parte 1 esercizio 2

# Divido il testo in base al carattere \n

lista_righe = testo.split('\n')

contatore = 0
for riga in lista_righe:
    if len(riga) > 0:
        contatore = contatore + 1 

print(contatore)

# Risolvendo parte 2 esercizio 2

# Divido il testo in base al carattere ()

lista_parole = testo.split()

contatore_parole = 0
for parola in lista_parole:
    if len(parola) > 0:
        contatore_parole = contatore_parole + 1

print(contatore_parole)

# Risolvendo parte 3 esercizio 2

# Utilizzo il metodo isalnum() per verificare se un carattere appartiene agli alfanumerici

lista_caratteri = list(testo) 

contatore_alfanumerici = 0
for carattere in lista_caratteri:
    if carattere.isalnum() == True:
        contatore_alfanumerici = contatore_alfanumerici + 1

print(contatore_alfanumerici)

# Risolvendo parte 4 esercizio 2

lettera = str( input('Inserisci una lettera: ') )

contatore_lettera = 0
for carattere in lista_caratteri:
    if carattere.lower() == lettera.lower():             # converto i caratteri e la lettera scelta in minuscolo
        contatore_lettera = contatore_lettera + 1

print(contatore_lettera)

# Risolvendo parte 5 esercizio 2

for i in range(len(lista_parole)):

    parola = lista_parole[i].lower()                                    # converto in minuscolo l'elemento corrente 
    
    if 'day' in parola or 'water' in parola or 'about' in parola:       # usare 'in' invece di '==' permette di ignorare la punteggiatura attaccata
        lista_parole[i] = 'PYTHON'

print(lista_parole)

# Risolvendo parte 6 esercizio 2

lista_parole = testo.split()                             # creo nuovamente la lista parole a partire dal testo originale

for i in range(len(lista_parole)):
    if i % 2 == 0:                                       # le parole di indice pari sono quelle in posizione dispari
        lista_parole[i] = lista_parole[i].upper()

print(lista_parole)

# Risolvendo parte 7 esercizio 2

lista_righe = testo.split('\n')
lista_righe.reverse()

print(lista_righe)

# Risolvendo parte 8 esercizio 2

lista_righe = testo.split('\n')                          # lista_righe contiene anche le righe vuote 

for i in range(len(lista_righe)):
    if i == 2 or i == 7 or i == 12 or i == 17:
        lista_righe[i] = lista_righe[i][::-1]            # utilizzo lo slicing con passo -1 per capovolgere la riga direttamente come stringa

for riga in lista_righe:
    print(riga) 

# Risolvendo parte 9 esercizio 2