#
# File: rubrica.py
#
# Author: Ester Zuccheri
#
# Date: 2026/08/24
#
# Version: 1.0
#
# Description: risoluzione esercizio 6: creazione classe rubrica
#

# Risolvendo parte 1 esercizio 6

import json

class Rubrica: 
    '''Classe che rappresenta una Rubrica di contatti.
    Permette di gestire un dizionario di persone eseguendo operazioni di 
    lettura e scrittura su file JSON e modifiche in memoria.'''
    
    def __init__(self, dizionario_iniziale=None): 
        '''Inizializza il dizionario interno vuoto.'''

        self.data = dizionario_iniziale

    # --- CLASSMETHOD 1: Inizializza da JSON ---
    @classmethod 
    def da_json(cls, nome_file):
        with open(nome_file, "r") as file_in:
            dizionario = json.load(file_in)
        # cls(dizionario) crea e restituisce una nuova Rubrica piena
        return cls(dizionario)

    # --- CLASSMETHOD 2: Inizializza da file di Testo ---
    @classmethod 
    def da_testo(cls, nome_file):
        dizionario = {}
        
        with open(nome_file, "r") as file_in:
            for riga in file_in:
                elementi = riga.strip().split(", ")        # separo la riga usando la virgola
                
                # Mi assicuro di avere almeno 7 fette di dati (elementi). Se la riga è vuota
                # o scritta male, la salto per non cercare indici che non esistono.
                if len(elementi) >= 7:
                    nome = elementi [0]
                    
                    # ricostruisco il dizionario interno della persona
                    dizionario[nome] = {
                        "giorno": int(elementi[1]),
                        "mese": elementi[2],
                        "anno": int(elementi[3]),
                        "età": int(elementi[4]),
                        "sesso": elementi[5],
                        "mail": elementi[6]
                    }
        return cls(dizionario)

    # definisco i 5 metodi di azione della rubrica

    def APRI(self, nome_file):
        '''Apre una rubrica leggendola da un file (JSON oppure testo).'''

        if nome_file.endswith(".json"):
            with open(nome_file, "r") as f:       
                self.data = json.load(f)
        
        elif nome_file.endswith(".txt"):
            self.data = 

        
        print(f'Rubrica caricata con successo da {nome_del_file}')

    def AGGIUNGI(self, nome, dettagli):
        '''Aggiunge un elemento alla rubrica. 
        Aggiunge una nuova voce al dizionario interno (self.data)
        'dettagli' è un dizionario contenente età, sesso, mail ...'''

        self.data[nome] = dettagli 
        print(f'Contatto '{nome}' aggiunto con successo.')

    def RIMUOVI(self, nome):
        '''Rimuove un elemento dalla rubrica dato il nome.'''

        # prima di rimuovere, verifico che il nome esista per evitare errori 
        if nome in self.data:
            del self.data[nome]
            print(f'Contatto '{nome}' rimosso dalla rubrica.')

        else:
            print(f'Errore: il contatto '{nome}' non esiste.')

    def SALVA(self,nome): 
        '''Salva la rubrica su un file (JSON o testo)'''

        with open(nome_del_file, "w", encoding="utf-8") as file_out:          # apro il file in modalità scrittura
                                                                                # encoding="utf-8" assicura che il file JSON sappia gestire caratteri speciali
            json.dump(self.data, file_out, indent=4, ensure_ascii=False)        # scrivo contenuto del dizionario self.data in file_out                 
                                                                                # indent= 4 per mettere 4 spazi e andare a capo per ogni elemento
                                                                                # ensure_ascii=False per dire a Python di non trasformare caratteri speciali in codice ascii
        print(f'Rubrica salvata con successo in {nome_del_file}.')
    
    def STAMPA(self, nome):
        '''Stampa tutte le informazioni di un contatto (dato il nome)'''

        if nome in self.data:
            print(f'\nInformazioni di {nome}: ')

            # self.data[nome] è il dizionario interno di quella persona
            for chiave, valore in self.data[nome].items():
                print(f'{chiave}: {valore}')
        
        else:
            print(f'Il contatto '{nome}' non è presente in rubrica.')