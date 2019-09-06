import random
import unidecode
import string
import pandas as pd
import uuid
import os
import git
import urllib.request
import json
from utilFechas import *

# nombres y apellidos
hombres = pd.read_csv('./corpus/hombres.csv')
hombres = hombres.values
mujeres = pd.read_csv('./corpus/mujeres.csv')
mujeres = mujeres.values
apellidos = pd.read_csv('./corpus/apellidos-20.csv')
apellidos = apellidos.values

# descarga los catálogos
if not os.path.isdir('./catalogos'):
    print('Descargando repositorio de catálogos...')
    git.Git('.').clone('https://github.com/PDNMX/catalogos.git')
    print('Listo!')

# (https://www.inegi.org.mx/app/ageeml/)
if not os.path.isfile('./catun_localidad.xlsx'):
    print('Descargando catálogo de localidades...')
    urllib.request.urlretrieve('https://www.inegi.org.mx/contenidos/app/ageeml/catuni/loc_mincona/catun_localidad.xlsx',
                               './catun_localidad.xlsx')
    print('Listo!')

catun = pd.read_excel('./catun_localidad.xlsx', header=3)


# Marco Geoestadístico (https://www.inegi.org.mx/app/ageeml/)


def get_id():
    return str(uuid.uuid1())


def rand_bool():
    return random.choice([True, False])


def get_name():
    gender = random.choice(['F', 'M'])

    name = random.choice(hombres) if gender is 'M' else \
        random.choice(mujeres)
    name = str(name[0])
    return name


def get_last_name():
    apellido = random.choice(apellidos)
    apellido = str(apellido[0])
    return apellido


def get_full_name():
    return "{} {} {}".format(get_name(), get_last_name(), get_last_name())


def get_email(domain):
    length = 12
    letters = string.ascii_lowercase
    user = ''.join(random.choice(letters) for i in range(length))
    return "{0}@{1}".format(user, domain)


def getMayusculas(total):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(total))


def getNumeros(total):
    return ''.join("{}".format(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) for i in range(total))


# BEML920313HMCLNS09
def get_curp():
    return "{}{}{}{}".format(getMayusculas(4), getNumeros(6), getMayusculas(6), getNumeros(2))


# GOAP780710RH7
def get_rfc():
    return "{}{}{}{}".format(getMayusculas(4), getNumeros(6), getMayusculas(2), getNumeros(1))


# IDMEX1710783604
def get_identificacion():
    return "IDMEX{}".format(getNumeros(10))


def getIdentificacionNacional():
    return "{}{}".format(getMayusculas(4), getNumeros(6))


def get_telephone(type):
    prefix = '+52' + ('1' if type == 'celular' else '')
    return prefix + str(random.randint(5500000000, 7779999999))


def get_bith_date():
    dia = (random.randint(1, 28))
    mes = (random.randint(1, 12))
    anio = (random.randint(1950, 1999))

    dia = "0{0}".format(dia) if dia < 10 else "{0}".format(dia)
    mes = "0{0}".format(mes) if mes < 10 else "{0}".format(mes)
    return "{0}-{1}-{2}".format(anio, mes, dia)


def get_college():
    colleges = [
        'Instituto Politécnico Nacional',
        'Instituto Tecnológico Autónomo de México',
        'Universidad Nacional Autónoma de México',
        'Universidad Iberoamericana',
        'Universidad de Guadalajara'
    ]

    return random.choice(colleges)


def get_amount(a, b):
    return round(random.randint(a, b), 2)


def get_degree():
    degrees = [
        'Ingeniería en Sistemas Computacionales',
        'Licenciatura en Matemáticas Aplicadas',
        'Ingeniería en Computación',
        'Ingeniería en Comunicaciones y Electrónica',
        'Licenciatura en Derecho',
        'Licenciatura en Ciencias Políticas',
        'Licenciatura en Física',
        'Ingeniería Industrial',
        'Ingeniería Civil',
        "Licenciatura en Historia",
        "Licenciatura en Ciencias de la Comunicación",
        "Ingeniería Mecánica",
        "Ingeniería Petrolera",
        "Ingeniería en Telecomunicaciones",
        "Ingeniería Química"
    ]
    return random.choice(degrees)


def get_position():
    positions = [
        'Enlace de Alto Nivel de Responsabilidad',
        'Jefe de Departamento',
        'Subdirector de Area',
        'Director de Area',
        'Director General Adjunto',
        'Director General',
        'Titular de Unidad'
    ]
    return random.choice(positions)


def lorem_ipsum():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."


