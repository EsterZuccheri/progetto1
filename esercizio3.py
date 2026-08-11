#
# File: esercizio3.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/10
#
# Version: 1.0
#
# Description: risoluzione esercizio 3
#

import sys
import argparse

# NOTA: Prima di eseguire il programma esercizio3.py, commentare 
# una tra la parte 5 e la parte 6, perché non è possibile far leggere 
# gli argomenti contemporaneamente con argv e argparse senza creare conflitti.

# Risolvendo parte 1 esercizio 3

# parto dal dizionario annidato rubrica
rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

for nome, dati in rubrica.items():           # il metodo items applicato ad un dizionario ne estrae contemporaneamente la sua chiave e valore
                                             # alla variabile nome verrà associata la chiave esterna e a dati il dizionario interno
    frase_finale = f"'{nome}'"

    for chiave, valore in dati.items():      # applico items al dizionario interno dati
        frase_finale = frase_finale + f", '{chiave}' {valore}"

    print(frase_finale)                      # per ogni nome stampo la frase finale

# Risolvendo parte 2 esercizio 3

lista_coppie = list()

for nome, dati in rubrica.items():
    
    età = dati['età']                        # estraggo dal dizionario dati il valore corrispondente alla chiave 'età'
    lista_coppie.append([età, nome])

lista_coppie.sort()                          # ordino le età usando direttamente il metodo sort perchè considera automaticamente solo il primo elemento di ogni coppia (l'età)

for [età, nome] in lista_coppie:

    print(f"{nome} ha {età} anni")

# Risolvendo parte 3 esercizio 3

lista_coppie.reverse()                       # inverto l'ordine della lista creata nel punto 2

for [età, nome] in lista_coppie:

    print(f"{nome} ha {età} anni")

# Risolvendo parte 4 esercizio 3

for nome, dati in rubrica.items():

    if dati['sesso'] == 'M':
        print(f"Caro {nome}, \nsei nato il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. \nTi manderemo gli auguri a {dati['mail']}")

    else:
        print(f"Cara {nome}, \nsei nata il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. \nTi manderemo gli auguri a {dati['mail']}")
    
# Risolvendo parte 5 esercizio 3

if len(sys.argv) > 1:                       # verifico che l'utente abbia scritto un argomento controllando se la lista argv contiene più di 1 elemento (un elemento è sempre il nome del file)
    
    chiave_scelta = sys.argv[1]     
    print (f"'Hai scelto di cercare: {chiave_scelta}")

    for nome, dati in rubrica.items():
        
        valore = dati[chiave_scelta]
        print(f"{nome}: {valore}")

else:
    print("Errore: Non hai inserito nessuna chiave! Avvia il programma scrivendo ad esempio: python file.py età")

# Risolvendo parte 6 esercizio 3

parser = argparse.ArgumentParser(description = "Stampa gli auguri per una persona tra quelle in rubrica")

parser.add_argument('--nome', help = "Nome e cognome della persona scelta")    # aggiungo i parametri attesi dal programma con il metodo add_argument

args = parser.parse_args()                                                     # uso il metodo parse_args per leggere i dati inseriti dall'utente e salvati nella variabile "args"      

nome_cercato = args.nome                                                       # estrae il nome inserito dall'utente nel terminale (dopo '--nome') e lo salva in una variabile

if nome_cercato != None:

    if nome_cercato in rubrica:
        
        dati = rubrica[nome_cercato]                                           # estraggo i dati della persona scelta
        
        if dati['sesso'] == 'M':
            print(f"Caro {nome_cercato}, \nsei nato il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. \nTi manderemo gli auguri a {dati['mail']}")

        else:
            print(f"Cara {nome_cercato}, \nsei nata il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. \nTi manderemo gli auguri a {dati['mail']}")
    
    else:
        print(f"Errore: {nome_cercato} non è in rubrica.")