import random, string

def get_email(domain):
    length = 12
    letters = string.ascii_lowercase
    user = ''.join(random.choice(letters) for i in range(length))
    return "{0}@{1}".format(user, domain)

def get_telephone(type):
    prefix = '+52' + ('1' if type == 'celular' else '')
    return prefix + str(random.randint(5500000000,7779999999))

def get_bith_date():
    dia = str(random.randint(1,28))
    mes = str(random.randint(1,12))
    anio = str(random.randint(1950,1999))
    return "{0}/{1}/{2}".format(dia, mes, anio)


def get_college():

    colleges= [
        'Instituto Politécnico Nacional',
        'Instituto Tecnológico Autónomo de México',
        'Universidad Nacional Autónoma de México',
        'Universidad Iberoamericana',
        'Universidad de Guadalajara'
    ]

    return colleges[ random.randint(0, (len(colleges)-1))]

def get_degree():
    degrees =[
        'Ingeniería en Sistemas Computacionales',
        'Licenciatura en Matemáticas Aplicadas',
        'Ingeniería en Computación',
        'Ingeniería en Comunicaciones y Electrónica',
        'Licenciatura en Derecho',
        'Licenciatura en Ciencias Políticas',
        'Licenciatura en Física',
        'Ingeniería Industrial'
    ]
    return degrees[random.randint(0, (len(degrees) - 1))]

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
    return positions[random.randint(0, (len(positions) - 1))]


def get_institution():
    institutions=[
        'Instituto Federal de Telecomunicaciones',
        'Presidencia de la República',
        'Comisión Federal de Competencia Económica',
        'Secretaría de Comunicaciones y Transportes',
        'Secretaría Ejecutiva del Sistema Nacional Anticorrupción',
        'Secretaría de la Función Pública'
    ]
    return institutions[random.randint(0, (len(institutions)-1))]
