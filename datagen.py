# data generator
import json
import argparse
#import sqlite3
from pymongo import MongoClient
from random_data import *
import os
from urllib.parse import quote_plus
# import urllib.request
# import git
# import os

parser = argparse.ArgumentParser(description='SESNA data generator')
parser.add_argument('-s', '--sys', default=0, type=int,
                    help='System number', choices=[1, 2, 3])
parser.add_argument('-n', '--samples', default=10,
                    type=int, help='Number of samples')
#parser.add_argument('-o','--out', default='JSON', help='Output format', choices= ['JSON', 'CSV'])
args = parser.parse_args()

sys_number = args.sys
number_of_samples = args.samples


host = os.environ.get('DATAGEN_MONGO_HOST', 'localhost')
port = os.environ.get('DATAGEN_MONGO_PORT', 27017)
user = os.environ.get('DATAGEN_MONGO_USER', None)
password = os.environ.get('DATAGEN_MONGO_PASS', None)
dbadmin = os.environ.get('DATAGEN_MONGO_DBADMIN', 'test')

uri = "mongodb://%s:%s" % (host, port)
if user is not None and password is not None:
    uri = "mongodb://%s:%s@%s:%s/%s" % (quote_plus(user),
                                        quote_plus(password), host, port, dbadmin)

print(uri)
client = MongoClient(uri)

db = client.datagen

