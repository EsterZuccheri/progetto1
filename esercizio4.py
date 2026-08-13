#
# File: esercizio4.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/13
#
# Version: 1.0
#
# Description: risoluzione esercizio 4
#

import argparse
import sys
import json

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

# aggiungo un parametro per risolvere parte 1 esercizio 4
parser.add_argument('--crea_file', action='store_true', help="Genera il file rubrica.txt con tutti i contatti")
# aggiungo un parametro per risolvere parte 2 esercizio 4
parser.add_argument('--scrivi_json', action='store_true', help="Crea il file rubrica.json partendo dal dizionario")
# aggiungo un parametro per risolvere parte 3 esercizio 4
parser.add_argument('--leggi_json', action='store_true', help="Legge il file rubrica.json e ne stampa il contenuto")

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

# Risolvendo parte 1 esercizio 4

if args.crea_file == True:

    with open("rubrica.txt", "w") as file:                   # apro il file rubrica.txt in modalità scrittura usando context manager

        for nome, dati in rubrica.items():
            riga = f"{nome}, {dati['giorno']}, {dati['mese']}, {dati['anno']}, {dati['età']}, {dati['sesso']}, {dati['mail']}\n"
            file.write(riga)

    print("File rubrica.txt generato con successo.")

# Risolvendo parte 2 esercizio 4

if args.scrivi_json == True:

    with open("rubrica.json", "w", encoding="utf-8") as file:                  # apro il file in modalità scrittura
                                                                               # encoding="utf-8" assicura che il file JSON sappia gestire caratteri speciali (come à)
        json.dump(rubrica, file, indent=4, ensure_ascii=False)                 # scrivo contenuto del dizionario rubrica in file
                                                                               # indent= 4 per mettere 4 spazi e andare a capo per ogni elemento
                                                                               # ensure_ascii=False per dire a Python di non trasformare la à nel codice \u00e0

# le aggiunte permettono di evitare che Python converta le lettere speiali come à in ASCII quando crea un JSON file

    print("File rubrica.json creato con successo.")

# Risolvendo parte 3 esercizio 4

if args.leggi_json == True:
    
    with open("rubrica.json", "r") as file:              # apro il file in modalità lettura
        rubrica_letta = json.load(file)                  # il file JSON è letto in un dizionario Python   

    print("CONTENUTO DEL FILE JSON: \n")

    for nome, dati in rubrica_letta.items():
        print(f"{nome}: {dati}")
