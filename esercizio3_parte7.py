#
# File: esercizio3_parte7.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/11
#
# Version: 1.0
#
# Description: risoluzione parte 7 esercizio 3
#

import argparse
import sys

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

parser = argparse.ArgumentParser(description = "Esegue il punto dell'esercizio 3 richiesto dall'utente")

# aggiungo un parametro per ogni punto dell'esercizio
parser.add_argument('--punto1', action='store_true', help="Esegue il punto 1 (stampa dizionario)")
parser.add_argument('--lista_ordinata', action='store_true', help="Esegue il punto 2 (età crescenti)")
parser.add_argument('--lista_inversa', action='store_true', help="Esegue il punto 3 (età decrescenti)")
parser.add_argument('--messaggio_auguri', action='store_true', help="Esegue il punto 4 (stampa messaggi auguri)")
# Non uso action='store_true' perché questa opzione ha bisogno di ricevere 
# un valore (la chiave da cercare). Con type=str salvo la parola digitata.
parser.add_argument('--visualizza_chiave', type=str, help="Esegue il punto 5 (stampa tutti i valori in rubrica corrispondenti alla chiave scelta)")

args = parser.parse_args()

if args.punto1 == True:
    
    for nome, dati in rubrica.items():                             # il metodo items applicato ad un dizionario ne estrae contemporaneamente la sua chiave e valore
                                                                   # alla variabile nome verrà associata la chiave esterna e a dati il dizionario interno
        frase_finale = f"'{nome}'"

    for chiave, valore in dati.items():                            # applico items al dizionario interno dati
        frase_finale = frase_finale + f", '{chiave}' {valore}"

    print(frase_finale)                                            # per ogni nome stampo la frase finale

if args.lista_ordinata == True:

    lista_coppie = list()

    for nome, dati in rubrica.items():
    
        età = dati['età']                        # estraggo dal dizionario dati il valore corrispondente alla chiave 'età'
        lista_coppie.append([età, nome])

    lista_coppie.sort()                          # ordino le età usando direttamente il metodo sort perchè considera automaticamente solo il primo elemento di ogni coppia (l'età)

    for [età, nome] in lista_coppie:

        print(f"{nome} ha {età} anni")

if args.lista_inversa == True:
    
    lista_coppie = list()

    for nome, dati in rubrica.items():
    
        età = dati['età']                        
        lista_coppie.append([età, nome])

    lista_coppie.sort()    
    lista_coppie.reverse()                       

    for [età, nome] in lista_coppie:

        print(f"{nome} ha {età} anni")

if args.messaggio_auguri == True:

    for nome, dati in rubrica.items():

        if dati['sesso'] == 'M':
            print(f"Caro {nome}, \nsei nato il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. \nTi manderemo gli auguri a {dati['mail']}")

        else:
            print(f"Cara {nome}, \nsei nata il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. \nTi manderemo gli auguri a {dati['mail']}")
    
if args.visualizza_chiave != None:

    if len(args.visualizza_chiave) > 1:                       # verifico che l'utente abbia scritto un argomento controllando se la lista argv contiene più di 1 elemento (un elemento è sempre il nome del file)
    
        chiave_scelta = args.visualizza_chiave     
        print (f"'Hai scelto di cercare: {chiave_scelta}")

        for nome, dati in rubrica.items():
        
            valore = dati[chiave_scelta]
            print(f"{nome}: {valore}")

    else:
        print("Errore: Non hai inserito nessuna chiave! Avvia il programma scrivendo ad esempio: python file.py età")


