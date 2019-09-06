import random

def getDia(mes):
    if (mes == 2):
        return "{:02d}".format(random.randint(1, 28))
    else:
        return "{:02d}".format(random.randint(1, 30))

def getMes():
    return "{:02d}".format(random.randint(1, 12))

def getAnio():
    return random.randint(2000, 2018)

def getAnioNacimiento():
    return random.randint(1940, 2018)


def getHora():
    return "{:02d}".format(random.randint(0, 24))

def getMinuto():
    return "{:02d}".format(random.randint(0, 60))

def getSegundo():
    return "{:02d}".format(random.randint(0, 60))

def getFecha():
    anio = getAnio()
    mes = getMes()
    dia = getDia(mes)
    return "{}-{}-{}".format(str(anio), str(mes), str(dia))


def getFechaNacimiento():
    anio = getAnioNacimiento()
    mes = getMes()
    dia = getDia(mes)
    return "{}-{}-{}".format(str(anio), str(mes), str(dia))

def getHoras():
    hora = getHora()
    minuto = getMinuto()
    segundo = getSegundo()
    return "{}:{}:{}".format(str(hora), str(minuto), str(segundo))

def getUTCDate():
    return "{}T{}Z".format(getFecha(), getHoras())