def get_entidad():
    rows = len(catun)
    index = random.randint(1, rows - 1)
    loc = catun.iloc[index]

    return {
        "nom_agee": loc['nom_ent'],
        "cve_agee": str(loc['cve_ent'])
    }


def getLugarInstitucionEducativa():
    rows = len(catun)
    index = random.randint(1, rows - 1)
    loc = catun.iloc[index]

    return {
        "pais": {
            "valor": "MEXICO",
            "codigo": "MX"
        },
        "entidad_federativa": {
            "nom_agee": loc['nom_ent'],
            "cve_agee": str(loc['cve_ent'])
        },
        "municipio": {
            "nom_agem": loc['nom_mun'],
            "cve_agem": str(loc['cve_mun'])
        },
    }


def get_address():
    rows = len(catun)
    index = random.randint(1, rows - 1)
    loc = catun.iloc[index]

    return {
        "pais": {
            "valor": "MEXICO",
            "codigo": "MX"
        },
        "entidad_federativa": {
            "nom_agee": loc['nom_ent'],
            "cve_agee": str(loc['cve_ent'])
        },
        "municipio": {
            "nom_agem": loc['nom_mun'],
            "cve_agem": str(loc['cve_mun'])
        },
        "cp": "55018",
        "localidad": {
            "nom_loc": loc['nom_loc'],
            "cve_loc": str(loc['cve_loc'])
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
    }


def citizenship():
    countries = [
        {
            "valor": "Mexico",
            "codigo": "MX"
        },
        {
            "valor": "Australia",
            "codigo": "AU"
        },
        {
            "valor": "Bolivia",
            "codigo": "BO"
        },
        {
            "valor": "Brazil",
            "codigo": "BR"
        },
        {
            "valor": "Canada",
            "codigo": "CA"
        },
        {
            "valor": "Chile",
            "codigo": "CL"
        },
        {
            "valor": "China",
            "codigo": "CN"
        },
        {
            "valor": "Colombia",
            "codigo": "CO"
        },
        {
            "valor": "Cuba",
            "codigo": "CU"
        },
        {
            "valor": "Findland",
            "codigo": "FI"
        },
        {
            "valor": "Venezuela",
            "codigo": "VE"
        }
    ]

    c1 = {
        "valor": "Mexico",
        "codigo": "MX"
    }
    c2 = random.choice(countries)

    return [c1, c2] if c1.get("codigo") != c2.get("codigo") else [c1]


with open("./instituciones.json") as instituciones:
    cat_instituciones = json.load(instituciones)


def getInstitucion():
    return random.choice(cat_instituciones)


with open("./catalogos/catTipoApoyo.json") as tipo_apoyo:
    cat_tipo_apoyo = json.load(tipo_apoyo)


def getTipoApoyo():
    return random.choice(cat_tipo_apoyo)


with open("./catalogos/catRegimenMatrimonial.json") as regimen_matrimonial:
    cat_regimen_matrimonial = json.load(regimen_matrimonial)

with open("./catalogos/catEstadoCivil.json") as estado_civil:
    cat_estado_civil = json.load(estado_civil)

with open('./catalogos/catTipoBienInmueble.json') as inmuebles:
    cat_bien_inmueble = json.load(inmuebles)
    # cat_bien_inmueble

with open('./catalogos/catFormaAdquisicion.json') as forma_adquisicion:
    cat_forma_adquisicion = json.load(forma_adquisicion)


def getFormaAdquision():
    return random.choice(cat_forma_adquisicion)


with open("./catalogos/catPoder.json") as poder:
    cat_poder = json.load(poder)


def getPoder():
    return random.choice(cat_poder)


with open("./catalogos/catSectorIndustria.json") as sector_industria:
    cat_sector_industria = json.load(sector_industria)


def getSectorIndustria():
    return random.choice(cat_sector_industria)


with open("./catalogos/catFunciones.json") as funciones:
    cat_funciones = json.load(funciones)


def getFuncionesPrincipales():
    list = []
    for x in range(random.randint(1, 10)):
        funcion = random.choice(cat_funciones)
        if funcion["codigo"] != "OTRO":
            list.append(funcion)

    return list


with open("./catalogos/catAmbito.json") as ambito:
    cat_ambito = json.load(ambito)


def getAmbitos():
    return random.choice(cat_ambito)


with open("./catalogos/catNivelOrdenGobierno.json") as nivel_gobierno:
    cat_nivel_gobierno = json.load(nivel_gobierno)


def getNivelGobierno():
    return random.choice(cat_nivel_gobierno)


def getExperienciaLaboral():
    return {
        "ambito": getAmbitos(),
        "nivel_gobierno": getNivelGobierno(),
        "poder_ente": getPoder(),
        "nombre_institucion": getInstitucion(),
        "unidad_administrativa": "Unidad de Politica Regulatoria",
        "direccion": get_address(),
        "sector_industria": getSectorIndustria(),
        "jerarquia_rango": "string",
        "cargo_puesto": get_position(),
        "fecha_ingreso": getFecha(),
        "fecha_salida": getFecha(),
        "funciones_principales": getFuncionesPrincipales()
    }


def getExperienciasLaborales():
    list = []
    for x in range(random.randint(1, 4)):
        list.append(getExperienciaLaboral())

    return list


with open("./catalogos/catRelacionPersona.json") as relacion_persona:
    cat_relacion_persona = json.load(relacion_persona)


def getRelacionPersona(number):
    return cat_relacion_persona[number % 12]


with open("./catalogos/catRelacionPersona1.json") as relacion_persona1:
    cat_relacion_persona1 = json.load(relacion_persona1)


def getRelacionPersona1(number):
    return cat_relacion_persona1[number % 5]


with open("./catalogos/catRelacionPersona2.json") as relacion_persona2:
    cat_relacion_persona2 = json.load(relacion_persona2)


def getRelacionPersona2(number):
    return cat_relacion_persona2[number % 12]


with open("./catalogos/catRelacionPersona3.json") as relacion_persona3:
    cat_relacion_persona3 = json.load(relacion_persona3)


def getRelacionPersona3(number):
    return cat_relacion_persona3[number % 4]


def getDependiente(number):
    return {
        "nombre_personal": {
            "nombres": get_name(),
            "primer_apellido": get_last_name(),
            "segundo_apellido": get_last_name()
        },
        "tipo_relacion": getRelacionPersona1(number),
        "nacionalidades": citizenship(),
        "curp": get_curp(),
        "rfc": get_rfc(),
        "fecha_nacimiento": getFecha(),
        "numero_identificacion_nacional": getIdentificacionNacional(),
        "habita_domicilio_declarante": rand_bool(),
        "domicilio": get_address(),
        "medio_contacto": get_email('coldmail.com'),
        "ingresos_propios": True,
        "ocupacion_profesion": "Administrador de empresas",
        "sector_industria": getSectorIndustria(),
        "proveedor_contratista_gobierno": rand_bool(),
        "tiene_intereses_mismo_sector_declarante": rand_bool(),
        "desarrolla_cabildeo_sector_declarante": {
            "respuesta": True,
            "observaciones": lorem_ipsum()
        },
        "beneficiario_programa_publico": [{
            "nombre_programa": "Prospera",
            "institucion_otorga_apoyo": getInstitucion(),
            "tipo_apoyo": getTipoApoyo(),
            "valor_apoyo": random.randint(10000, 999999)
        }],
        "observaciones": lorem_ipsum()
    }


def getDependientesEconomicos():
    list = []
    number = random.randint(1, 10000)
    for x in range(random.randint(1, 6)):
        list.append(getDependiente(number + x))

    return list


with open("./empresas.json") as empresas:
    cat_empresas = json.load(empresas)


def getEmpresa():
    return unidecode.unidecode(random.choice(cat_empresas))


def getEmpresas():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_empresa_sociedad_asociacion": getEmpresa(),
            "pais_registro": {"valor": "MEXICO", "codigo": "MX"},
            "fecha_constitucion": getFecha(),
            "numero_registro": getIdentificacionNacional(),
            "rfc": get_rfc(),
            "domicilio": get_address(),
            "rol": "Dueño",
            "actividad_economica": rand_bool(),
            "sector_industria": getSectorIndustria(),
            "porcentaje_participacion": random.randint(10, 100)
        })

    return list