if sys_number == 1:
    print('Sistema 1 -> Declaraciones ')

    collection = db.s1
    # samples = []

    # conn = sqlite3.connect('corpus.db')

    for x in range(0, number_of_samples):

        sample = dict()
        # informacion personal
        #sample['id'] = str(uuiduuid1())
        sample['metadata'] = {
            "actualizacion": '2018-10-01T00:00:00Z',
            "institucion": "Secretaria de la Administracion de Declaraciones",
            "contacto": "usuario@dominio.org",
            "persona_contacto": "José John",
            "diccionario": "https://diccionariomx/archivocsv"
        }

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
                "nom_agee": "México",
                "cve_agee": "15"
            },
            "curp": "BEML920313HMCLNS09",
            "rfc": "GOAP780710RH7",
            "fecha_nacimiento": get_bith_date(),
            "numero_identificacion_oficial": "a1b2c3d4",
            "correo_electronico": {
                "personal": get_email('abcmailcom'),
                "laboral": get_email('dependenciagobmx')
            },
            "telefono": {
                "particular": get_telephone('fijo'),
                "celular": get_telephone('celular')
            },
            "domicilio": get_address(),
            "estado_civil": {
                "codigo": "CAS",
                "valor": "Casado (a)"
            },
            "regimen_matrimonial": {
                "codigo": "SBI",
                "valor": "Separación de Bienes"
            },
            "fecha_declaracion": "2010-07-26"
        }

        sample['informacion_personal']['datos_curriculares'] = {
            "grado_maximo_escolaridad": {
                "codigo": "LICE",
                "valor": "Licenciatura"
              },
            "grados_academicos": [{
                "grado_obtenido": {
                    "codigo": "LICE",
                    "valor": "Licenciatura"
                  },
                "institucion_educativa": get_college(),
                "lugar_institucion_educativa": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad_federativa": {
                        "nom_agee": "México",
                        "cve_agee": "15"
                    },
                    "municipio": {
                      "nom_agem": "Ecatepec de Morelos",
                      "cve_agem": "033"
                    }
                },
                "carrera": get_degree(),
                "estatus": {
                    "codigo": "CURS",
                    "valor": "Cursando"
                },
                "ano_conclusion": 2005,
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
            "area_adscripcion": "Unidad de Politica Regulatoria",
            "fecha_posesion": get_bith_date(),
            "lugar_ubicacion": {
                "pais": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "entidad": {
                    "nom_agee": "México",
                    "cve_agee": "15"
                }
            },
            "direccion_encargo": {
                "pais": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "entidad_federativa": {
                    "nom_agee": "México",
                    "cve_agee": "15"
                },
                "municipio": {
                    "nom_agem": "Ecatepec de Morelos",
                    "cve_agem": "033"
                },
                "cp": "55018",
                "localidad": {
                    "nom_loc": "Ecatepec de Morelos",
                    "cve_loc": "0001"
                },
                "asentamiento": {
                  "cve_asen": 1,
                  "nom_asen": "AGUA CLARA",
                  "cve_tipo_asen": 16
                },
                "vialidad": {
                    "tipo_vial": "CALLE",
                    "nom_vial": "El Rosal"
                },
                "numExt": "24",
                "numInt": "48"
            },
            "telefono_laboral": {
                "numero": get_telephone('fijo'),
                "extension": 1020
            },
            "sector_industria": {
                "codigo": "SFS",
                "valor": "Servicios de salud y asistencia social"
            },
            "funciones_principales": [{
                "codigo": "ABI",
                "valor": "Administracion de bienes"
            }]
        }

        sample['informacion_personal']['experiencia_laboral'] = [
            {
                "ambito": {
                    "codigo": "PUB",
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
                "nombre_institucion": get_institution(),
                "unidad_administrativa": "Unidad de Politica Regulatoria",
                "direccion": get_address(),
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "jerarquia_rango": "string",
                "cargo_puesto": get_position(),
                "fecha_ingreso": get_bith_date(),
                "fecha_salida": get_bith_date(),
                "funciones_principales": [{
                    "codigo": "ABI",
                    "valor": "Administracion de bienes"
                }]
            }
        ]

        sample['informacion_personal']['dependientes_economicos'] = [
            {
                "nombre_personal": {
                    "nombres": get_name(),
                    "primer_apellido": get_last_name(),
                    "segundo_apellido": get_last_name()
                },
                "tipo_relacion": {
                    "codigo": "CONY",
                    "valor": "Conyuge"
                },
                "nacionalidades": [{
                    "valor": "México",
                    "codigo": "MX"
                }],
                "curp": "BEML920313HMCLNS09",
                "rfc": "GOAP780710RH7",
                "fecha_nacimiento": get_bith_date(),
                "numero_identificacion_nacional": "ABCD1234",
                "habita_domicilio_declarante": rand_bool(),
                "domicilio": get_address(),
                "medio_contacto": get_email('coldmailcom'),
                "ingresos_propios": True,
                "ocupacion_profesion": "Administrador de empresas",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "proveedor_contratista_gobierno": True,
                "tiene_intereses_mismo_sector_declarante": True,
                "desarrolla_cabildeo_sector_declarante": {
                    "respuesta": True,
                    "observaciones": "Esto es una observacion"
                },
                "beneficiario_programa_publico": [{
                    "nombre_programa": "Prospera",
                    "institucion_otorga_apoyo": get_institution(),
                    "tipo_apoyo": {
                      "codigo": "OBRA",
                      "valor": "Obra"
                    },
                    "valor_apoyo": 4000
                }],
                "observaciones": lorem_ipsum()
            }
        ]

        # Intereses
        sample['intereses'] = {
            "empresas_sociedades_asociaciones": [{
                "id": 123,
                "nombre_empresa_sociedad_asociacion": "DataIQ",
                "pais_registro": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "fecha_constitucion": get_bith_date(),
                "numero_registro": "ABC123",
                "rfc": "GOAP780710RH7",
                "domicilio": get_address(),
                "rol": "Dueño",
                "actividad_economica": True,
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "porcentaje_participacion": 70
            }],
            "membresias": [{
                "id": 123,
                "tipo_institucion": {
                    "codigo": "ASC",
                    "valor": "Asociaciones civiles"
                },
                "nombre_institucion": "Asociacion AC",
                "naturaleza_membresia": {
                  "codigo": "ASC",
                  "valor": "Asociacion Civil"
                },
                "domicilio": get_address(),
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "puesto_rol": "Titular",
                "fecha_inicio": get_bith_date(),
                "pagado": rand_bool(),
                "observaciones": lorem_ipsum()
            }],
            "apoyos_beneficios_publicos": [{
                "id": 123,
                "es_beneficiario": True,
                "programa": "Programa de Estimulos Economicos a Deportistas del Distrito Federal",
                "institucion_otorgante": "Instituto del Deporte del Distrito Federal ",
                "nivel_orden_gobierno": {
                    "codigo": "EST",
                    "valor": "Estatal"
                },
                "tipo_apoyo": {
                    "codigo": "SERV",
                    "valor": "Servicio"
                },
                "valor_anual_apoyo": 7500,
                "observaciones": lorem_ipsum()
            }],
            "representacion_activa": [{
                "id": 123,
                "tipo_representacion": {
                    "codigo": "APOD",
                    "valor": "Apoderado"
                },
                "nombre_parte_representada": "Cecilia Gomez Urrutia",
                "curp_parte": "BEML920313HMCLNS09",
                "rfc_parte": "GOAP780710RH7",
                "fecha_nacimiento_parte": get_bith_date(),
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_inicio": get_bith_date(),
                "pagado": rand_bool(),
                "observaciones": lorem_ipsum()
            }],
            "representacion_pasiva": [{
                "id": 123,
                "tipo_representacion": {
                    "codigo": "APOD",
                    "valor": "Apoderado"
                },
                "nombre": "Augusto Fernandez Castro",
                "fecha_inicio_representacion": get_bith_date(),
                "nacionalidades": [{
                    "valor": "México",
                    "codigo": "MX"
                }],
                "curp": "BEML920313HMCLNS09",
                "rfc": "GOAP780710RH7",
                "fecha_nacimiento": get_bith_date(),
                "tiene_intereses": rand_bool(),
                "ocupacion_profesion": "Contador",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "observaciones": lorem_ipsum()
            }],
            "socios_comerciales": [{
                "id": 123,
                "nombre_actividad": "Actividad",
                "tipo_vinculo": "Socio",
                "antiguedad_vinculo": 20,
                "rfc_entidad": "GOAP780710RH7",
                "nombre": "Armando Rodriguez Saes",
                "curp": "BEML920313HMCLNS09",
                "rfc": "GOAP780710RH7",
                "lugar_nacimiento": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad": {
                        "nom_agee": "México",
                        "cve_agee": "15"
                    }
                },
                "fecha_nacimiento": get_bith_date(),
                "porcentaje_participacion": 70,
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "observaciones": lorem_ipsum()
            }],
            "clientes_principales": [{
                "id": 123,
                "nombre_negocio": "Nombre negocio",
                "numero_registro": "HTC896DSFA",
                "dueno_encargado": "Salvador Hernandez Torres",
                "nombre": "AMEXSA",
                "rfc": "GOAP780710RH7",
                "domicilio": get_address(),
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "porcentaje_participacion": 70,
                "observaciones": lorem_ipsum()
            }],
            "otras_partes": [{
                "id": 123,
                "tipo_relacion": {
                    "codigo": "GPR",
                    "valor": "Garantes de Préstamos Recibidos"
                },
                "nombre_denominacion_parte": "Sergio Rodriguez",
                "fecha_inicio_relacion": get_bith_date(),
                "nacionalidades": [{
                    "valor": "México",
                    "codigo": "MX"
                }],
                "curp": "BEML920313HMCLNS09",
                "rfc": "GOAP780710RH7",
                "fecha_nacimiento": get_bith_date(),
                "ocupacion": "Administrador de empresas",
                "tiene_interes": True,
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "observaciones": lorem_ipsum()
            }],
            "beneficios_gratuitos": [{
                "id": 123,
                "tipo_beneficio": "Tarjetas o monederos electronicos",
                "origen_beneficio": "Prestacion laboral",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "valor_beneficio": 1256,
                "observaciones": lorem_ipsum()
            }]
        }

        # Ingresos
        sample['ingresos'] = {
            "sueldos_salarios_publicos": [{
                "id": 123,
                "ente_publico": {
                  "valor": "SECRETARIA DE GOBERNACION",
                  "codigo": "SEGOB"
                },
                "rfc": "GOAP780710RH7",
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "sueldos_salarios_otros_empleos": [{
                "id": 123,
                "nombre_denominacion_razon_social": "Max Power Inc",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_actividad_servicio": lorem_ipsum(),
                "domicilio_persona_paga": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "actividad_profesional": [{
                "id": 123,
                "nombre_denominacion_razon_social": "Nombre",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_actividad_servicio": lorem_ipsum(),
                "domicilio_persona_paga": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "actividad_empresarial": [{
                "id": 123,
                "nombre_denominacion_razon_social": "Empresa SA",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_actividad_servicio": lorem_ipsum(),
                "domicilio_actividad_empresarial": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": "Esto es una observacion"
            }],
            "actividad_economica_menor": [{
                "id": 123,
                "nombre_denominacion_razon_social": "Nombre",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_actividad_servicio": "Descripcion del servicio",
                "domicilio_actividad": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "arrendamiento": [{
                "id": 123,
                "nombre_denominacion_razon_social": "ABC Inc",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_actividad_servicio": "Descripcion del servicio",
                "domicilio_actividad": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "intereses": [{
                "id": 123,
                "nombre_denominacion_razon_social": "BANC SA",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_actividad_servicio": lorem_ipsum(),
                "domicilio": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "premios": [{
                "id": 123,
                "nombre_denominacion": "Loteria Nacional",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_premio": lorem_ipsum(),
                "domicilio": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "enajenacion_bienes": [{
                "id": 123,
                "nombre_denominacion": "Loteria Nacional",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "tipo_bien": {
                  "codigo": "BAR",
                  "valor": "Barco"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_bien": lorem_ipsum(),
                "domicilio_bien_enajenado": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "otros_ingresos": [{
                "id": 123,
                "nombre_denominacion": "Centro Educativo",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad": {
                    "codigo": "SAL",
                    "valor": "Salud"
                },
                "descripcion_actividad": lorem_ipsum(),
                "domicilio_actividad": get_address(),
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }]
        }

        # Activos
        sample['activos'] = {
            "bienes_inmuebles": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "tipo_bien": {
                    "codigo": "DPT",
                    "valor": "Departamento"
                },
                "superficie_terreno": 300,
                "superficie_construccion": 100,
                "titular": {
                  "codigo": "DECL",
                  "valor": "Declarante"
                },
                "porcentaje_propiedad": 70,
                "nombre_copropietario": {
                    "nombres": "Carlos",
                    "primer_apellido": "Perez",
                    "segundo_apellido": "Sanchez"
                },
                "identificacion_bien": {
                    "numero_escritura_publica": 202020,
                    "numero_registro_publico": 404040,
                    "folio_real": "jsjs74747",
                    "fecha_contrato": "2010-07-26"
                },
                "domicilio_bien": get_address(),
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesion"
                },
                "nombre_denominacion_quien_adquirio": "Monster Inc",
                "rfc_quien_adquirio": "GOAP780710RH7",
                "curp_quien_adquirio": "BEML920313HMCLNS09",
                "relacion_persona_adquirio": {
                    "codigo": "CONY",
                    "valor": "Conyuge"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_adquisicion": get_bith_date(),
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    }
                },
                "valor_catastral": 800,
                "observaciones": "Esto es una observacion"
            }],
            "bienes_muebles_registrables": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "tipo_bien_mueble": {
                    "codigo": "VEH",
                    "valor": "Vehiculo"
                },
                "marca": "NISSAN",
                "submarca": "RS-122234",
                "modelo": 2018,
                "numero_serie": "6545243-4334",
                "lugar_registro": {
                    "pais": {
                        "valor": "MEXICO",
                        "codigo": "MX"
                    },
                    "entidad": {
                        "nom_agee": "MEXICO",
                        "cve_agee": "15"
                    }
                },
                "titular_bien": {
                    "codigo": "DECL",
                    "valor": "Declarante"
                },
                "porcentaje_propiedad": 70,
                "nombres_copropietarios": [
                    "Monstr Inc"
                ],
                "numero_registro_vehicular": 455000,
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesion"
                },
                "nombre_denominacion_adquirio": "Monstr Inc",
                "rfc_quien_adquirio": "GOAP780710RH7",
                "relacion_persona_quien_adquirio": {
                    "codigo": "CONY",
                    "valor": "Conyuge"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_adquisicion": get_bith_date(),
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    }
                },
                "observaciones": lorem_ipsum()
            }],
            "bienes_muebles_no_registrables": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "tipo_bien": {
                    "codigo": "VEH",
                    "valor": "Vehiculo"
                },
                "descripcion": "Con descripcion",
                "titular_bien": {
                    "codigo": "DECL",
                    "valor": "Declarante"
                },
                "porcentaje_propiedad": 70,
                "nombres_copropietarios": [
                    "Monstr Inc"
                ],
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesion"
                },
                "nombre_denominacion_adquirio": "Tesl Mtr Inc",
                "relacion_quien_adquirio": {
                    "codigo": "CONY",
                    "valor": "Conyuge"
                },
                "fecha_adquisicion": get_bith_date(),
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    }
                },
                "observaciones": "Esto es una observacion"
            }],
            "inversiones_cuentas_valores": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "tipo_inversion": {
                    "codigo": "VALS",
                    "valor": "Valores"
                },
                "tipo_especifico_inversion": {
                    "codigo": "VALRS",
                    "valor": "Valores"
                },
                "numero_cuenta": "GFHRTY788778",
                "nacional_extranjero": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "nombre_institucion": "Bank Inkc",
                "rfc_institucion": "GOAP780710RH7",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "domicilio_institucion": get_address(),
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesion"
                },
                "fecha_inicio": get_bith_date(),
                "monto_original": get_amount(80000, 100000),
                "tipo_moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                },
                "tasa_interes": 10,
                "saldo_anual": 5000,
                "plazo": 6,
                "unidad_medida_plazo": {
                    "codigo": "MESS",
                    "valor": "Meses"
                },
                "titular_bien": {
                    "codigo": "DECL",
                    "valor": "Declarante"
                },
                "porcentaje_inversion": 70,
                "observaciones": lorem_ipsum()
            }],
            "efectivo_metales": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "tipo_moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                },
                "monto_moneda": get_amount(70000, 100000),
                "tipo_metal": {
                    "codigo": "ORO",
                    "valor": "Oro"
                },
                "unidades": 100,
                "monto_metal": get_amount(70000, 100000),
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesion"
                },
                "observaciones_comentarios": lorem_ipsum()
            }],
            "fideicomisos": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "identificador_fideicomiso": "93232",
                "tipo_fideicomiso": {
                    "codigo": "GARNT",
                    "valor": "Garantia"
                },
                "objetivo": "Objetivo del fideicomiso",
                "numero_registro": "788544abc",
                "fecha_creacion": get_bith_date(),
                "vigencia": get_bith_date(),
                "residencia": {
                    "valor": "MEXICO",
                    "codigo": "MX"
                },
                "valor": 78555555,
                "moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                },
                "porcentaje_propiedad_derechos_fiduciarios": 70,
                "ingreso_monetario_obtenido": 56666,
                "institucion_fiduciaria": "Banco de México",
                "fideicomitente": {
                  "nombre": "Banco Robmen1",
                  "rfc": "GOAP780710RH7",
                  "curp": "BEML920313HMCLNS09",
                  "domicilio": get_address(),
                  "fecha_constitucion": "2010-07-26"
                },
                "fideicomisario": {
                  "nombre": "Banco Robmen1",
                  "rfc": "GOAP780710RH7",
                  "curp": "BEML920313HMCLNS09",
                  "domicilio": get_address(),
                  "fecha_constitucion": "2010-07-26"
                },
                "fiduciario": {
                  "nombre": "Banco Robmen1",
                  "rfc": "GOAP780710RH7",
                  "curp": "BEML920313HMCLNS09",
                  "domicilio": get_address(),
                  "fecha_constitucion": "2010-07-26"
                },
                "observaciones": lorem_ipsum()
            }],
            "bienes_intangibles": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "propietario_registrado": ["Sergio Perez"],
                "descripcion": lorem_ipsum(),
                "ente_publico_encargado": get_institution(),
                "numero_registro": 754444,
                "fecha_registro": get_bith_date(),
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    }
                },
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesion"
                },
                "fecha_vencimiento": get_bith_date(),
                "porcentaje_copropiedad": 70,
                "precio_total_copropiedad": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    }
                },
                "nombre_copropietario": "Vien Incorporation",
                "porcentaje_propiedad_copropietario": 70,
                "observaciones": lorem_ipsum()
            }],
            "cuentas_por_cobrar": [{
                "id": 123,
                "nombre_prestatario": "Max Power Tier",
                "numero_registro": "488755avvv",
                "domicilio_prestatarios": get_address(),
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_prestamo": get_bith_date(),
                "monto_original_prestamo": get_amount(70000, 100000),
                "tasa_interes": 1001,
                "saldo_pendiente": 4555,
                "fecha_vencimiento": get_bith_date(),
                "porcentaje_copropiedad": 70,
                "nombre_copropietario": "Max Power Bansky",
                "observaciones": lorem_ipsum()
            }],
            "uso_especie_propiedad_tercero": [{
                "id": 123,
                "tipo_bien": "Bien Inmueble",
                "valor_mercado": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "MXN"
                    }
                },
                "nombre_tercero_propietario": "Bansky Von Trier",
                "rfc_tercero_propietario": "GOAP780710RH7",
                "curp_tercero_propietario": "BEML920313HMCLNS09",
                "relacion_persona": {
                    "codigo": "CONY",
                    "valor": "Conyuge"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_inicio": get_bith_date(),
                "domicilio_persona": get_address(),
                "observaciones": lorem_ipsum()
            }]
        }

        # Pasivos
        sample['pasivos'] = {
            "deudas": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "tipo_acreedor": {
                    "codigo": "INSTF",
                    "valor": "Institucion Financiera"
                },
                "tipo_adeudo": {
                      "codigo": "CH",
                      "valor": "Crédito hipotecario"
                },
                "identificador_deuda": "CONT12354",
                "nacional_extranjero": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "nombre_acreedor": "PNBKSRIBAS SA DE CV",
                "rfc_acreedor": "GOAP780710RH7",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "domicilio_acreedor": get_address(),
                "fecha_adeudo": get_bith_date(),
                "monto_original": get_amount(70000, 100000),
                "tipo_moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                },
                "tasa_interes": 12,
                "saldo_pendiente": 28000,
                "montos_abonados": [
                    get_amount(7000, 10000)
                ],
                "plazo_adeudo": 24,
                "unidad_medida_adeudo": {
                    "codigo": "MESS",
                    "valor": "Meses"
                },
                "titularidad_deuda": {
                    "codigo": "DECL",
                    "valor": "Declarante"
                },
                "porcentaje_adeudo_titular": 70,
                "garantia": rand_bool(),
                "nombre_garante": "Bansky Von Tier",
                "observaciones": "Esto es una observacion"
            }],
            "otras_obligaciones": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporacion"
                },
                "tipo_acreedor": {
                    "codigo": "INSTF",
                    "valor": "Institucion Financiera"
                },
                "tipo_obligacion": {
                  "codigo": "CVH",
                  "valor": "Compra de vehiculo"
                },
                "identificador_obligacion": "FONAET8945",
                "nacional_extranjero": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "nombre_acreedor": "Bansky Hola Adios",
                "rfc_acreedor": "GOAP780710RH7",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "domicilio_acreedor": get_address(),
                "fecha_obligacion": get_bith_date(),
                "monto_original": get_amount(40000, 500000),
                "tipo_moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                },
                "tasa_interes": 12,
                "saldo_pendiente": 297000,
                "montos_abonados": [
                    28000
                ],
                "plazo_obligacion": 360,
                "unidad_medida_plazo": {
                    "codigo": "MESS",
                    "valor": "Meses"
                },
                "titularidad_obligacion": {
                    "codigo": "DECL",
                    "valor": "Declarante"
                },
                "porcentaje_obligacion_titular": 70,
                "garantia": rand_bool(),
                "nombre_garante": "Banksy Von Tier",
                "observaciones": lorem_ipsum()
            }]
        }

        collection.insert_one(sample)
        #samples.append(sample)

    #with open('data.json', 'w') as outfile:
    #    json.dump(samples,outfile, indent=4)


#conn.close()
elif sys_number == 1:
    print('Sistema 2 -> Servidores públicos que intervienen en contrataciones')
elif sys_number == 2:
    print('Sistema 3 -> Servidores públicos y particulares sancionados')
else:
    parser.print_help()
