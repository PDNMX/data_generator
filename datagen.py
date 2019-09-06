import random
import json
import argparse
from pymongo import MongoClient
from random_data import *
import os
from urllib.parse import quote_plus
from utilFechas import *
from funGradosAcademicos import *

# import urllib.request
# import git
# import os
random.seed()
parser = argparse.ArgumentParser(description='SESNA data generator')
parser.add_argument('-s', '--sys', default=0, type=int,
                    help='System number', choices=[1, 2, 3])
parser.add_argument('-n', '--samples', default=10,
                    type=int, help='Number of samples')
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
    collection.drop()
    # samples = []

    # conn = sqlite3.connect('corpus.db')

    for x in range(0, number_of_samples):
        sample = dict()

        _institucion = getInstitucion()

        # informacion personal
        # sample['id'] = str(uuiduuid1())
        sample['metadata'] = {
            "actualizacion": getUTCDate(),
            "institucion": _institucion,
            "contacto": "usuario@dominio.org",
            "persona_contacto": get_full_name(),
            "diccionario": "https://diccionariomx/archivocsv"
        }

        sample['informacion_personal'] = {}

        sample['informacion_personal']['informacion_general'] = {
            "nombres": get_name(),
            "primer_apellido": get_last_name(),
            "segundo_apellido": get_last_name(),
            "nacionalidades": citizenship(),
            "pais_nacimiento": {"valor": "México", "codigo": "MX"},
            "entidad_federativa_nacimiento": get_entidad(),
            "curp": get_curp(),
            "rfc": get_rfc(),
            "fecha_nacimiento": getFechaNacimiento(),
            "numero_identificacion_oficial": get_identificacion(),
            "correo_electronico": {"personal": get_email('abcmail.com'), "laboral": get_email('dependencia.gob.mx')},
            "telefono": {"particular": get_telephone('fijo'), "celular": get_telephone('celular')},
            "domicilio": get_address(),
            "estado_civil": random.choice(cat_estado_civil),
            "regimen_matrimonial": random.choice(cat_regimen_matrimonial),
            "fecha_declaracion": getFecha()
        }

        gradosAcademicos = getGradosAcademicos()
        sample['informacion_personal']['datos_curriculares'] = {
            "grado_maximo_escolaridad": gradosAcademicos[0]["grado_obtenido"],
            "grados_academicos": gradosAcademicos
        }

        sample['informacion_personal']['datos_encargo_actual'] = {
            "ente_publico": _institucion,
            "empleo_cargo_comision": get_position(),
            "nivel_gobierno": getNivelGobierno(),
            "poder_juridico": getPoder(),
            "contratado_honorarios": rand_bool(),
            "nivel_encargo": "{}00{}".format(getMayusculas(2), getNumeros(2)),
            "area_adscripcion": "Unidad de Politica Regulatoria",
            "fecha_posesion": getFecha(),
            "lugar_ubicacion": {"pais": {"valor": "MEXICO", "codigo": "MX"}, "entidad": get_entidad()},
            "direccion_encargo": get_address(),
            "telefono_laboral": {"numero": get_telephone('fijo'), "extension": int(getNumeros(4))},
            "sector_industria": getSectorIndustria(),
            "funciones_principales": getFuncionesPrincipales()
        }

        sample['informacion_personal']['experiencia_laboral'] = getExperienciasLaborales()

        sample['informacion_personal']['dependientes_economicos'] = getDependientesEconomicos()

        # Intereses
        sample['intereses'] = {
            "empresas_sociedades_asociaciones": getEmpresas(),
            "membresias": getMembresias(),
            "apoyos_beneficios_publicos": getApoyos(),
            "representacion_activa": getRepresentacionActiva(),
            "representacion_pasiva": getRepresentacionPasiva(),
            "socios_comerciales": getSociosComerciales(),
            "clientes_principales": getClientesPrincipales(),
            "otras_partes": getOtrasPartes(),
            "beneficios_gratuitos": getBeneficiosGratuitos()
        }

        # Ingresos
        sample['ingresos'] = getIngresos()

        # Activos
        sample['activos'] = {
            "bienes_inmuebles": getBienesInmuebles(),
            "bienes_muebles_registrables": getBienMuebleRegistrable(),
            "bienes_muebles_no_registrables": getBienMuebleNoRegistrable(),
            "inversiones_cuentas_valores": getInversionesCuentasValores(),
            "efectivo_metales": getEfectivoMetales(),
            "fideicomisos": getFideicomisos(),
            "bienes_intangibles": getBienesIntangibles(),
            "cuentas_por_cobrar": getCuentasXCobrar(),
            "uso_especie_propiedad_tercero": getUsoEspeciePropietarioTercero()
        }

        # Pasivos
        sample['pasivos'] = {
            "deudas": getDeudas(),
            "otras_obligaciones": getOtrasObligaciones()
        }

        #print(sample)
        collection.insert_one(sample)
        # samples.append(sample)

    # with open('data.json', 'w') as outfile:
    #    json.dump(samples,outfile, indent=4)


# conn.close()
elif sys_number == 1:
    print('Sistema 2 -> Servidores públicos que intervienen en contrataciones')
elif sys_number == 2:
    print('Sistema 3 -> Servidores públicos y particulares sancionados')
else:
    parser.print_help()
