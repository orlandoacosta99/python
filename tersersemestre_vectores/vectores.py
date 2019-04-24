import statistics
import math

def producto_escalar(escalar, vector):
    """

    >>> producto_escalar(2, [1, 2, 3])
    [2, 4, 6]

    :param escalar:
    :param vector:
    :return:
    """
    res = []
    cont = 0
    while cont < len(vector):
        res.append(escalar * vector[cont])
        cont += 1
    return res

# def producto_escalar(escalar, vector):
#     """
#     (num, vector) -> vector
#     >>> producto_escalar(2, [2, 1])
#     [4, 2]
#     :param escalar:
#     :param vector:
#     :return:
#     """
#
#     res = []
#     cont = 0
#
#     for i in vector:
#         res.append(vector[cont] * escalar)
#         cont += 1
#
#     return res

def suma_productos(nvector1, nvector2):
    resultado = []
    contador = 0

    while(contador < len(nvector1)):
        resultado.append(nvector1[contador] + nvector2[contador])
        contador += 1

    return resultado

def producto_puntos (nvector1, nvector2):
    resultado = []
    contador = 0

    while (contador < len(nvector1)):
        resultado.append(nvector1[contador] * nvector2[contador])
        contador += 1

    Suma = 0

    for i in resultado:
        Suma = Suma + i
    return Suma

def elemento_mayor(nvector):

    return max(nvector)

def elemento_menor(nvector):

    return min(nvector)

def prom(nvector):
    resultado = []
    contador = 0

    while (contador < len(nvector)):
        resultado.append(nvector[contador])
        contador += 1
    Suma = 0

    for i in resultado:
        Suma = Suma + i

    resultado_promedio= Suma/len(resultado)
    return resultado_promedio

def desviacion_est(nvector):

    return statistics.stdev(nvector)

def elemento_igual(nvector):
    repetido = []
    unico = []

    for i in nvector:
        if i not in unico:
            unico.append(i)
            resultado=('no hay elementos repetidos')
        else:
            if i not in repetido:
                repetido.append(i)
            resultado = repetido

    return resultado

def Norma_vec(nvector):
    añadido = []
    contador = 0

    while (contador < len(nvector)):
        añadido.append((nvector[contador])**2 )
        contador += 1
    Suma = 0

    for i in añadido:
        Suma = Suma + i

    resultado_norma = math.sqrt(Suma)
    return resultado_norma

def Moda_vec(nvector):
    repeticiones = 0

    for i in nvector:
        cont = nvector.count(i)
        if cont > repeticiones:
            repeticiones = cont

    modas = []
    for i in nvector:
        cont = nvector.count(i)
        if cont == repeticiones and i not in modas:
            modas.append(i)

    return modas

