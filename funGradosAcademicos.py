from random_data import *

with open('./catalogos/catGradoAcademico.json') as grado_academico:
    cat_grado_academico = json.load(grado_academico)


def grados_academicos():
    return random.choice(cat_grado_academico)


with open('./catalogos/catEstatusEstudios.json') as estatus_estudios:
    cat_estatus_estudios = json.load(estatus_estudios)


def getEstatusEstudios():
    return random.choice(cat_estatus_estudios)


with open('./catalogos/catDocumentoObtenido.json') as documento_obtenido:
    cat_documento_obtenido = json.load(documento_obtenido)


def getDocumentoObtenido():
    return random.choice(cat_documento_obtenido)


def getGrado(data=None):
    if data is None:
        info = grados_academicos()
    else:
        info = data

    return {
        "grado_obtenido": info,
        "institucion_educativa": get_college(),
        "lugar_institucion_educativa": getLugarInstitucionEducativa(),
        "carrera": get_degree(),
        "estatus": getEstatusEstudios(),
        "ano_conclusion": random.randint(1950, 2018),
        "documento_obtenido": getDocumentoObtenido(),
        "cedula_profesional": "{}".format(getNumeros(6))
    }


def getGradosAcademicos():
    total = random.randint(1, 4)

    if total == 1:
        return [getGrado({
            "codigo": "BACH",
            "valor": "Bachillerato"
        })]

    if total == 2:
        return [getGrado({
            "codigo": "LICE",
            "valor": "Licenciatura"
        }), getGrado({
            "codigo": "BACH",
            "valor": "Bachillerato"
        })]

    if total == 3:
        return [getGrado({
            "codigo": "MAES",
            "valor": "Maestría"
        }), getGrado({
            "codigo": "LICE",
            "valor": "Licenciatura"
        }), getGrado({
            "codigo": "BACH",
            "valor": "Bachillerato"
        })]

    if total == 4:
        return [getGrado({
            "codigo": "DOCT",
            "valor": "Doctorado"
        }), getGrado({
            "codigo": "MAES",
            "valor": "Maestría"
        }), getGrado({
            "codigo": "LICE",
            "valor": "Licenciatura"
        }), getGrado({
            "codigo": "BACH",
            "valor": "Bachillerato"
        })]
