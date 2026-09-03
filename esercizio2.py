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
    
    if 'day' in parola or 'water' in parola or 'about' in parola:       # usare 'in' invece di '==' permette di 
                                                                        # ignorare la punteggiatura attaccata
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
lista_righe.reverse()                               # il metodo reverse inverte l'ordine degli elementi della lista

print(lista_righe)

# Risolvendo parte 8 esercizio 2

lista_righe = testo.split('\n')                          # lista_righe contiene anche le righe vuote 

for i in range(len(lista_righe)):
    if i == 2 or i == 7 or i == 12 or i == 17:
        lista_righe[i] = lista_righe[i][::-1]            # utilizzo lo slicing con passo -1 per 
                                                         # capovolgere la riga direttamente come stringa

for riga in lista_righe:
    print(riga) 

# Risolvendo parte 9 esercizio 2

lista_strofe = testo.split('\n\n')                            # divido il testo in strofe ossia blocchi di testo 
                                                              # separati da una riga vuota

parole_comuni = set()                                         # creo un set che conterrà le parole comuni

for parola in lista_strofe[0].split():                        # estraggo le parole della prima strofa 
    parola_pulita = parola.lower().strip(".,;:!'")            # rendo ogni parola minuscola ed elimino 
                                                              # la punteggiatura con il metodo strip()
    parole_comuni.add(parola_pulita)

for i in range(1, len(lista_strofe)):                         # analizzo le strofe dalla seconda in poi
    
    parole_strofa_corrente = set()

    for parola in lista_strofe[i].split():
        parola_pulita = parola.lower().strip(".,;:!'")
        parole_strofa_corrente.add(parola_pulita)
    
    # uso operatore di intersezione per mantenere solo le parole presenti in entrambi i set
    parole_comuni = parole_comuni & parole_strofa_corrente    

print(f"Le parole presenti in tutte le strofe sono:  {parole_comuni}") 

# Risolvendo parte 10 esercizio 2

lista_parole = testo.split()
set_parole = set()                                      # creo un set in cui inserire le parole pulite 
                                                        # in modo che vengano eliminati i doppioni

for parola in lista_parole:
    parola_pulita = parola.lower().strip(".,;:!'")
    set_parole.add(parola_pulita)

# la consegna chiede una lista univoca quindi trasformo il set in lista
lista_unica = list(set_parole)                          

# uso il medoto sort con chiave di ordinamento len per ordinare le parole in base alla loro lunghezza
lista_unica.sort(key = len)                             
print(lista_unica)

# Risolvendo parte 11 esercizio 2

dizionario_caratteri = {}

for carattere in testo:                                    # il testo è una stringa che è un oggetto iterabile
    carattere_minuscolo = carattere.lower()
    
    # se il carattere è già presente nel dizionario incremento di 1 il valore corrispondete
    if carattere_minuscolo in dizionario_caratteri:       
        dizionario_caratteri[carattere_minuscolo] = dizionario_caratteri[carattere_minuscolo] + 1

    else:
        dizionario_caratteri[carattere_minuscolo] = 1

print(dizionario_caratteri)

# Risolvendo parte 12 esercizio 2

dizionario_alfanumerici = {}

for carattere in testo:
    if carattere.isalnum():

        carattere_minuscolo = carattere.lower()

        if carattere_minuscolo in dizionario_alfanumerici:
            dizionario_alfanumerici[carattere_minuscolo] = dizionario_alfanumerici[carattere_minuscolo] + 1

        else:
            dizionario_alfanumerici[carattere_minuscolo] = 1

print(dizionario_alfanumerici)