with open("./catalogos/catTipoInstitucion.json") as tipo_institucion:
    cat_tipo_institucion = json.load(tipo_institucion)


def getTipoInstitucion():
    return random.choice(cat_tipo_institucion)


with open("./catalogos/catNaturalezaMembresia.json") as naturaleza_membresia:
    cat_naturaleza_membresia = json.load(naturaleza_membresia)


def getNatualezaMembresia():
    return random.choice(cat_naturaleza_membresia)


def getMembresias():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_institucion": getTipoInstitucion(),
            "nombre_institucion": getEmpresa(),
            "naturaleza_membresia": getNatualezaMembresia(),
            "domicilio": get_address(),
            "sector_industria": getSectorIndustria(),
            "puesto_rol": "Titular",
            "fecha_inicio": getFecha(),
            "pagado": rand_bool(),
            "observaciones": lorem_ipsum()
        })

    return list


with open("./apoyos.json") as apoyos:
    cat_apoyos = json.load(apoyos)


def getApoyo():
    return random.choice(cat_apoyos)


def getApoyos():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "es_beneficiario": rand_bool(),
            "programa": getApoyo(),
            "institucion_otorgante": getInstitucion(),
            "nivel_orden_gobierno": getNivelGobierno(),
            "tipo_apoyo": getTipoApoyo(),
            "valor_anual_apoyo": random.randint(1, 999999),
            "observaciones": lorem_ipsum()
        })

    return list


