# Generador de datos sintéticos

## ¿Qué es y para qué sirve?
Es un generador de datos sintético para los 6 sistemas de la PDN. 

*Actualmente sólo está programado el del sistema de declaraciones*

## Dependendecias Generales
```
pip install pymongo
pip install pandas
```


## USO
```
usage: datagen.py [-h] [-s {1,2,3}] [-n SAMPLES]

SESNA data generator

optional arguments:
  -h,--help                         show this help message and exit
  -s {1,2,3}, --sys {1,2,3}         System number
  -n SAMPLES, --samples SAMPLES     Number of samples
```

### Sistema 1 .- Declaraciones
#### Pasos
1. Contar con una base de datos mongo previamente configurada.
2. Configurar las lineas de acceso a la base de datos mongo directamente en el archivo datagen.py o use las variables de entorno
```
host = os.environ.get('DATAGEN_MONGO_HOST', 'localhost')
port = os.environ.get('DATAGEN_MONGO_PORT', 27017)
user = os.environ.get('DATAGEN_MONGO_USER', None)
password = os.environ.get('DATAGEN_MONGO_PASS', None)
```
3. Uso para generar 10 declaraciones ficticias
```
$ python datagen.py -s 1 -n 10

```
