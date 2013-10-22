#!/usr/bin/python

import sys

def convert(t,fc):
        if t == "2f":
                print (fc * 9) / 5 + 32,"Degress Fahrenheit"
        elif t == "2c":
                print (fc - 32) / 9 * 5,"Degress Celcuis"

def usage():
  print('''\
Usage: convert-temp [TEMP] [TYPE]
This program coverts the temperatures celcius and fahrenheit.
Options include:
     --version   : Prints the version number
     --help      : Display this help

 Examples:
     convert_temp 33 2f     Convert to fahrenheit
     convert_temp 80 2c    Convert to celcuis''')

try:
        if sys.argv[1].startswith('--'):
                option = sys.argv[1][2:]
                # fetch sys.argv[1] but without the first two characters
                if option == 'version':
                        print( 'Version 0.1')
                elif option == 'help':
                        usage()
                else:
                        print( 'Unknown option.')
                sys.exit()
        elif len(sys.argv) < 3:
                print( 'Insufficient Parameters.')
        else:
                type = sys.argv[2]
                temp = int(sys.argv[1])
                convert(type,temp)
except:
        usage()