with open("./catalogos/catTipoRepresentacion.json") as tipo_representacion:
    cat_tipo_representacion = json.load(tipo_representacion)


def getTipoRepresentacion():
    return random.choice(cat_tipo_representacion)


def getRepresentacionActiva():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_representacion": getTipoRepresentacion(),
            "nombre_parte_representada": get_full_name(),
            "curp_parte": get_curp(),
            "rfc_parte": get_rfc(),
            "fecha_nacimiento_parte": get_bith_date(),
            "sector_industria": getSectorIndustria(),
            "fecha_inicio": get_bith_date(),
            "pagado": rand_bool(),
            "observaciones": lorem_ipsum()
        })

    return list


def getRepresentacionPasiva():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_representacion": getTipoRepresentacion(),
            "nombre": get_full_name(),
            "fecha_inicio_representacion": getFecha(),
            "nacionalidades": citizenship(),
            "curp": get_curp(),
            "rfc": get_rfc(),
            "fecha_nacimiento": get_bith_date(),
            "tiene_intereses": rand_bool(),
            "ocupacion_profesion": "Contador",
            "sector_industria": getSectorIndustria(),
            "observaciones": lorem_ipsum()
        })

    return list


def getSociosComerciales():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_actividad": "Actividad",
            "tipo_vinculo": getRelacionPersona(random.randint(1, 100))["valor"],
            "antiguedad_vinculo": random.randint(1, 30),
            "rfc_entidad": get_rfc(),
            "nombre": get_full_name(),
            "curp": get_curp(),
            "rfc": get_rfc(),
            "lugar_nacimiento": {
                "pais": {
                    "valor": "MEXICO",
                    "codigo": "MX"
                },
                "entidad": get_entidad()
            },
            "fecha_nacimiento": get_bith_date(),
            "porcentaje_participacion": random.randint(10, 100),
            "sector_industria": getSectorIndustria(),
            "observaciones": lorem_ipsum()
        })

    return list


def getClientesPrincipales():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_negocio": getEmpresa(),
            "numero_registro": get_rfc(),
            "dueno_encargado": get_full_name(),
            "nombre": get_full_name(),
            "rfc": get_rfc(),
            "domicilio": get_address(),
            "sector_industria": getSectorIndustria(),
            "porcentaje_participacion": random.randint(10, 100),
            "observaciones": lorem_ipsum()
        })

    return list


def getOtrasPartes():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_relacion": getRelacionPersona3(random.randint(1, 100)),
            "nombre_denominacion_parte": get_full_name(),
            "fecha_inicio_relacion": getFecha(),
            "nacionalidades": citizenship(),
            "curp": get_curp(),
            "rfc": get_rfc(),
            "fecha_nacimiento": get_bith_date(),
            "ocupacion": "Administrador de empresas",
            "tiene_interes": True,
            "sector_industria": getSectorIndustria(),
            "observaciones": lorem_ipsum()
        })

    return list


def getBeneficiosGratuitos():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_beneficio": "Tarjetas o monederos electronicos",
            "origen_beneficio": "Prestacion laboral",
            "sector_industria": getSectorIndustria(),
            "valor_beneficio": 1256,
            "observaciones": lorem_ipsum()
        })

    return list


with open("./catalogos/catUnidadMedidaPlazo.json") as unidad_medida:
    cat_unidad_medida = json.load(unidad_medida)


def getUnidadMedida():
    return random.choice(cat_unidad_medida)


def getIngreso():
    valor = random.randint(10000, 999999)
    unidad_temporal = getUnidadMedida()

    if valor > 999999:
        unidad_temporal = {
            "codigo": "TUNI",
            "valor": "Transacción única"
        }

    return {
        "valor": valor,
        "moneda": {
            "codigo": "MXN",
            "moneda": "MXN"
        },
        "unidad_temporal": unidad_temporal,
        "duracion_frecuencia": random.randint(1, 12),
        "fecha_transaccion": getFecha()
    }


#######################################
############## INGRESOS ###############
#######################################


