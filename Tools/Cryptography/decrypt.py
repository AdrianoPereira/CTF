#x-x-x--x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
# Author:       Adriano Almeida - adrianopereira.github.com     -
# Algorithm:    Encode and decode text using shift of           x
#               position of character on table ASCII            -
#                                                     Sc4recr0w x
#x-x-x--x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
#char
#bin
#oct
#dec
#hex

import argparse

parser = argparse.ArgumentParser(description = 'A program to working with manipulations of text using the table ASCII')

parser.add_argument('-t', '--text', action='store', dest='text', required=True)
parser.add_argument('-c', '--current', action='store', dest='current', required=True)
parser.add_argument('-r', '--result', action='store', dest='result', required=True)

args = parser.parse_args()

def charToDec(string):
    return ' '.join([str(ord(char)) for char in string])

def decToChar(string):
    _list = string.split()
    return (' '.join([str(chr(int(dig))) for dig in _list])).replace(' ', '')



if args.current == 'char':
    if args.result == 'dec':
        print('Character to Decimal:', charToDec(args.text))

elif args.current == 'dec':
    if args.result == 'char':
        print('Decimal to Character: ', decToChar(args.text))

