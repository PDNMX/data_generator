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
        sample['ingresos'] = {
            "sueldos_y_salarios_publicos": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "ente_publico": "Presidencia de la República",
                    "rfc": "GOAP780710RH7",
                    "ingreso_bruto_anual": {
                        "valor": 10000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "MESS",
                            "valor": "Meses"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ],
            "sueldos_salarios_otros_empleos": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "Max Power Inc.",
                    "rfc": "PNKSD780710RH7",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "valor": "Sector público"
                    },
                    "descripcion_actividad_servicio": "Servicio profesional de TI",
                    "domicilio_persona_recibe_ingreso": {
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "valor": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "SEMS",
                            "valor": "Semanas"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ],
            "actividad_profesional": [
                {
                    "id": 1,
                    "titular": {
                        "id": 2,
                        "nombres": "Juan",
                        "primer_apellido" : "Tovar",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "Nombre",
                    "rfc": "PEGJ851231",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "valor": "Sector Público"
                    },
                    "descripcion_actividad_servicio": "Descripción del servicio",
                    "domicilio_persona_recibe_ingreso": {
                        "pais": "MX",
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "MESS",
                            "valor": "Meses"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ],
            "actividad_empresarial": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "Empresa S.A.",
                    "rfc": "PNKSD780710RH7",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "nombre": "Sector público"
                    },
                    "descripcion_actividad_servicio": "Descripción del servicio",
                    "domicilio_actividad_empresarial": {
                        "pais": "MX",
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "SEMS",
                            "valor": "Semanas"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ],
            "actividad_economica_menor": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "Nombre",
                    "rfc": "PNKSD780710RH7",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "valor": "Sector público"
                    },
                    "descripcion_actividad_servicio": "Descripción del servicio",
                    "domicilio_actividad": {
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "SEMS",
                            "valor": "Semanas"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ],
            "arrendamiento": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "",
                    "rfc": "PNKSD780710RH7",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "valor": "Sector público"
                    },
                    "descripcion_actividad_servicio": "Descripción del servicio",
                    "domicilio_actividad": {
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "SEMS",
                            "valor": "Semanas"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ],
            "intereses": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "BANC S.A.",
                    "rfc": "PNKSD780710RH7",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "valor": "Sector público"
                    },
                    "descripcion_actividad_servicio": "Descripción del servicio",
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "SEMS",
                            "valor": "Semanas"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": "no hay observaciones"
                }
            ],
            "premios": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "Loteria Nacional",
                    "rfc": "PNKSD780710RH7",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "valor": "Sector público"
                    },
                    "descripcion_actividad_servicio": "Descripción del servicio",
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "SEMS",
                            "valor": "Semanas"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ],
            "enajenacion_bienes": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "",
                    "rfc": "PNKSD780710RH7",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "valor": "Sector público"
                    },
                    "descripcion_actividad_servicio": "Descripción del servicio",
                    "domicilio_bien_enajenado": {
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "SEMS",
                            "valor": "Semanas"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ],
            "otros_ingresos": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Sergio",
                        "primer_apellido" : "Rodríguez",
                        "segundo_apellido" : "López"
                    },
                    "nombre_denominacion_razon_social": "Centro Educativo",
                    "rfc": "PNKSD780710RH7",
                    "curp": "PEGJ851231HVZRVR05",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "tipo_actividad_servicio": {
                        "codigo": "SPU",
                        "valor": "Sector público"
                    },
                    "descripcion_actividad_servicio": "Descripción del servicio",
                    "domicilio_actividad_situacion": {
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
                    "ingreso_bruto_anual": {
                        "valor": 20000,
                        "moneda": {
                            "codigo": "MXN",
                            "moneda": "Pesos"
                        },
                        "unidad_temporal": {
                            "codigo": "SEMS",
                            "valor": "Semanas"
                        },
                        "duracion_frecuencia": 10,
                        "fecha_transaccion": "2016-12-14"
                    },
                    "observaciones_comentarios": lorem_ipsum()
                }
            ]
        }

        # Activos
        sample['activos'] = {
            "bienes_inmuebles": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor:": "Incorporación"
                },
                "tipo_bien": {
                    "codigo": "VEH",
                    "valor:": "Vehículo"
                },
                "superficie_terreno": 300,
                "superficie_construccion": 100,
                "porcentaje_propiedad": 100,
                "nombre_copropietario": {
                    "nombres": "Juan",
                    "primer_apellido": "Pérez",
                    "segundo_apellido": "García"
                },
                "identificacion_bien": {
                    "numero_escritura_publica": 202020,
                    "numero_registro_publico_propiedad": 404040,
                    "folio_real": "jsjs74747",
                    "fecha_contrato_compra-venta_privado": "1985-12-31"
                },
                "domicilio_donde_ubica_bien": {
                    "pais": "MX",
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
                "forma_adquisicion": {
                    "codigo": "CONY",
                    "valor:": "Cónyuge"
                },
                "nombre_denominacion_razon_social_quien_adquirio": "Monster Inc.",
                "rfc_quien_adquirio": "PEGJ851231C33",
                "curp_quien_adquirio": "PEGJ851231HVZRVR05",
                "relacion_con_persona_quien_adquirio_inmueble": {
                    "codigo": "",
                    "valor:": ""
                },
                "sector_industria": {
                    "codigo": "MINE",
                    "valor:": "Minería"
                },
                "fecha_adquisicion": "1985-12-31",
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": "MXN"
                },
                "valor_catastral": 800.00,
                "observaciones_comentarios": "No hay comentarios"
            }],
            "bienes_muebles_registrables": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor:": "Incorporación"
                },
                "tipo_bien_mueble": {
                    "codigo": "VEH",
                    "valor:": "Vehículo"
                },
                "marca": "NISSAN",
                "submarca_linea_tipo": "RS-122234",
                "modelo": "2018",
                "numero_serie": "6545243-4334",
                "lugar_registro": {
                    "codigo": "MX",
                    "valor:": "México"
                },
                "porcentaje_propiedad": 99,
                "nombres_copropietarios": [{
                    "nombres": "Juan",
                    "primer_apellido": "Pérez",
                    "segundo_apellido": "García"
                }, {
                    "nombres": "Manuel",
                    "primer_apellido": "Tenorio",
                    "segundo_apellido": "García"
                }],
                "numero_registro_publico_vehicular": 455000,
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor:": "Cesión"
                },
                "nombre_denominacion_razon_social_quien_adquirio": "Monstr Inc.",
                "rfc_quien_adquirio": "PEGJ851231C33",
                "curp_quien_adquirio": "PEGJ851231HVZRVR05",
                "relacion_con_persona_quien_adquirio_inmueble": {
                    "codigo": "DEC",
                    "valor:": "Dependiente económico"
                },
                "sector_industria": {
                    "codigo": "MINE",
                    "valor:": "Minería"
                },
                "fecha_adquisicion": "1985-12-31",
                "precio_adquisicion": {
                    "valor": 4000,
                    "mmoneda": "MXN"
                },
                "valor_catastral": 4500,
                "observaciones_comentarios": "No hay comentarios"
            }],
            "bienes_muebles_no_registrables": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor:": "Incorporación"
                },
                "tipo_bien": {
                    "codigo": "BAR",
                    "valor:": "Barco"
                },
                "descripcion": "sin descripción",
                "numero_registro": 458800,
                "lugar_registro": "MX",
                "nombres_copropietarios": [{
                    "nombres": "Juan",
                    "primer_apellido": "Pérez",
                    "segundo_apellido": "García"
                }, {
                    "nombres": "Manuel",
                    "primer_apellido": "Tenorio",
                    "segundo_apellido": "García"
                }],
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor:": "Cesión"
                },
                "nombre_denominacion_razon_social_quien_adquirio": "Tesl Mtr Inc.",
                "relacion_con_persona_quien_adquirio": {
                    "codigo": "CONY",
                    "valor:": "Cónyuge"
                },
                "fecha_adquisicion": "1995-12-31",
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": "MXN"
                },
                "observaciones_comentarios": "No hay comentarios"
            }],
            "inversiones_cuentas_valores": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor:": "Incorporación"
                },
                "tipo_inversion": {
                    "codigo": "VENT",
                    "valor:": "Venta"
                },
                "tipo_especifico_inversion": {
                    "codigo": "ACCS",
                    "valor:": "Acciones"
                },
                "numero_cuenta_contrato_inversion": "GFHRTY788778",
                "nacional_extranjero": {
                    "codigo": "MEX",
                    "valor:": "México"
                },
                "nombre_institucion": "Bank Inkc",
                "rfc_institucion": "PEGJ851231C33",
                "sector_industria": {
                    "codigo": "MINE",
                    "valor:": "Minería"
                },
                "domicilio_institucion": {
                    "pais": "MX",
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
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor:": "Cesión"
                },
                "fecha_inicio": "1985-12-31",
                "monto_original": 80000,
                "tipo_moneda": "USD",
                "tasa_interes": 10.00,
                "saldo_anual": 5000,
                "plazo": 6,
                "unidad_medida_plazo": {
                    "codigo": "DIAS",
                    "valor:": "Días"
                },
                "porcentaje_inversion": 99.9,
                "observaciones_comentarios": "No hay comentarios"
            }],
            "efectivo_metales": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor:": "Incorporación"
                },
                "tipo_moneda": "USD",
                "monto": 78555,
                "tipo_metal": {
                    "codigo": "ORO",
                    "valor:": "Oro"
                },
                "unidades": "gramos",
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor:": "Cesión"
                },
                "observaciones_comentarios": "No hay comentarios"
            }],
            "fideicomisos": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor:": "Incorporación"
                },
                "nombre_identificador": "93232",
                "tipo_fideicomiso": {
                    "codigo": "GARNT",
                    "valor:": "Garantía"
                },
                "objetivo": "Objetivo del fideicomiso",
                "numero_registro": 788544,
                "fecha_creacion": "2005-12-31",
                "vigencia": "2006-12-31",
                "residencia": {
                    "codigo": "MEX",
                    "valor:": "México"
                },
                "valor": 78555555,
                "moneda": "MXN",
                "porcentaje_propiedad_derechos_fiduciarios": 99,
                "ingreso_monetario_obtenido": 56666,
                "institucion_fiduciaria": "Banco de México",
                "nombre_denominacion_razon_social_fideicomitente": "Banco Robmen1",
                "nombre_denominacion_razon_social_fideicomisario": "Banco Robmen2",
                "nombre_denominacion_razon_social_fiduciario": "Banco Robmenos2",
                "rfc_fideicomitente": "ZEGJ851231C33",
                "rfc_fideicomsario": "YEGJ851231C33",
                "rfc_fiduciario": "XEGJ851231C33",
                "curp_fideicomitente": "ZEGJ851231HVZRVR05",
                "curp_fideicomisario": "YEGJ851231HVZRVR05",
                "curp_fiduciario": "XEGJ851231HVZRVR05",
                "domicilio_fideicomitente": {
                    "pais": "MX",
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
                "domicilio_fideicomisario": {
                    "pais": "MX",
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
                "domicilio_fiduciario": {
                    "pais": "MX",
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
                "fecha_nacimiento_constitucion_fideicomitente": "1995-12-31",
                "fecha_nacimiento_constitucion_fideicomisario": "1994-12-31",
                "fecha_nacimiento_constitucion_fiduciario": "1985-12-31",
                "observaciones_comentarios": "no hay comentarios"
            }],
            "bienes_intangibles": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor:": "Incorporación"
                },
                "propietario_registrado": "Sergio Perez",
                "descripcion": "Aquí va una descripción breve",
                "ente_publico_encargado_registro": {
                    "nombres": "Raúl",
                    "primer_apellido": "Segura",
                    "segundo_apellido": "García"
                },
                "numero_registro": 754444,
                "fecha_registro": "1985-12-31",
                "sector_industria": {
                    "codigo": "MINE",
                    "valor:": "Minería"
                },
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": "MXN"
                },
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor:": "Cesión"
                },
                "fecha_vencimiento": "1985-12-31",
                "porcentaje_propiedad_caso_copropiedad": 90,
                "precio_total_adquisicion_caso_copropiedad": {
                    "valor": 4000,
                    "moneda": "MXN"
                },
                "nombre_denominacion_razon_social_copropietario": "Vien Inc,",
                "porcentaje_propiedad_copropietario": 10,
                "observaciones_comentarios": "No hay comentarios"
            }],
            "cuentas_por_cobrar": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "nombre_prestatario": {
                    "nombres": "Manuel",
                    "primer_apellido": "Tenorio",
                    "segundo_apellido": "García"
                },
                "numero_registro": 488755,
                "domicilio_prestatarios": {
                    "pais": "MX",
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
                    "codigo": "MINE",
                    "valor:": "Minería"
                },
                "fecha_prestamo": "1985-12-31",
                "monto_original_prestamo": 488844,
                "tasa_interes": 10.01,
                "saldo_pendiente": 4555,
                "fecha_vencimiento": "1985-12-31",
                "porcentaje_propiedad_caso_copropiedad": "",
                "nombre_copropietario": {
                    "nombres": "Luis",
                    "primer_apellido": "Peralta",
                    "segundo_apellido": "García"
                },
                "observacione_comentarios": "aquí más comentarios"
            }],
            "uso_beneficios_especie_propiedad_de_tercero": [{
                "id": 1,
                "titular": {
                    "id": 1,
                    "nombres": "Alma",
                    "primer_apellido": "Rosales",
                    "segundo_apellido": "Trueba"
                },
                "tipo_bien_servicio": "inmueble",
                "valor_mercado_aproximado": {
                    "valor": 4000,
                    "moneda": "MXN"
                },
                "nombre_denominacion_razon_social": "Marca Inc.",
                "rfc_tercero_propietario": "PEGJ851231C33",
                "curp_tercero_propietario": "PEGJ851231HVZRVR05",
                "sector_industria": "Servicios financieros y seguros",
                "relacion_persona": {
                    "codigo": "CONY",
                    "valor:": "Cónyuge"
                },
                "fecha_inicio": "1985-12-31",
                "domicilio_persona": {
                    "pais": "MX",
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
                "observaciones_comentarios": "Aquí comentarios u observaciones"
            }]
        }

        # Pasivos
        sample['pasivos'] = {
            "deudas": [
                {
                    "id": 1,
                    "titular": {
                        "id": 1,
                        "nombres": "Alma",
                        "primer_apellido" : "Rosales",
                        "segundo_apellido" : "Trueba"
                    },
                    "tipo_operacion": {
                        "codigo": "INCP",
                        "valor:": "Incorporación"
                    },
                    "tipo_acreedor": {
                        "codigo": "INSTF",
                        "valor": "Institución Financiera"
                    },
                    "tipo_adeudo": {
                        "codigo": "CVH",
                        "valor": "Compra de vehículo"
                    },
                    "identificador_deuda": "CONT12354",
                    "nacional_extranjero": {
                        "codigo": "MEX",
                        "valor": "México"
                    },
                    "identificador_acreedor": "PNBKSRIBAS S.A. DE C.V",
                    "rfc_acreedor": "PNKSD780710RH7",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "domicilio_acreedor": {
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
                    "fecha_adeudo": "2016-12-14",
                    "monto_original": 277900,
                    "tipo_moneda": {
                        "codigo" : "MXN",
                        "moneda" : "Pesos"
                    },
                    "tasa_interes": 12,
                    "saldo_pendiente": 28000,
                    "plazo_adeudo": 24,
                    "unidad_medida_adeudo": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "titularidad_deuda": {
                        "codigo": "DECL",
                        "valor": "Declarante"
                    },
                    "porcentaje_adeudo_titular": 100,
                    "garantia": random.choice([True, False]),
                    "observaciones": "xxxx"
                }
            ],
            "otras_obligaciones": [
                {
                    "id":1,
                    "titular": {
                        "id": 1,
                        "nombres": "Alma",
                        "primer_apellido" : "Rosales",
                        "segundo_apellido" : "Trueba"
                    },
                    "tipo_operacion": {
                        "codigo": "INCP",
                        "valor:": "Incorporación"
                    },
                    "tipo_acreedor": {
                        "codigo": "INSTF",
                        "valor": "Institución Financiera"
                    },
                    "tipo_obligacion":{
                        "codigo":"CHIP",
                        "valor":"Créditos Hipotecarios"
                    },
                    "identificador_obligacion":"FONAET8945",
                    "nacional_extranjero": {
                        "codigo": "MEX",
                        "valor": "México"
                    },
                    "identificador_acreedor":"INFONAVIT",
                    "rfc_acreedor":"NHJR89ASS5R5",
                    "sector_industria": {
                        "codigo": "SFS",
                        "valor": "Servicios financieros y seguros"
                    },
                    "domicilio_acreedor": {
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
                    "fecha_obligacion":"2018-03-14",
                    "monto_original":300000,
                    "tipo_moneda": {
                        "codigo" : "MXN",
                        "moneda" : "Pesos"
                    },
                    "tasa_interes":12,
                    "saldo_pendiente":297000,
                    "plazo_obligacion":360,
                    "unidad_medida_plazo":{
                        "codigo":"MESS",
                        "valor":"Meses"
                    },
                    "titularidad_obligacion": {
                        "codigo":"CONY",
                        "valor": "Conyuge"
                    },
                    "porcentaje_obligacion_titular": 100,
                    "garantia": random.choice([True, False]),
                    "observaciones": lorem_ipsum()
                }
            ]
        }

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
