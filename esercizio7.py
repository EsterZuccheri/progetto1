#
# File: esercizio7.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/27
#
# Version: 1.0
#
# Description: risoluzione esercizio 7
#


def tabellina(n):
    '''Generatore che dato un numero 'n', genera la corrispondente tabellina all'infinito.'''
    k = 0

    while True: 
        # moltiplico il numero scelto per il contatore k
        yield n * k
        k = k + 1

def main ():
    print("=== IL GIOCO DELLE TABELLINE ===")
    
    numero_scelto = int(input('Quale tabellina vuoi allenare? '))
    g = tabellina(numero_scelto)                                    # creo il generatore passandogli il numero scelto
    k = 0

    risposta_corretta = next(g)                                     # estraggo il primo risultato corretto (0 x numero)
    print("\nIniziamo! (Scrivi 'esci' in qualsiasi momento per chiudere il gioco)")

    # loop interattivo in cui chiedo all'utente di indovinare
    while True:
        # .strip ripulisce gli spazzi accidentali
        risposta_utente = input(f'Quanto fa {k} x {numero_scelto}? ').strip().lower()

        # gestione della chiusura gioco 
        if risposta_utente == "esci":
            print("Gioco terminato.")
            break                           # break interrompe istantaneamente il ciclo 'while' facendo terminare il gioco

        # gestione degli errori (lettere, decimali, simboli speciali)
        # 'try' prova a eseguire codice a rischio. 
        # Se fallisce, 'except' cattura l'errore (ValueError) evitando il crash
        try:
            # provo a trasformare la risposta in un numero intero
            valore_inserito = int(risposta_utente)

            # passo all'istruzione successiva se l'utente ha inserito un numero intero valido 
            if valore_inserito == risposta_corretta:
                print("Risposta esatta!\n")

                k = k + 1
                risposta_corretta = next(g)           # il generatore calcola il valore successivo

            else:
                print("Sbagliato! Ritenta: ")

        except ValueError:
            print("Attenzione: devi inserire solo numeri interi! Niente lettere o virgole.\n")

main()