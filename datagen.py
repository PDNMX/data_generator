# data generator
#from pprint import pprint
import pandas as pd
import json
import argparse
#import sqlite3
import uuid
from random_data import *

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

    # nombres y apellidos
    hombres = pd.read_csv('./corpus/hombres.csv')
    mujeres = pd.read_csv('./corpus/mujeres.csv')
    apellidos = pd.read_csv('./corpus/apellidos-20.csv')
    # domicilios
    # catálogos de códigos
    # conn = sqlite3.connect('corpus.db')

    for x in range(0, number_of_samples):
        sample = dict()
        # información personal
        sample['id'] = str(uuid.uuid1())
        sample['informacion_personal'] = {}

        sample['informacion_personal']['informacion_general'] = {
            "nombres": "Carlos",
            "primer_apellido": "Pérez",
            "segundo_apellido": "López",
            "nacionalidades": [{
                "valor": "México",
                "codigo": "MX"
            }],
            "pais_nacimiento": {
                "valor": "México",
                "codigo": "MX"
            },
            "entidad_federativa_nacimiento": {
                "nom_ent": "México",
                "cve_ent": 15
            },
            "curp": "BEML920313HMCLNS09",
            "rfc": "GOAP780710RH7",
            "fecha_nacimiento": get_bith_date(),
            "numero_identificacion_oficial": "a1b2c3d4",
            "correo_electronico": {
                "personal": get_email('abcmail.com'),
                "laboral": get_email('dependencia.gob.mx')
            },
            "telefono": {
                "personal": get_telephone('fijo'),
                "celular": get_telephone('celular')
            },
            "domicilio": {
                "pais": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "entidad_federativa": {
                    "nom_ent": "México",
                    "cve_ent": 15
                },
                "municipio": {
                    "nom_mun": "Ecatepec de Morelos",
                    "cve_mun": 27
                },
                "cp": 55018,
                "localidad": {
                    "nom_loc": "Ecatepec de Morelos",
                    "cve_loc": 1
                },
                "vialidad": {
                    "tipo_vial": "CALLE",
                    "nom_vial": "El Rosal"
                },
                "numExt": 24,
                "numInt": 48
            },
            "estado_civil": {
                "codigo": "CAS",
                "valor": "Casado (a)"
            },
            "regimen_matrimonial": {
                "codigo": "SBI",
                "valor": "Separación de bienes"
            },
            "fecha_declaracion": "31/07/1980"
        }

        sample['informacion_personal']['datos_curriculares'] = {
            "grado_maximo_escolaridad": "Licenciatura",
            "grados_academicos": [{
                "grado_obtenido": "Licenciatura",
                "institucion_educativa": get_college(),
                "lugar_institucion_educativa": {
                    "nom_ent": "México",
                    "cve_ent": 15
                },
                "carrera": get_degree(),
                "estatus": {
                    "codigo": "CURS",
                    "valor": "Cursando"
                },
                "ano_conclusion": "2005",
                "documento_obtenido": {
                    "codigo": "BOL",
                    "valor": "Boleta"
                },
                "cedula_profesional": "2094884"
            }]
        }

        sample['informacion_personal']['datos_encargo_actual'] = {
            "ente_publico": get_institution(),
            "empleo_cargo_comision": get_position(),
            "nivel_gobierno": {
                "codigo": "EST",
                "valor": "Estatal"
            },
            "poder_juridico": {
                "codigo": "JUD",
                "valor": "Judicial"
            },
            "contratado_honorarios": False,
            "nivel_encargo": "CA0001",
            "area_adscripcion": "Unidad de Política Regulatoria",
            "fecha_posesion": "31/07/1980",
            "lugar_ubicacion": {
                "valor": "México",
                "codigo": "MX"
            },
            "direccion_encargo": {
                "pais": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "entidad_federativa": {
                    "nom_ent": "México",
                    "cve_ent": 15
                },
                "municipio": {
                    "nom_mun": "Ecatepec de Morelos",
                    "cve_mun": 27
                },
                "cp": 55018,
                "localidad": {
                    "nom_loc": "Ecatepec de Morelos",
                    "cve_loc": 1
                },
                "vialidad": {
                    "tipo_vial": "CALLE",
                    "nom_vial": "El Rosal"
                },
                "numExt": 24,
                "numInt": 48
            },
            "sector_industria": {
                "codigo": "SFS",
                "valor": "Servicios de salud y asistencia social"
            },
            "funciones_principales": [{
                "codigo": "ABI",
                "valor": "Administración de bienes"
            }]
        }

        sample['informacion_personal']['experiencia_laboral'] = [
            {
                "ambito": {
                    "codigo": "Pub",
                    "valor": "Público"
                },
                "nivel_gobierno": {
                    "codigo": "EST",
                    "valor": "Estatal"
                },
                "poder_ente": {
                    "codigo": "JUD",
                    "valor": "Judicial"
                },
                "nombre_institucion": "Instituto Federal de Telecomunicaciones",
                "unidad_administrativa": "Unidad de Política Regulatoria",
                "direccion": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad_federativa": {
                        "nom_ent": "México",
                        "cve_ent": 15
                    },
                    "municipio": {
                        "nom_mun": "Ecatepec de Morelos",
                        "cve_mun": 27
                    },
                    "cp": 55018,
                    "localidad": {
                        "nom_loc": "Ecatepec de Morelos",
                        "cve_loc": 1
                    },
                    "vialidad": {
                        "tipo_vial": "CALLE",
                        "nom_vial": "El Rosal"
                    },
                    "numExt": 24,
                    "numInt": 48
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "jerarquia_rango": "string",
                "cargo_puesto": "Jefe de Departamento",
                "fecha_ingreso": "31/07/1980",
                "fecha_salida": "31/07/1980",
                "funciones_principales": [{
                    "codigo": "ABI",
                    "valor": "Administración de bienes"
                }]
            }
        ]

        sample['informacion_personal']['datos_dependientes_economicos'] = [
            {
                "nombres": "Carlos",
                "primer_apellido": "Pérez",
                "segundo_apellido": "López",
                "tipo_relacion": {
                    "codigo": "CONY",
                    "valor": "Cónyuge"
                },
                "nacionalidad": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "curp": "BEML920313HMCLNS09",
                "rfc": "GOAP780710RH7",
                "fecha_nacimiento": get_bith_date(),
                "numero_identificacion_nacional": "ABCD1234",
                "habita_domicilio_declarante": True,
                "domicilio": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad_federativa": {
                        "nom_ent": "México",
                        "cve_ent": 15
                    },
                    "municipio": {
                        "nom_mun": "Ecatepec de Morelos",
                        "cve_mun": 27
                    },
                    "cp": 55018,
                    "localidad": {
                        "nom_loc": "Ecatepec de Morelos",
                        "cve_loc": 1
                    },
                    "vialidad": {
                        "tipo_vial": "CALLE",
                        "nom_vial": "El Rosal"
                    },
                    "numExt": 24,
                    "numInt": 48
                },
                "medio_contacto": get_email('coldmail.com'),
                "ingresos_propios": True,
                "ocupacion_profesion": "Administrador de empresas",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "proveedor_contratista_gobierno": True,
                "tiene_intereses_mismo_sector_declarante": True,
                "desarrolla_cabildeo_sector_declarante": True,
                "beneficiario_programa_publico": [{
                    "nombre_programa": "Prospera",
                    "institucion_otorga_apoyo": "XE-IPN Canal 11",
                    "tipo_apoyo": "Servicio",
                    "valor_apoyo": 4000
                }],
                "observaciones": "Esto es una observación"
            }
        ]

        # Intereses
        sample['intereses'] = {}
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
