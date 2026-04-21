import json

class Rubrica: 
    pass
    
    def __init__(self):
        self.data = {}
        
    def APRI(self, nome_del_file):
        with opern(nome_del_file) as dile_in:
            self.data = json.load(file_in)