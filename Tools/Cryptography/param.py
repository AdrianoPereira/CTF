#Program to add arguments by command line

import argparse

parser = argparse.ArgumentParser(description = 'Programa para adicionar argumentos por linha de comando')

parser.add_argument('--string','-s',  action='store', dest='string', default='Uma frase', required=False, help='Texto para ser impresso')
parser.add_argument('--number', '-n', action='store', dest='n', required=True, help ='Número de vezes que será impressa')

arguments = parser.parse_args()
for x in range (int(arguments.n)):
    print(arguments.string)
