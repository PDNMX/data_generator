# data generator
from pprint import pprint
import pandas as pd
import json
import argparse
#import sqlite3
import uuid

parser = argparse.ArgumentParser(description='SESNA data generator')
parser.add_argument('-s','--sys', default=0, type=int,  help='System number', choices=[1, 2, 3])
parser.add_argument('-n', '--samples', default=10, type=int, help='Number of samples')
parser.add_argument('-o','--out', default='JSON', help='Output format', choices= ['JSON', 'CSV'])
args = parser.parse_args()

sys_number = args.sys
number_of_samples = args.samples

if sys_number == 1:
    print ('Sistema 1 -> Declaraciones ')
    samples = []


    hombres = pd.read_csv('./corpus/hombres.csv')
    mujeres = pd.read_csv('./corpus/mujeres.csv')
    apellidos = pd.read_csv('./corpus/apellidos-20.csv')
    #conn = sqlite3.connect('corpus.db')
    for x in range(0, number_of_samples):
        sample = dict()
        # información personal
        sample['informacion_personal'] = {}
        sample['informacion_personal']['id'] = str(uuid.uuid1())
        sample['informacion_personal']['nombres'] = ''
        sample['informacion_personal']['primer_apellido'] = ''
        sample['informacion_personal']['segundo_apellido'] = ''
        sample['informacion_personal']['nacionalidad_representante'] = {}
        sample['informacion_personal']['nacionalidad_representante']['pais'] = 'México'
        sample['informacion_personal']['nacionalidad_representante']['codigo'] = 'MX'
        sample['informacion_personal']['entidad_federativa_nacimiento'] = {}
        sample['informacion_personal']['entidad_federativa_nacimiento']['nom_ent'] = 'México'
        sample['informacion_personal']['entidad_federativa_nacimiento']['cve_ent'] = '15'
        sample['informacion_personal']['curp'] = ''
        sample['informacion_personal']['rfc'] = {}
        sample['informacion_personal']['rfc']['valor'] = ''
        sample['informacion_personal']['rfc']['homoclave'] = ''
        sample['informacion_personal']['fecha_nacimiento'] = ''
        sample['informacion_personal']['numero_identificacion_oficial'] = ''


        sample['informacion_personal']['datos_curriculares'] = {}
        sample['informacion_personal']['datos_curriculares']['grado_maximo_escolaridad'] = ''
        # Intereses
        sample['intereses'] = {}
        sample['intereses'][''] =''
        # Ingresos
        sample['ingresos'] = {}
        # Activos
        sample['activos'] = {}
        # Pasivos
        sample['pasivos'] = {}
        #pprint(sample)
        samples.append(sample)

    with open('data.json', 'w') as outfile:
        json.dump(samples,outfile, indent=4)

   #conn.close()
elif sys_number == 1:
    print ('Sistema 2 -> Servidores públicos que intervienen en contrataciones')
elif sys_number == 2:
    print ('Sistema 3 -> Servidores públicos y particulares sancionados')
else:
    parser.print_help()
