#
# File: esercizio6.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/24
#
# Version: 1.0
#
# Description: risoluzione esercizio 6
#

# Risolvendo parte 2 esercizio 6

import rubrica

def main():
    
    rb = rubrica.Rubrica()

    print("Comandi disponibili: APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA")
    print("Scrivi EXIT per chiudere il programma. \n")
    
    # creo un ciclo infinito 
    while True:
        # rimuove gli spazi accidentali inseriti dall'utente e rende il testo maiuscolo
        comando = input("\nCosa vuoi fare? ").strip().upper()
        
        if comando == "EXIT":
            print("Chiusura del programma.")
            break

        elif comando == "APRI":
            file = input("Inserisci il nome del file (es. rubrica.json o rubrica.txt): ")
            rb.APRI(file)

        elif comando == "AGGIUNGI":
            print("Inserisci i dati del nuovo contatto:")
            nome = input("Nome e Cognome: ")

            giorno = int(input("Giorno di nascita (es. 9): "))
            mese = input("Mese (es. giugno): ")
            anno = int(input("Anno (es. 1934): "))
            età = int(input("Età: "))
            sesso = input("Sesso (M/F): ")
            mail = input("Mail: ")

            dettagli = {
                "giorno": giorno, "mese": mese, "anno": anno,
                "età": età, "sesso": sesso, "mail": mail
            }
            
            rb.AGGIUNGI(nome, dettagli)

        elif comando == "RIMUOVI":
            nome = input("Quale contatto vuoi rimuovere? ")
            rb.RIMUOVI(nome)

        elif comando == "SALVA":
            file = input("Come vuoi chiamare il file? (es. backup.json o backup.txt): ")
            rb.SALVA(file)

        elif comando == "STAMPA":
            nome = input("Di chi vuoi stampare le informazioni? ")
            rb.STAMPA(nome)

        else:
            print("Errore: Comando non riconosciuto. I comandi validi sono:")
            print("APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA, EXIT")

main()
