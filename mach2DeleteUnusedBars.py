import os
import sys
import argparse
import configparser

# przygotowanie parsowania parametrów wejściowych
parser = argparse.ArgumentParser(description='Skrypt do usuwania niepotrzebnych listew z pliku listwy.dat. Do działania potrzebuję listy uzywnaych listew.')
parser.add_argument('-i',dest='bar_list_in_use',
                    help='plik z listą używanych listew')
parser.add_argument('mach2_listwy',
                    help='plik wejściowy listwy.dat')
parser.add_argument('-o',dest='output_file',
                    help='plik wyjściowy listwy.dat')

#parsowanie parametrów wejściowych
args = parser.parse_args()
if args.output_file==None:
    args.output_file = args.mach2_listwy
print(args)


config = configparser.ConfigParser()
config.optionxform = str
config.read_file(open(args.mach2_listwy))

bars_in_use = []

# if config.has_section('SEW24POW'):
#     print('has section SEW24POW')
print(len(config.sections()))

with open(args.bar_list_in_use, 'r', newline='') as bar_list_file:
    bars_in_use = bar_list_file.read().splitlines()

for section in config.sections():
    if section not in bars_in_use:
        config.remove_section(section)
        print(section,' removed')
# for section in config.sections():
#     print(section)
print(len(config.sections()))

config.write(open(args.output_file,'w'))