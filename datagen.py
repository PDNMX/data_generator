# data generator
import json
import argparse
#import sqlite3
from pymongo import MongoClient
from random_data import *
import os

parser = argparse.ArgumentParser(description='SESNA data generator')
parser.add_argument('-s','--sys', default=0, type=int,  help='System number', choices=[1, 2, 3])
parser.add_argument('-n', '--samples', default=10, type=int, help='Number of samples')
#parser.add_argument('-o','--out', default='JSON', help='Output format', choices= ['JSON', 'CSV'])
args = parser.parse_args()

sys_number = args.sys
number_of_samples = args.samples


host = os.environ.get('DATAGEN_MONGO_HOST', 'localhost')
port = os.environ.get('DATAGEN_MONGO_PORT', 27017)
user = os.environ.get('DATAGEN_MONGO_USER', None)
password = os.environ.get('DATAGEN_MONGO_PASS', None)

uri = "mongodb://%s:%s" % (host, port)
if user is not None and password is not None:
    uri = "mongodb://%s@%s:%s" % ((user+":"+password), host, port)

client = MongoClient(uri)

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
        #sample['id'] = str(uuid.uuid1())
        sample['metadatos'] = {
            "fecha_actualizacion": '2018-10-01T:00:00:00Z',
            "institucion_responsable": "Secretaría de la Administración de Declaraciones",
            "contacto": "declaraciones@sad.mx"
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
                "nom_ent": "México",
                "cve_ent": "15"
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
                    "cve_ent": "15"
                },
                "municipio": {
                    "nom_mun": "Ecatepec de Morelos",
                    "cve_mun": "27"
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
                "numExt": "24",
                "numInt": "48"
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
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad":{
                        "nom_ent": "México",
                        "cve_ent": "15"
                    }
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
                "pais": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "entidad": {
                    "nom_ent": "México",
                    "cve_ent": "15"
                }
            },
            "direccion_encargo": {
                "pais": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "entidad_federativa": {
                    "nom_ent": "México",
                    "cve_ent": "15"
                },
                "municipio": {
                    "nom_mun": "Ecatepec de Morelos",
                    "cve_mun": "27"
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
                "numExt": "24",
                "numInt": "48"
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
                "nombre_institucion": get_institution(),
                "unidad_administrativa": "Unidad de Política Regulatoria",
                "direccion": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad_federativa": {
                        "nom_ent": "México",
                        "cve_ent": "15"
                    },
                    "municipio": {
                        "nom_mun": "Ecatepec de Morelos",
                        "cve_mun": "27"
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "jerarquia_rango": "string",
                "cargo_puesto": get_position(),
                "fecha_ingreso": "31/07/1980",
                "fecha_salida": "31/07/1990",
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
                "habita_domicilio_declarante": rand_bool(),
                "domicilio": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad_federativa": {
                        "nom_ent": "México",
                        "cve_ent": "15"
                    },
                    "municipio": {
                        "nom_mun": "Ecatepec de Morelos",
                        "cve_mun": "27"
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
                    "numExt": "24",
                    "numInt": "48"
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
            "empresas_sociedades_asociaciones": [{
                "id": 123,
                "nombre_empresa_sociedad_asociacion": "DataIQ",
                "pais_registro": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "fecha_constitucion": "31/07/1980",
                "numero_registro": "ABC123",
                "rfc": "GOAP780710RH7",
                "domicilio": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
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
                "nombre_institucion": "Asociacion A.C",
                "naturaleza_membresia": "Civil",
                "domicilio": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "puesto_rol": "Titular",
                "fecha_inicio": "31/07/1980",
                "pagado": rand_bool(),
                "observaciones": lorem_ipsum()
            }],
            "apoyos_beneficios_publicos": [{
                "id": 123,
                "es_beneficiario": True,
                "programa": "Programa de Estímulos Económicos a Deportistas del Distrito Federal",
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
                "nombre_parte_representada": "Cecilia Gómez Urrutia",
                "curp_parte": "BEML920313HMCLNS09",
                "rfc_parte": "GOAP780710RH7",
                "fecha_nacimiento_parte": "31/07/1980",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_inicio": "31/07/1980",
                "pagado": rand_bool(),
                "observaciones": lorem_ipsum()
            }],
            "representacion_pasiva": [{
                "id": 123,
                "tipo_representacion": {
                    "codigo": "APOD",
                    "valor": "Apoderado"
                },
                "nombre_representante": "Augusto Fernández Castro",
                "fecha_inicio_representacion": "31/07/1980",
                "nacionalidades_representante": [{
                    "valor": "México",
                    "codigo": "MX"
                }],
                "curp_representante": "BEML920313HMCLNS09",
                "rfc_representante": "GOAP780710RH7",
                "fecha_nacimiento_representante": "31/07/1980",
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
                "nombre_socio": "Armando Rodríguez Saes",
                "curp_socio": "BEML920313HMCLNS09",
                "rfc_socio": "GOAP780710RH7",
                "lugar_nacimiento_socio": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad": {
                        "nom_ent": "México",
                        "cve_ent": "15"
                    }
                },
                "fecha_nacimiento_socio": "31/07/1980",
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
                "numero_Registro": "HTC896DSFA",
                "dueño_encargado": "Salvador Hernández Torres",
                "nombre_cliente": "AMEX.S.A.",
                "rfc_cliente": "GOAP780710RH7",
                "domicilio_cliente": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "porcentaje_facturacion": 70,
                "observaciones": lorem_ipsum()
            }],
            "otras_partes": [{
                "id": 123,
                "tipo_relacion": {
                    "codigo": "GPR",
                    "valor": "Garantes de Préstamos Recibidos"
                },
                "nombre_denominacion_parte": "Sergio Rodríguez",
                "fecha_inicio_relacion": "31/07/1980",
                "nacionalidad": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "curp": "BEML920313HMCLNS09",
                "rfc": "GOAP780710RH7",
                "fecha_nacimiento": "31/07/1980",
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
                "tipo_beneficio": {
                    "codigo": "TARJ",
                    "valor": "Tarjetas o monederos electrónicos"
                },
                "origen_beneficio": "Prestación laboral",
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
                "ente_publico": get_institution(),
                "rfc": "GOAP780710RH7",
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
                },
                "observaciones": lorem_ipsum()
            }],
            "sueldos_salarios_otros_empleos": [{
                "id": 123,
                "nombre_denominacion_razon_social": "Max Power Inc.",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_actividad_servicio": lorem_ipsum(),
                "domicilio_persona_recibe_ingreso": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
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
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_actividad_servicio": lorem_ipsum(),
                "domicilio_persona_recibe_ingreso": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
                },
                "observaciones": lorem_ipsum()
            }],
            "actividad_empresarial": [{
                "id": 123,
                "nombre_denominacion_razon_social": "Empresa S.A.",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_actividad_servicio": lorem_ipsum(),
                "domicilio_actividad_empresarial": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
                },
                "observaciones": "Esto es una observación"
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
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_actividad_servicio": "Descripción del servicio",
                "domicilio_actividad": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
                },
                "observaciones": lorem_ipsum()
            }],
            "arrendamiento": [{
                "id": 123,
                "nombre_denominacion_razon_social": "ABC Inc.",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_actividad_servicio": "Descripción del servicio",
                "domicilio_actividad": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
                },
                "observaciones": lorem_ipsum()
            }],
            "intereses": [{
                "id": 123,
                "nombre_denominacion_razon_social": "BANC S.A.",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_actividad_servicio": lorem_ipsum(),
                "domicilio": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
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
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_actividad": lorem_ipsum(),
                "domicilio": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
                },
                "observaciones": lorem_ipsum()
            }],
            "enajenacion_bienes": [{
                "id": 123,
                "nombre_denominacion": "Loteria Nacional",
                "rfc": "GOAP780710RH7",
                "curp": "BEML920313HMCLNS09",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "tipo_actividad_servicio": {
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_bien": lorem_ipsum(),
                "domicilio_bien_enajenado": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
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
                    "codigo": "SPU",
                    "valor": "Sector público"
                },
                "descripcion_actividad": lorem_ipsum(),
                "domicilio_actividad": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "ingreso_bruto_anual": {
                    "valor": 10000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    },
                    "unidad_temporal": {
                        "codigo": "MESS",
                        "valor": "Meses"
                    },
                    "duracion_frecuencia": 10,
                    "fecha_transaccion": "31/07/1980"
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
                    "valor": "Incorporación"
                },
                "tipo_bien": {
                    "codigo": "VEH",
                    "valor": "Vehículo"
                },
                "superficie_terreno": 300,
                "superficie_construccion": 100,
                "porcentaje_propiedad": 70,
                "nombre_copropietario": {
                    "nombres": "Carlos",
                    "primer_apellido": "Pérez",
                    "segundo_apellido": "López"
                },
                "identificacion_bien": {
                    "numero_escritura_publica": 202020,
                    "numero_registro_publico": 404040,
                    "folio_real": "jsjs74747",
                    "fecha_contrato": "31/07/1980"
                },
                "domicilio_bien": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesión"
                },
                "nombre_denominacion_quien_adquirio": "Monster Inc.",
                "rfc_quien_adquirio": "GOAP780710RH7",
                "curp_quien_adquirio": "BEML920313HMCLNS09",
                "relacion_persona_adquirio": {
                    "codigo": "CONY",
                    "valor": "Cónyuge"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_adquisicion": "31/07/1980",
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    }
                },
                "valor_catastral": 800,
                "observaciones": "Esto es una observación"
            }],
            "bienes_muebles_registrables": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporación"
                },
                "tipo_bien_mueble": {
                    "codigo": "VEH",
                    "valor": "Vehículo"
                },
                "marca": "NISSAN",
                "submarca": "RS-122234",
                "modelo": 2018,
                "numero_serie": "6545243-4334",
                "lugar_registro": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
                    "entidad": {
                        "nom_ent": "México",
                        "cve_ent": "15"
                    }
                },
                "titular_bien": {
                    "codigo": "DECL",
                    "valor": "Declarante"
                },
                "porcentaje_propiedad": 70,
                "nombres_copropietarios": [
                    "Monstr Inc."
                ],
                "numero_registro_vehicular": 455000,
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesión"
                },
                "nombre_denominacion_adquirio": "Monstr Inc.",
                "rfc_quien_adquirio": "GOAP780710RH7",
                "relacion_persona_quien_adquirio": {
                    "codigo": "CONY",
                    "valor": "Cónyuge"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_adquisicion": "31/07/1980",
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    }
                },
                "observaciones": "Esto es una observación"
            }],
            "bienes_muebles_no_registrables": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporación"
                },
                "tipo_bien": {
                    "codigo": "VEH",
                    "valor": "Vehículo"
                },
                "descripcion": "Con descripción",
                "titular_bien": {
                    "codigo": "DECL",
                    "valor": "Declarante"
                },
                "porcentaje_propiedad": 70,
                "nombres_copropietarios": [
                    "Monstr Inc."
                ],
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesión"
                },
                "nombre_denominacion_adquirio": "Tesl Mtr Inc.",
                "relacion_quien_adquirio": {
                    "codigo": "CONY",
                    "valor": "Cónyuge"
                },
                "fecha_adquisicion": "31/07/1980",
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    }
                },
                "observaciones": "Esto es una observación"
            }],
            "inversiones_cuentas_valores": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporación"
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
                "domicilio_institucion": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesión"
                },
                "fecha_inicio": "31/07/1980",
                "monto_original": 80000,
                "tipo_moneda": {
                    "codigo": "MXN",
                    "moneda": "Peso mexicano"
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
                    "valor": "Incorporación"
                },
                "tipo_moneda": {
                    "codigo": "MXN",
                    "moneda": "Peso mexicano"
                },
                "monto": 78555,
                "tipo_metal": {
                    "codigo": "ORO",
                    "valor": "Oro"
                },
                "unidades": 100,
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesión"
                },
                "observaciones_comentarios": lorem_ipsum()
            }],
            "fideicomisos": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporación"
                },
                "identificador_fideicomiso": "93232",
                "tipo_fideicomiso": {
                    "codigo": "GARNT",
                    "valor": "Garantía"
                },
                "objetivo": "Objetivo del fideicomiso",
                "numero_registro": "788544abc",
                "fecha_creacion": "31/07/1980",
                "vigencia": "31/07/1980",
                "residencia": {
                    "valor": "México",
                    "codigo": "MX"
                },
                "valor": 78555555,
                "moneda": {
                    "codigo": "MXN",
                    "moneda": "Peso mexicano"
                },
                "porcentaje_propiedad_derechos_fiduciarios": 70,
                "ingreso_monetario_obtenido": 56666,
                "institucion_fiduciaria": "Banco de México",
                "nombre_fideicomitente": "Banco Robmen1",
                "nombre_fideicomisario": "Banco Robmen2",
                "nombre_fiduciario": "Banco Robmenos2",
                "rfc_fideicomitente": "GOAP780710RH7",
                "rfc_fideicomsario": "GOAP780710RH7",
                "rfc_fiduciario": "GOAP780710RH7",
                "curp_fideicomitente": "BEML920313HMCLNS09",
                "curp_fideicomisario": "BEML920313HMCLNS09",
                "curp_fiduciario": "BEML920313HMCLNS09",
                "domicilio_fideicomitente": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "domicilio_fideicomisario": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "domicilio_fiduciario": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "fecha_nacimiento_constitucion_fideicomitente": "31/07/1980",
                "fecha_nacimiento_constitucion_fideicomisario": "31/07/1980",
                "fecha_nacimiento_constitucion_fiduciario": "31/07/1980",
                "observaciones": lorem_ipsum()
            }],
            "bienes_intangibles": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporación"
                },
                "propietario_registrado": "Sergio Perez",
                "descripcion": lorem_ipsum(),
                "ente_publico_encargado": {
                    "nombres": "Carlos",
                    "primer_apellido": "Pérez",
                    "segundo_apellido": "López"
                },
                "numero_registro": 754444,
                "fecha_registro": "31/07/1980",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "precio_adquisicion": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    }
                },
                "forma_adquisicion": {
                    "codigo": "CES",
                    "valor": "Cesión"
                },
                "fecha_vencimiento": "31/07/1980",
                "porcentaje_copropiedad": 70,
                "precio_total_copropiedad": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    }
                },
                "nombre_copropietario": "Vien Inc,",
                "porcentaje_propiedad_copropietario": 70,
                "observaciones": lorem_ipsum()
            }],
            "cuentas_por_cobrar": [{
                "id": 123,
                "nombre_prestatario": "Max Power Tier",
                "numero_registro": "488755avvv",
                "domicilio_prestatarios": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_prestamo": "31/07/1980",
                "monto_original_prestamo": 488844,
                "tasa_interes": 10.01,
                "saldo_pendiente": 4555,
                "fecha_vencimiento": "31/07/1980",
                "porcentaje_copropiedad": 70,
                "nombre_copropietario": "Max Power Bansky",
                "observaciones": lorem_ipsum()
            }],
            "uso_especie_propiedad_tercero": [{
                "id": 123,
                "tipo_bien": {
                    "codigo": "VEH",
                    "valor": "Vehículo"
                },
                "valor_mercado": {
                    "valor": 4000,
                    "moneda": {
                        "codigo": "MXN",
                        "moneda": "Peso mexicano"
                    }
                },
                "nombre_tercero_propietario": "Bansky Von Trier",
                "rfc_tercero_propietario": "GOAP780710RH7",
                "curp_tercero_propietario": "BEML920313HMCLNS09",
                "relacion_persona": {
                    "codigo": "CONY",
                    "valor": "Cónyuge"
                },
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "fecha_inicio": "31/07/1980",
                "domicilio_persona": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "observaciones": lorem_ipsum()
            }]
        }

        # Pasivos
        sample['pasivos'] = {
            "deudas": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporación"
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
                    "valor": "México",
                    "codigo": "MX"
                },
                "nombre_acreedor": "PNBKSRIBAS S.A. DE C.V",
                "rfc_acreedor": "GOAP780710RH7",
                "sector_industria": {
                    "codigo": "SFS",
                    "valor": "Servicios de salud y asistencia social"
                },
                "domicilio_acreedor": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "fecha_adeudo": "31/07/1980",
                "monto_original": 277900,
                "tipo_moneda": {
                    "codigo": "MXN",
                    "moneda": "Peso mexicano"
                },
                "tasa_interes": 12,
                "saldo_pendiente": 28000,
                "montos_abonados": [
                    28000
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
                "observaciones": "Esto es una observación"
            }],
            "otras_obligaciones": [{
                "id": 123,
                "tipo_operacion": {
                    "codigo": "INCP",
                    "valor": "Incorporación"
                },
                "tipo_acreedor": {
                    "codigo": "INSTF",
                    "valor": "Institución Financiera"
                },
                "tipo_obligacion": "Ejemplo",
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
                "domicilio_acreedor": {
                    "pais": {
                        "valor": "México",
                        "codigo": "MX"
                    },
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
                    "numExt": "24",
                    "numInt": "48"
                },
                "fecha_obligacion": "31/07/1980",
                "monto_original": 300000,
                "tipo_moneda": {
                    "codigo": "MXN",
                    "moneda": "Peso mexicano"
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
                "observaciones": lorem_ipsum()
            }]
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