def getSalariosPublicos():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "ente_publico": {
                "valor": "SECRETARIA DE GOBERNACION",
                "codigo": "SEGOB"
            },
            "rfc": get_rfc(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


def getSalariosOtrosEmpleos():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion_razon_social": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad_servicio": getActividadServicio(),
            "descripcion_actividad_servicio": lorem_ipsum(),
            "domicilio_persona_paga": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


with open("./catalogos/catTipoActividadServicio.json") as actividad_servicio:
    cat_actividad_servicio = json.load(actividad_servicio)


def getActividadServicio():
    return random.choice(cat_actividad_servicio)


def getActividadProfesional():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion_razon_social": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad_servicio": getActividadServicio(),
            "descripcion_actividad_servicio": lorem_ipsum(),
            "domicilio_persona_paga": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


def getActividadEmpresarial():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion_razon_social": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad_servicio": getActividadServicio(),
            "descripcion_actividad_servicio": lorem_ipsum(),
            "domicilio_actividad_empresarial": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


def getActividadEconomicaMenor():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion_razon_social": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad_servicio": getActividadServicio(),
            "descripcion_actividad_servicio": lorem_ipsum(),
            "domicilio_actividad": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


def getArrendamiento():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion_razon_social": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad_servicio": getActividadServicio(),
            "descripcion_actividad_servicio": lorem_ipsum(),
            "domicilio_actividad": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


def getIntereses():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion_razon_social": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad_servicio": getActividadServicio(),
            "descripcion_actividad_servicio": lorem_ipsum(),
            "domicilio": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


def getPremios():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad_servicio": getActividadServicio(),
            "descripcion_premio": lorem_ipsum(),
            "domicilio": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


with open("./catalogos/catTipoBien_enajenacion_bienes.json") as tipo_bien:
    cat_tipo_bien = json.load(tipo_bien)


def getTipoBien():
    return random.choice(cat_tipo_bien)


with open("./catalogos/catTipoBien_propiedad_tercero.json") as tipo_bien2:
    cat_tipo_bien2 = json.load(tipo_bien2)


def getTipoBien2():
    return random.choice(cat_tipo_bien2)


def getEnajenacionBienes():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "tipo_bien": getTipoBien(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad_servicio": getActividadServicio(),
            "descripcion_bien": lorem_ipsum(),
            "domicilio_bien_enajenado": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


def getOtrosIngresos():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_denominacion": getEmpresa(),
            "rfc": get_rfc(),
            "curp": get_curp(),
            "sector_industria": getSectorIndustria(),
            "tipo_actividad": getActividadServicio(),
            "descripcion_actividad": lorem_ipsum(),
            "domicilio_actividad": get_address(),
            "ingreso_bruto_anual": getIngreso(),
            "observaciones": lorem_ipsum()
        })

    return list


def getIngresos():
    return {
        "sueldos_salarios_publicos": getSalariosPublicos(),
        "sueldos_salarios_otros_empleos": getSalariosOtrosEmpleos(),
        "actividad_profesional": getActividadProfesional(),
        "actividad_empresarial": getActividadEmpresarial(),
        "actividad_economica_menor": getActividadEconomicaMenor(),
        "arrendamiento": getArrendamiento(),
        "intereses": getIntereses(),
        "premios": getPremios(),
        "enajenacion_bienes": getEnajenacionBienes(),
        "otros_ingresos": getOtrosIngresos()
    }


#######################################
############## activos ################
#######################################

with open('./catalogos/catTipoOperacion1.json') as tipo_operacion1:
    cat_tipo_operacion1 = json.load(tipo_operacion1)


def getTipoOperacion1():
    return random.choice(cat_tipo_operacion1)


with open('./catalogos/catTitulaBien.json') as titular_bien:
    cat_titular_bien = json.load(titular_bien)


def getTitularBien():
    return random.choice(cat_titular_bien)


def getBienesInmuebles():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion1(),
            "tipo_bien": random.choice(cat_bien_inmueble),
            "superficie_terreno": random.randint(1, 999),
            "superficie_construccion": random.randint(1, 999),
            "titular": getTitularBien(),
            "porcentaje_propiedad": random.randint(10, 100),
            "nombre_copropietario": {
                "nombres": get_name(),
                "primer_apellido": get_last_name(),
                "segundo_apellido": get_last_name()
            },
            "identificacion_bien": {
                "numero_escritura_publica": int(getNumeros(10)),
                "numero_registro_publico": int(getNumeros(10)),
                "folio_real": "{}-{}".format(getMayusculas(4), getNumeros(6)),
                "fecha_contrato": getFecha()
            },
            "domicilio_bien": get_address(),
            "forma_adquisicion": random.choice(cat_forma_adquisicion),
            "nombre_denominacion_quien_adquirio": get_full_name(),
            "rfc_quien_adquirio": get_rfc(),
            "curp_quien_adquirio": get_curp(),
            "relacion_persona_adquirio": getRelacionPersona2(random.randint(1, 1000)),
            "sector_industria": getSectorIndustria(),
            "fecha_adquisicion": getFecha(),
            "precio_adquisicion": {
                "valor": random.randint(1, 999999),
                "moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                }
            },
            "valor_catastral": random.randint(1, 999999),
            "observaciones": lorem_ipsum()
        })

    return list


