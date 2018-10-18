# data generator
from pprint import pprint
import pandas as pd
import json
import argparse


parser = argparse.ArgumentParser(description='SESNA data generator')
parser.add_argument('-s','--sys', default=0, type=int,  help='System number', choices=[1, 2, 3])
parser.add_argument('-n', '--samples', default=10, type=int, help='Number of samples')
parser.add_argument('-o','--out', default='JSON', help='Output format', choices= ['JSON', 'CSV'])
args = parser.parse_args()

sys_number = args.sys
samples = args.samples

if sys_number == 1:
    print ('Sistema 1 -> Declaraciones ')
    for x in range(0, samples):
        sample = dict()
        sample['id'] = ''
        sample['primer_apellido'] = ''
        sample['segundo_apellido'] = ''
        pprint(sample)
elif sys_number == 1:
    print ('Sistema 2 -> Servidores públicos que intervienen en contrataciones')
elif sys_number == 2:
    print ('Sistema 3 -> Servidores públicos y particulares sancionados')
else:
    parser.print_help()