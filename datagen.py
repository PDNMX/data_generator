# data generator
import json
import argparse
#import sqlite3
from pymongo import MongoClient
import uuid
from random_data import *

parser = argparse.ArgumentParser(description='SESNA data generator')
parser.add_argument('-s','--sys', default=0, type=int,  help='System number', choices=[1, 2, 3])
parser.add_argument('-n', '--samples', default=10, type=int, help='Number of samples')
#parser.add_argument('-o','--out', default='JSON', help='Output format', choices= ['JSON', 'CSV'])
args = parser.parse_args()

sys_number = args.sys
number_of_samples = args.samples

client = MongoClient('localhost', 27017)
db = client.datagen

if sys_number == 1:
    print ('Sistema 1 -> Declaraciones ')

    collection = db.s1
    #samples = []
    # domicilios
    # catálogos de códigos
    # conn = sqlite3.connect('corpus.db')

    for x in range(0, number_of_samples):
        sample = dict()
        # información personal
        sample['id'] = str(uuid.uuid1())
        sample['informacion_personal'] = {}

        sample['informacion_personal']['informacion_general'] = {
            "nombres": get_name(),
            "primer_apellido": get_last_name(),
            "segundo_apellido": get_last_name(),
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
                "nombres": get_name(),
                "primer_apellido": get_last_name(),
                "segundo_apellido": get_last_name(),
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
                    "institucion_otorga_apoyo": get_institution(),
                    "tipo_apoyo": "Servicio",
                    "valor_apoyo": 4000
                }],
                "observaciones": lorem_ipsum()
            }
        ]

        # Intereses
        sample['intereses'] = {
            "empresas_sociedades_asociaciones": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": get_name(),
                        "primer_apellido" : get_last_name(),
                        "segundo_apellido" : get_last_name()
                    },
                    "nombre_empesa_sociedad_asociacion": "DataIQ",
                    "pais_registro": {
                        "pais": "México",
                        "codigo": "MX"
                    },
                    "fecha_consitutcion": "2015-05-10",
                    "numero_registro": "ABC123",
                    "rfc": "GOAP780710RH7",
                    "domicilio": {
                        "entidad_federativa": {
                            "nom_ent": "México",
                            "cve_ent": "15"
                        },
                        "municipio": {
                            "nom_mun": "Ecatepec de Morelos",
                            "cve_mun": "033"
                        },
                        "cp": "55018",
                        "localidad": {
                            "nom_loc": "Ecatepec de Morelos",
                            "cve_loc": "0001"
                        },
                        "vialidad": {
                            "tipo_vial": "CALLE",
                            "nom_vial": "El Rosal"
                        },
                        "numExt": {
                            "numExt_num": 24
                        },
                        "numInt": {
                            "numInt_alf": "S/N"
                        }
                    },
                    "rol":"Dueño",
                    "actividad_Economica": True,
                    "sector_industria": {
                        "codigo": "CPMY",
                        "valor": "Comercio al por mayor"
                    },
                    "porcentaje_participacion": 70
                }
            ],
            "membresias": [
                {
                    "id": 1,
                    "titular": {
                        "id": 2,
                        "nombres": get_name(),
                        "primer_apellido" : get_last_name(),
                        "segundo_apellido" : get_last_name()
                    },
                    "tipo_institucion": {
                        "codigo": "ASC",
                        "valor": "Asociaciones civiles"
                    },
                    "nombre_institucion": "Asociacion A.C",
                    "naturaleza_membresia": "Civil",
                    "domicilio": {
                        "entidad_federativa": {
                            "nom_ent": "México",
                            "cve_ent": "15"
                        },
                        "municipio": {
                            "nom_mun": "Ecatepec de Morelos",
                            "cve_mun": "033"
                        },
                        "cp": "55018",
                        "localidad": {
                            "nom_loc": "Ecatepec de Morelos",
                            "cve_loc": "0001"
                        },
                        "vialidad": {
                            "tipo_vial": "CALLE",
                            "nom_vial": "El Rosal"
                        },
                        "numExt": {
                            "numExt_num": 24
                        },
                        "numInt": {
                            "numInt_alf": "S/N"
                        }
                    },
                    "sector_industria": {
                        "codigo": "SSAS",
                        "valor": "Servicios de salud y asistencia social"
                    },
                    "rol": "Titular",
                    "fecha_inicio": "2018-05-14",
                    "pagado": True,
                    "observaciones": lorem_ipsum()
                }
            ],
            "apoyosBeneficiosPublicos": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": get_name(),
                        "primer_apellido" : get_last_name(),
                        "segundo_apellido" : get_last_name()
                    },
                    "es_beneficiario": True,
                    "programa": "Programa de Estímulos Económicos a Deportistas del Distrito Federal",
                    "institucion_otorgante" : get_institution(),
                    "nivel_orden_gobierno": {
                        "codigo": "EST",
                        "valor": "Estatal"
                    },
                    "tipo_apoyo": {
                        "codigo": "SERV",
                        "valor": "Servicio"
                    },
                    "valor_apoyo": 7500,
                    "observaciones": lorem_ipsum()
                }
            ],
            "representacion_activa": [
                {
                    "id": 1,
                    "titular": {
                        "id": 3,
                        "nombres": get_name(),
                        "primer_apellido" : get_last_name(),
                        "segundo_apellido" : get_last_name()
                    },
                    "tipo_representacion": {
                        "codigo": "APOD",
                        "valor": "Apoderado"
                    },
                    "nombre_parte": "Cecilia Gómez Urrutia",
                    "curp_parte": "BEML920313HMCLNS09",
                    "rfc_parte": "GOAP780710RH7",
                    "fecha_nacimiento_parte": "1956-08-15",
                    "sector_industria": {
                        "codigo": "CPMY",
                        "valor": "Comercio al por mayor"
                    },
                    "fecha_inicio": "2017-08-12",
                    "pagado": True,
                    "observaciones": lorem_ipsum()
                }
            ],
            "representacion_pasiva": [
                {
                    "id": 1,
                    "titular": {
                        "id": 2,
                        "nombres": get_name(),
                        "primer_apellido" : get_last_name(),
                        "segundo_apellido" : get_last_name()
                    },
                    "tipo_representacion": {
                        "codigo": "APOD",
                        "valor": "Apoderado"
                    },
                    "nombre_representante": "Augusto Fernández Castro",
                    "fecha_inicio_representacion": "2016-05-12",
                    "nacionalidad_representante": {
                        "pais": "México",
                        "codigo": "MX"
                    },
                    "curp_representante": "BEML920313HMCLNS09",
                    "rfc_representante": "GOAP780710RH7",
                    "fecha_nacimiento_representante" : "1987-08-12",
                    "tiene_intereses": True,
                    "ocupacion_profesion": "Contador",
                    "sector_industria": {
                        "codigo": "CPMY",
                        "valor": "Comercio al por mayor"
                    },
                    "observaciones": lorem_ipsum()
                }
            ],
            "socios_comerciales": [
                {
                    "id": 1,
                    "titular": {
                        "id": 2,
                        "nombres": get_name(),
                        "primer_apellido" : get_last_name(),
                        "segundo_apellido" : get_last_name()
                    },
                    "nombre_actividad": "Actividad",
                    "tipo_vinculo": {
                        "codigo": "SOC",
                        "valor": "Socio"
                    },
                    "antiguedad_vinculo": "2017-05-14",
                    "rfc_entidad": "GOAP780710RH7",
                    "nombre_socio": "Armando Rodríguez Saes",
                    "curp_socio": "BEML920313HMCLNS09",
                    "rfc_socio": "GOAP780710RH7",
                    "lugar_nacimiento_socio": {
                        "pais": "México",
                        "codigo": "MX"
                    },
                    "fecha_nacimiento_socio" : "1970-05-14",
                    "porcentaje_participacion": 70,
                    "sector_industria": {
                        "codigo": "CPMY",
                        "valor": "Comercio al por mayor"
                    },
                    "observaciones": lorem_ipsum()
                }
            ],
            "clientes_principales": [
                {
                    "id": 1,
                    "titular": {
                        "id": 4,
                        "nombres": get_name(),
                        "primer_apellido" : get_last_name(),
                        "segundo_apellido" : get_last_name()
                    },
                    "nombre_naturaleza_negocio": {
                        "codigo": "Negocio",
                        "valor": "Nombre negocio"
                    },
                    "numero_Registro": "HTC896DSFA",
                    "dueño_encargado": "Salvador Hernández Torres",
                    "nombre_denominacion_social_cliente": "AMEX.S.A.",
                    "rfc_cliente": "GOAP780710RH7",
                    "domicilio_cliente": {
                        "entidad_federativa": {
                            "nom_ent": "México",
                            "cve_ent": "15"
                        },
                        "municipio": {
                            "nom_mun": "Ecatepec de Morelos",
                            "cve_mun": "033"
                        },
                        "cp": "55018",
                        "localidad": {
                            "nom_loc": "Ecatepec de Morelos",
                            "cve_loc": "0001"
                        },
                        "vialidad": {
                            "tipo_vial": "CALLE",
                            "nom_vial": "El Rosal"
                        },
                        "numExt": {
                            "numExt_num": 24
                        },
                        "numInt": {
                            "numInt_alf": "S/N"
                        }
                    },
                    "sector_industria": {
                        "codigo": "CPMY",
                        "valor": "Comercio al por mayor"
                    },
                    "porcentaje_facturacion": 20,
                    "observaciones": lorem_ipsum()
                }
            ],
            "otras_partes": [
                {
                    "id": 1,
                    "titular": {
                        "id": 4,
                        "nombres": get_name(),
                        "primer_apellido" : get_last_name(),
                        "segundo_apellido" : get_last_name()
                    },
                    "tipo_parte": {
                        "codigo": "GPR",
                        "valor": "Garantes de Préstamos Recibidos"
                    },
                    "nombre_denominacion_parte": "",
                    "fecha_inicio_relacion": "2016-05-08",
                    "nacionalidad": {
                        "pais": "México",
                        "codigo": "MX"
                    },
                    "curp": "BEML920313HMCLNS09",
                    "rfc": "GOAP780710RH7",
                    "fecha_nacimiento": "1979-08-23",
                    "ocupacion_profesion": "Administrador de empresas",
                    "tiene_intereses": True,
                    "sector_industria": {
                        "codigo": "CPMY",
                        "valor": "Comercio al por mayor"
                    },
                    "observaciones": lorem_ipsum()
                }
            ],
            "beneficios_gratuitos": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Carlos",
                        "primer_apellido" : "Pérez",
                        "segundo_apellido" : "López"
                    },
                    "tipo_beneficio": {
                        "codigo": "TARJ",
                        "valor": "Tarjetas o monederos electrónicos"
                    },
                    "origen_beneficio":"Prestación laboral",
                    "sector_industria": {
                        "codigo": "CPMY",
                        "valor": "Comercio al por mayor"
                    },
                    "valor_beneficio": 1256,
                    "observaciones": lorem_ipsum()
                }
            ]
        }
        # Ingresos
        sample['ingresos'] = {}
        # Activos
        sample['activos'] = {}
        # Pasivos
        sample['pasivos'] = {}

        collection.insert_one(sample)
        #samples.append(sample)


    #with open('data.json', 'w') as outfile:
    #    json.dump(samples,outfile, indent=4)


#conn.close()
elif sys_number == 1:
    print ('Sistema 2 -> Servidores públicos que intervienen en contrataciones')
elif sys_number == 2:
    print ('Sistema 3 -> Servidores públicos y particulares sancionados')
else:
    parser.print_help()