#######################################
############## pasivos ################
#######################################

def getMarcas():
    return random.choice(["ALFA-ROMERO",
                          "AUDI",
                          "BMW",
                          "CHEVROLET",
                          "DODGE",
                          "HONDA",
                          "ISUZU",
                          "JAGUAR",
                          "MAZDA",
                          "MERCEDES-BENZ",
                          "MERCURY",
                          "MITSUBISHI",
                          "NISSAN",
                          "PEUGOT",
                          "PLYMOUTH",
                          "PORSCHE",
                          "RENAULT",
                          "SAAB",
                          "SUBARU",
                          "TOYOTA",
                          "VOLKSWAGEN",
                          "VOLVO"])


def getCopropietarios():
    list = []
    for x in range(random.randint(1, 6)):
        list.append(get_full_name())

    return list


def getBienMuebleRegistrable():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion1(),
            "tipo_bien_mueble": getTipoBien2(),
            "marca": getMarcas(),
            "submarca": "{}-{}".format(getMayusculas(4), getNumeros(6)),
            "modelo": random.randint(1995, 2020),
            "numero_serie": "{}-{}-{}".format(getNumeros(6), getMayusculas(4), getNumeros(6)),
            "lugar_registro": {
                "pais": {
                    "valor": "MEXICO",
                    "codigo": "MX"
                },
                "entidad": get_entidad()
            },
            "titular_bien": getTitularBien(),
            "porcentaje_propiedad": random.randint(10, 100),
            "nombres_copropietarios": getCopropietarios(),
            "numero_registro_vehicular": int(getNumeros(10)),
            "forma_adquisicion": getFormaAdquision(),
            "nombre_denominacion_adquirio": get_full_name(),
            "rfc_quien_adquirio": get_rfc(),
            "relacion_persona_quien_adquirio": getRelacionPersona2(random.randint(1, 10000)),
            "sector_industria": getSectorIndustria(),
            "fecha_adquisicion": get_bith_date(),
            "precio_adquisicion": {
                "valor": random.randint(1, 999999),
                "moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                }
            },
            "observaciones": lorem_ipsum()
        })

    return list


def getBienMuebleNoRegistrable():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion1(),
            "tipo_bien": getTipoBien2(),
            "descripcion": lorem_ipsum(),
            "titular_bien": getTitularBien(),
            "porcentaje_propiedad": random.randint(1, 100),
            "nombres_copropietarios": getCopropietarios(),
            "forma_adquisicion": getFormaAdquision(),
            "nombre_denominacion_adquirio": get_full_name(),
            "relacion_quien_adquirio": getRelacionPersona2(random.randint(1, 999999)),
            "fecha_adquisicion": getFecha(),
            "precio_adquisicion": {
                "valor": random.randint(10000, 999999),
                "moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                }
            },
            "observaciones": lorem_ipsum()
        })

    return list


with open('./catalogos/catTipoOperacion2.json') as tipo_operacion2:
    cat_tipo_operacion2 = json.load(tipo_operacion2)


def getTipoOperacion2():
    return random.choice(cat_tipo_operacion2)


with open('./catalogos/catTipoInversion.json') as tipo_inversion:
    cat_tipo_inversion = json.load(tipo_inversion)


def getTipoInversion():
    return random.choice(cat_tipo_inversion)


with open('./catalogos/catTipoEspecificoInversion.json') as tipo_especifico_inversion:
    cat_tipo_especifico_inversion = json.load(tipo_especifico_inversion)


def getTipoEspecificoInversion():
    return random.choice(cat_tipo_especifico_inversion)


