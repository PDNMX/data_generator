# Generador de datos sintéticos

## ¿Qué es y para qué sirve?
Es un generador de datos sintético para los 6 sistemas de la PDN. 

*Actualmente sólo está programado el del sistema de declaraciones*

## Dependendecias Generales
```
$ conda create --name <env> --file requirements.txt

donde:
  env -> nombre del ambiente donde se cargaran las dependencias
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
2. Setear las variables de entorno para la conexion a la base de datos mongo
```
export DATAGEN_MONGO_HOST=host
export DATAGEN_MONGO_PORT=port
export DATAGEN_MONGO_USER=user
export DATAGEN_MONGO_PASS=password
```
3. Uso para generar 10 declaraciones ficticias
```
$ python datagen.py -s 1 -n 10

```
