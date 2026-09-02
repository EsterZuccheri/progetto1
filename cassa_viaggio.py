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

import json

class CassaViaggio:
    '''Classe che gestisce il budget e le spese di un viaggio'''

    # imposto il budget iniziale e creo una lista vuota per le spese
    def __init__(self, budget_iniziale):
        self.budget = float(budget_iniziale)
        self.spese = []

    @classmethod

    # classmethod: carica da JSON
    def da_json(cls, nome_file):
        '''Crea una CassaViaggio leggendo i dati da un file JSON'''

        with open(nome_file, "r") as f:
            dati = json.load(f)

        # dati["budget"] estrae il numero, cls(...) crea la nuova cassa
        nuova_cassa = cls(dati["budget"])
        # copio la lista delle spese dal file JSON alla nuova cassa
        nuova_cassa.spese = dati["spese"]

        return nuova_cassa

    # METODI
    def AGGIUNGI_SPESA(self, descrizione, costo):
        '''Aggiunge una nuova spesa (come dizionario) alla lista delle spese'''

        # creo un dizionario per la singola spesa e lo aggiungo alla lista 
        spesa = {
            "descrizione": descrizione,
            "costo": float(costo)
        }
        self.spese.append(spesa)
        print(f"Spesa '{descrizione}' di {costo}€ aggiunta con successo.")

    def RIEPILOGO(self):
        '''Stampa l'elenco delle spese, calcola il totale e mostra il budget residuo'''

        # se non ci sono spese, il totale è 0
        totale_speso = 0.0

        print("\n--- DETTAGLIO SPESE ---")
        # scorro la lista delle spese per stamparle e sommarle
        for spesa in self.spese:
            print(f"- {spesa['descrizione']}: {spesa['costo']}€")
            totale_speso = totale_speso + spesa['costo']

        rimanente = self.budget - totale_speso

        print("-" * 23)
        print(f"BUDGET INIZIALE: {self.budget}€")
        print(f"TOTALE SPESO: {totale_speso}€")
        print(f"BUDGET RIMANENTE: {rimanente}€\n")

    def SALVA(self, nome_file):
        '''Salva il budget e la cronologia delle spese in un file JSON'''

        # preparo un unico dizionario che contiene tutto
        dati_da_salvare = {
            "budget": self.budget,
            "spese": self.spese
        }
        with open(nome_file, "w") as f:
            json.dump(dati_da_salvare, f, indent = 4, ensure_ascii = False)
        print(f"Dati salvati con successo in {nome_file}.")

