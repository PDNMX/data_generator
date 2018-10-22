# data generator
from pprint import pprint
import pandas as pd
import json
import argparse
#import sqlite3
import uuid
import random

parser = argparse.ArgumentParser(description='SESNA data generator')
parser.add_argument('-s','--sys', default=0, type=int,  help='System number', choices=[1, 2, 3])
parser.add_argument('-n', '--samples', default=10, type=int, help='Number of samples')
parser.add_argument('-o','--out', default='JSON', help='Output format', choices= ['JSON', 'CSV'])
args = parser.parse_args()

sys_number = args.sys
number_of_samples = args.samples

def get_email(nombre, primer_apellido):
    return "{0}.{1}@example.com".format(nombre,primer_apellido)

def get_telephone():
    return str(random.randint(5500000000,7779999999))

if sys_number == 1:
    print ('Sistema 1 -> Declaraciones ')
    samples = []

    # nombres y apellidos
    hombres = pd.read_csv('./corpus/hombres.csv')
    mujeres = pd.read_csv('./corpus/mujeres.csv')
    apellidos = pd.read_csv('./corpus/apellidos-20.csv')
    # domicilios
    # conn = sqlite3.connect('corpus.db')

    for x in range(0, number_of_samples):
        sample = dict()
        # información personal
        sample['informacion_personal'] = {}
        sample['informacion_personal']['id'] = str(uuid.uuid1())
        sample['informacion_personal']['nombres'] = 'Juan'
        sample['informacion_personal']['primer_apellido'] = 'Pérez'
        sample['informacion_personal']['segundo_apellido'] = 'García'
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
        sample['informacion_personal']['correo_electronico'] = {}
        sample['informacion_personal']['correo_electronico']['laboral'] = ''
        sample['informacion_personal']['correo_electronico']['personal'] = ''
        sample['informacion_personal']['telefono'] = {}
        sample['informacion_personal']['telefono']['laboral']= get_telephone()
        sample['informacion_personal']['telefono']['personal']= get_telephone()
        sample['informacion_personal']['telefono']['celular']= get_telephone()
        sample['informacion_personal']['domicilio'] = {}
        sample['informacion_personal']['domicilio']['pais'] = 'MX'
        sample['informacion_personal']['domicilio']['entidad_federativa'] = {}
        sample['informacion_personal']['domicilio']['entidad_federativa']['nom_ent'] = 'México'
        sample['informacion_personal']['domicilio']['entidad_federativa']['cve_ent'] = '15'
        sample['informacion_personal']['domicilio']['municipio']= {}
        sample['informacion_personal']['domicilio']['municipio']['nom_mun']= 'Ecatepec de Morelos'
        sample['informacion_personal']['domicilio']['municipio']['cve_mun']= '033'
        sample['informacion_personal']['domicilio']['cp']='55018'
        sample['informacion_personal']['domicilio']['localidad']={}
        sample['informacion_personal']['domicilio']['localidad']['nom_loc']='Ecatepec de Morelos'
        sample['informacion_personal']['domicilio']['localidad']['cve_loc'] = '001'
        sample['informacion_personal']['domicilio']['vialidad']={}
        sample['informacion_personal']['domicilio']['vialidad']['tipo_vial']= 'CALLE'
        sample['informacion_personal']['domicilio']['vialidad']['nom_vial']='El Rosal'


        sample['informacion_personal']['datos_curriculares']={}
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



