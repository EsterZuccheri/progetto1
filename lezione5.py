import sys 

#argv prende tutto quello che c'è scritto dopo python nel terminale e lo inserisce in una lisa rispettando l'ordine in cui io ho scritto 

#print(sys.argv)

#print('Ciao', sys.argv[1])

import argparse

parser =  argparse.ArgumentParser()

parser.add_argument('-n','--nome_esteso', help="E' il nome da stampare")

#parser.add_argument('-b','--boolean_value', action='store_true', help="imposta il valore 'True' se trova il parametro")
#parser.add_argument('-d','--con_default',  default='riferimento', help="Parametro che ha già un valore di default se non viene fornito l'argomento")

variabili = parser.parse_args() # fa il parsing degli argomenti da linea di comando

print(variabili.nome_esteso)