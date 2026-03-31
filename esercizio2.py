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

#Risolvendo parte 1 esercizio 2

#Divido il testo in base al carattere \n

lista_righe = testo.split('\n')

contatore = 0
for riga in lista_righe:
    if len(riga) > 0:
        contatore = contatore + 1 

print(contatore)

#Risolvendo parte 2 esercizio 2

#Divido il testo in base al carattere ()

lista_parole = testo.split()

contatore_parole = 0
for parola in lista_parole:
    if len(parola) > 0:
        contatore_parole = contatore_parole + 1

print(contatore_parole)

#Risolvendo parte 3 esercizio 2

alfanumerici = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
lista_lettere = list(testo)

contatore_lettere = 0 
for lettera in lista_lettere:
    if lettera in alfanumerici:
        contatore_parole = contatore_parole + 1

print(contatore_parole)

#Risolvendo parte 8 esercizio 2

for indice in [2,]:
    lista_lettere_riga = list(lista_righe[1])
    print(lista_lettere_riga)