def getInversionesCuentasValores():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion2(),
            "tipo_inversion": getTipoInversion(),
            "tipo_especifico_inversion": getTipoEspecificoInversion(),
            "numero_cuenta": "{}{}".format(getMayusculas(6), getNumeros(6)),
            "nacional_extranjero": {
                "valor": "México",
                "codigo": "MX"
            },
            "nombre_institucion": random.choice(['Barclays', 'Citigroup', 'HSBC', 'BBVA', 'Bank of America']),
            "rfc_institucion": get_rfc(),
            "sector_industria": getSectorIndustria(),
            "domicilio_institucion": get_address(),
            "forma_adquisicion": getFormaAdquision(),
            "fecha_inicio": getFecha(),
            "monto_original": get_amount(1, 999999),
            "tipo_moneda": {
                "codigo": "MXN",
                "moneda": "MXN"
            },
            "tasa_interes": random.randint(10, 70),
            "saldo_anual": get_amount(1, 999999),
            "plazo": random.randint(1, 52),
            "unidad_medida_plazo": getUnidadMedida(),
            "titular_bien": getTitularBien(),
            "porcentaje_inversion": random.randint(1, 100),
            "observaciones": lorem_ipsum()
        })

    return list


with open('./catalogos/catTipoMetal.json') as tipo_metal:
    cat_tipo_metal = json.load(tipo_metal)


def getTipoMetal():
    return random.choice(cat_tipo_metal)


def getEfectivoMetales():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion2(),
            "tipo_moneda": {
                "codigo": "MXN",
                "moneda": "MXN"
            },
            "monto_moneda": get_amount(1, 999999),
            "tipo_metal": getTipoMetal(),
            "unidades": random.randint(1, 999999),
            "monto_metal": get_amount(1, 999999),
            "forma_adquisicion": getFormaAdquision(),
            "observaciones_comentarios": lorem_ipsum()
        })

    return list


with open('./catalogos/catTipoFideicomiso.json') as tipo_fideicomiso:
    tipo_fideicomiso = json.load(tipo_fideicomiso)


def getTipoFideicomiso():
    return random.choice(tipo_fideicomiso)


def getFideicomisos():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion2(),
            "identificador_fideicomiso": "{}{}".format(getMayusculas(4), getNumeros(6)),
            "tipo_fideicomiso": getTipoFideicomiso(),
            "objetivo": lorem_ipsum(),
            "numero_registro": "{}{}".format(getMayusculas(4), getNumeros(6)),
            "fecha_creacion": getFecha(),
            "vigencia": get_bith_date(),
            "residencia": {
                "valor": "MEXICO",
                "codigo": "MX"
            },
            "valor": random.randint(1, 999999),
            "moneda": {
                "codigo": "MXN",
                "moneda": "MXN"
            },
            "porcentaje_propiedad_derechos_fiduciarios": random.randint(1, 100),
            "ingreso_monetario_obtenido": random.randint(1, 999999),
            "institucion_fiduciaria": "Banco de México",
            "fideicomitente": {
                "nombre": get_full_name(),
                "rfc": get_rfc(),
                "curp": get_curp(),
                "domicilio": get_address(),
                "fecha_constitucion": getFecha()
            },
            "fideicomisario": {
                "nombre": get_full_name(),
                "rfc": get_rfc(),
                "curp": get_curp(),
                "domicilio": get_address(),
                "fecha_constitucion": getFecha()
            },
            "fiduciario": {
                "nombre": get_full_name(),
                "rfc": get_rfc(),
                "curp": get_curp(),
                "domicilio": get_address(),
                "fecha_constitucion": getFecha()
            },
            "observaciones": lorem_ipsum()
        })

    return list


def getBienesIntangibles():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion2(),
            "propietario_registrado": getCopropietarios(),
            "descripcion": lorem_ipsum(),
            "ente_publico_encargado": getInstitucion(),
            "numero_registro": int(getNumeros(10)),
            "fecha_registro": getFecha(),
            "sector_industria": getSectorIndustria(),
            "precio_adquisicion": {
                "valor": random.randint(1, 999999),
                "moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                }
            },
            "forma_adquisicion": getFormaAdquision(),
            "fecha_vencimiento": getFecha(),
            "porcentaje_copropiedad": random.randint(1, 100),
            "precio_total_copropiedad": {
                "valor": random.randint(1, 999999),
                "moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                }
            },
            "nombre_copropietario": get_full_name(),
            "porcentaje_propiedad_copropietario": random.randint(1, 100),
            "observaciones": lorem_ipsum()
        })

    return list


def getCuentasXCobrar():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "nombre_prestatario": get_full_name(),
            "numero_registro": "{}{}".format(getMayusculas(4), getNumeros(6)),
            "domicilio_prestatarios": get_address(),
            "sector_industria": getSectorIndustria(),
            "fecha_prestamo": getFecha(),
            "monto_original_prestamo": get_amount(1, 999999),
            "tasa_interes": random.randint(10, 100),
            "saldo_pendiente": random.randint(1, 999999),
            "fecha_vencimiento": getFecha(),
            "porcentaje_copropiedad": random.randint(1, 100),
            "nombre_copropietario": get_full_name(),
            "observaciones": lorem_ipsum()
        })

    return list


