#
# File: cassa_viaggio.py
#
# Author: Ester Zuccheri
#
# Date: 2026/09/02
#
# Version: 1.0
#
# Description: programma per monitorare le spese e gestire il budget durante un viaggio 
#

from cassa_viaggio import CassaViaggio

def main():
    print("🌍 === BENVENUTO NEL TRAVEL BUDGET MANAGER === 🌍\n")

    # fase di inizializzazione
    scelta = input("Vuoi caricare un viaggio salvato (C) o iniziarne uno nuovo (N)? ").strip().upper()

    if scelta == 'C':
        nome_file = input("Inserisci il nome del file (es. viaggio.json): ")

        try: 
            # uso il classmethod per costruire la cassa partendo dal file 
            mia_cassa = CassaViaggio.da_json(nome_file)
            print("Viaggio caricato con successo!\n")
        except FileNotFoundError:
            print("Errore: file non trovato. Verrà creato un nuovo viaggio.\n")
            scelta = 'N'    # forzo la creazione di un nuovo viaggio

    if scelta != 'C':
        # EAFP: Continuo a chiedere il budget finché non inserisce un numero valido
        while True:
            try:
                budget = input("Qual è il tuo budget totale per questo viaggio? (€): ")
                # provo a trasformare il testo in numero decimale (float)
                budget_float = float(budget)
                break        # se ha successo rompo il ciclo e vado avanti
            except ValueError:
                print("Errore: Inserisci solo numeri. Niente lettere!\n")

        # creo la nuova cassa
        mia_cassa = CassaViaggio(budget_float)
        print("Nuovo viaggio inizializzato!\n")

    print("Comandi disponibili: AGGIUNGI, RIEPILOGO, SALVA, ESCI")

    while True:
        comando = input("\nCosa vuoi fare? ").strip().upper()

        if comando == "ESCI":
            print("Chiusura del programma. Buon viaggio!")
            break
            
        elif comando == "AGGIUNGI":
            descrizione = input("Cosa hai comprato? ")
            
            # EAFP: Continuo a chiedere il costo finché non è un numero valido
            while True:
                try:
                    costo_str = input("Quanto è costato? (€): ")
                    costo_float = float(costo_str)
                    break
                except ValueError:
                    print("Errore: Inserisci un costo numerico valido (usa il punto per i decimali, es. 15.50).\n")
            
            # Chiamo il metodo della classe passandogli i dati corretti
            mia_cassa.AGGIUNGI_SPESA(descrizione, costo_float)
            
        elif comando == "RIEPILOGO":
            mia_cassa.RIEPILOGO()
            
        elif comando == "SALVA":
            nome_file = input("Come vuoi chiamare il file di salvataggio? (es. viaggio.json): ")
            mia_cassa.SALVA(nome_file)
            
        else:
            print("Comando non riconosciuto. Scrivi AGGIUNGI, RIEPILOGO, SALVA o ESCI.")

main()