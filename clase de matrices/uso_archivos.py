import json

diccionario = {
    'hola':'mundo',
    'camilo':'acosta',
    'programacion':'ean'
}

def guardar(nombre_archivo, diccionario_guardar):
    """

    :param nombre_archivo:
    :param diccionario_guardar:
    :return:
    """
    try:

        archivo = open(nombre_archivo, "w")

        convertido = json.dumps(diccionario_guardar)


        archivo.write(convertido)

        archivo.close()
        return True
    except:

        return False


def leer (nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r")

        diccionario_leido = json.load(archivo)

        archivo.close()
        return diccionario_leido
    except:

        return {}

if __name__ == '__main__':
    nombre_archivo = ('prueba.json')
    leido=leer(nombre_archivo)

    print(leido)
    print(guardar(nombre_archivo, diccionario))