def getUsoEspeciePropietarioTercero():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_bien": getTipoBien()["valor"],
            "valor_mercado": {
                "valor": random.randint(1, 999999),
                "moneda": {
                    "codigo": "MXN",
                    "moneda": "MXN"
                }
            },
            "nombre_tercero_propietario": get_full_name(),
            "rfc_tercero_propietario": get_rfc(),
            "curp_tercero_propietario": get_curp(),
            "relacion_persona": getRelacionPersona2(random.randint(1, 1000)),
            "sector_industria": getSectorIndustria(),
            "fecha_inicio": getFecha(),
            "domicilio_persona": get_address(),
            "observaciones": lorem_ipsum()
        })

    return list


with open('./catalogos/catTipoOperacion3.json') as tipo_operacion3:
    cat_tipo_operacion3 = json.load(tipo_operacion3)


def getTipoOperacion3():
    return random.choice(cat_tipo_operacion3)


with open('./catalogos/catTipoAcreedor.json') as tipo_acreedor:
    cat_tipo_acreedor = json.load(tipo_acreedor)


def getTipoAcreedor():
    return random.choice(cat_tipo_acreedor)


with open('./catalogos/catTipoAdeudo.json') as tipo_adeudo:
    cat_tipo_adeudo = json.load(tipo_adeudo)


def getTipoAdeudo():
    return random.choice(cat_tipo_adeudo)


def getMontosAbonados():
    list = []
    for x in range(random.randint(1, 100)):
        list.append(random.randint(1, 999999))

    return list


def getDeudas():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion3(),
            "tipo_acreedor": getTipoAcreedor(),
            "tipo_adeudo": getTipoAdeudo(),
            "identificador_deuda": "{}{}".format(getMayusculas(4), getNumeros(6)),
            "nacional_extranjero": {
                "valor": "MEXICO",
                "codigo": "MX"
            },
            "nombre_acreedor": get_full_name(),
            "rfc_acreedor": get_rfc(),
            "sector_industria": getSectorIndustria(),
            "domicilio_acreedor": get_address(),
            "fecha_adeudo": getFecha(),
            "monto_original": get_amount(1, 999999),
            "tipo_moneda": {
                "codigo": "MXN",
                "moneda": "MXN"
            },
            "tasa_interes": random.randint(1, 100),
            "saldo_pendiente": random.randint(1, 999999),
            "montos_abonados": getMontosAbonados(),
            "plazo_adeudo": random.randint(1, 72),
            "unidad_medida_adeudo": getUnidadMedida(),
            "titularidad_deuda": getTitularBien(),
            "porcentaje_adeudo_titular": random.randint(1, 100),
            "garantia": rand_bool(),
            "nombre_garante": get_full_name(),
            "observaciones": lorem_ipsum()
        })

    return list


with open('./catalogos/catTipoObligacion.json') as tipo_obligacion:
    cat_tipo_obligacion = json.load(tipo_obligacion)


def getTipoObligacion():
    return random.choice(cat_tipo_obligacion)


def getOtrasObligaciones():
    list = []
    for x in range(random.randint(1, 6)):
        list.append({
            "id": int(getNumeros(10)),
            "tipo_operacion": getTipoOperacion3(),
            "tipo_acreedor": getTipoAcreedor(),
            "tipo_obligacion": getTipoObligacion(),
            "identificador_obligacion": "{}{}".format(getMayusculas(4), getNumeros(6)),
            "nacional_extranjero": {
                "valor": "MEXICO",
                "codigo": "MX"
            },
            "nombre_acreedor": get_full_name(),
            "rfc_acreedor": get_rfc(),
            "sector_industria": getSectorIndustria(),
            "domicilio_acreedor": get_address(),
            "fecha_obligacion": getFecha(),
            "monto_original": get_amount(1, 999999),
            "tipo_moneda": {
                "codigo": "MXN",
                "moneda": "MXN"
            },
            "tasa_interes": random.randint(1, 100),
            "saldo_pendiente": random.randint(1, 999999),
            "montos_abonados": getMontosAbonados(),
            "plazo_adeudo": random.randint(1, 72),
            "unidad_medida_adeudo": getUnidadMedida(),
            "titularidad_obligacion": getTitularBien(),
            "porcentaje_obligacion_titular": random.randint(1, 100),
            "garantia": rand_bool(),
            "nombre_garante": get_full_name(),
            "observaciones": lorem_ipsum()
        })

    return list
