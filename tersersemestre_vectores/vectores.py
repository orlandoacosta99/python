import math
import statistics

def producto_escalar(escalar, vector):
    """

    >>> producto_escalar(2, [1, 2, 3])
    [2, 4, 6]
    >>> producto_escalar(5,[2, 5, 1])
    [10, 25, 5]
    >>> producto_escalar(2, [2, 1])
    [4, 2]

    :param escalar: dato que multiplicara al vector
    :param vector: datos a los cuales seran multiplicados
    :return: retorna una lista a la cual hemos hecho el cambio
    """
    res = []
    cont = 0
    while cont < len(vector):
        res.append(escalar * vector[cont])
        cont += 1
    return res

def producto_escalar(escalar, vector):
    """
    (num, vector) -> vector
    >>> producto_escalar(2, [2, 1])
    [4, 2]
    >>> producto_escalar(2, [1, 2, 3])
    [2, 4, 6]
    >>> producto_escalar(5,[2, 5, 1])
    [10, 25, 5]

    :param escalar: dato que multiplicara al vector
    :param vector: datos a los cuales seran multiplicados
    :return: retorna una lista a la cual hemos hecho el cambio
    """

    res = []
    cont = 0

    for i in vector:
        res.append(vector[cont] * escalar)
        cont += 1

    return res

def suma_productos(nvector1, nvector2):
    """
    (vector, vector) -> vector

    >>> suma_productos([1, 2, 3], [2, 1, 3])
    [3, 3, 6]
    >>> suma_productos([4, 7, 1], [8, 5, 2])
    [12, 12, 3]
    >>> suma_productos([2, 4, 2], [3, 2, 8])
    [5, 6, 10]

    :param nvector1: ingresamos el primer vector para ser sumado
    :param nvector2: ingreso del segundo vector
    :return: se retornara un vector suma de los dos vectores anteriores
    """
    resultado = []
    contador = 0

    while(contador < len(nvector1)):
        resultado.append(nvector1[contador] + nvector2[contador])
        contador += 1

    return resultado

def producto_puntos (nvector1, nvector2):
    """
    (vector, vector) -> vector

    >>> producto_puntos([1, 2, 3],[2, 1, 3])
    13
    >>> producto_puntos([1, 2, -3], [-2, 4, 1])
    3
    >>> producto_puntos([2, 1, 2], [2, 4, 1])
    10

    :param nvector1: vector un el cual va ha ser multiplicado
    :param nvector2: vector dos el cual va ha ser multiplicado
    :return: se retornara la sumatoria total de los dos vectores multiplicados
    """
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
    """
    (vector) -> num
    >>> elemento_mayor([1, 2, 4, 2, 3])
    4
    >>> elemento_mayor([8, 5, 2])
    8
    >>> elemento_mayor([9, 6, 3, 12])
    12

    :param nvector: ingresamos un vector el cual va ser recorrido
    :return: retornamos el elemento mayor del vector
    """
    cont = 0

    for num in nvector:

        if num > cont:
            cont = num

    return cont


def elemento_menor(nvector):
    """
    (vector) -> num
    >>> elemento_menor([2, 4, 6, 7, 5])
    2
    >>> elemento_menor([1, 2, 5, 1, 6])
    1
    >>> elemento_menor([21, 42, 2, 12, 5])
    2

    :param nvector: ingresamos un vector el cual va ser recorrido
    :return: retornamos el elemento menor del vector
    """
    return min(nvector)

def prom(nvector):
    """
    (vector) -> num
    >>> prom([1, 2, 4, 2, 1, 2])
    2.0
    >>> prom([2, 1, 3, 5, 6, 2])
    3.1666666666666665
    >>> prom([2, 2, 2, 1, 5, 5, 6])
    3.2857142857142856

    :param nvector: ingresamos un vector el cual sumamos
    :return: retornamos el resultado de la divicion
    """
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
    """
    (vector) -> num
    >>> desviacion_est([2, 34, 3, 2 , 1, 4])
    12.940891262454324
    >>> desviacion_est([2, 4, 5, 6, 8, 1, 2])
    2.516611478423583
    >>> desviacion_est([3, 5, 6, 8, 1, 3])
    2.503331114069145

    :param nvector:
    :return:
    """

    return statistics.stdev(nvector)

def elemento_igual(nvector):
    """
    (vector) -> vector
    >>> elemento_igual([2, 5, 6, 7, 8])
    'no hay elementos repetidos'
    >>> elemento_igual([1, 2, 1, 5, 2, 1])
    [1, 2]
    >>> elemento_igual([2, 1, 3, 3, 2])
    [3, 2]

    :param nvector: ingresamos un vector
    :return: retornamos si el vector tiene elementos iguales o un str
    """
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
    """
    (vector) -> num
    >>> Norma_vec([2, 4, 1, 5])
    6.782329983125268
    >>> Norma_vec([2, 3, 2, 1])
    4.242640687119285
    >>> Norma_vec([1, -3, 5, 2, 2])
    6.557438524302

    :param nvector: ingresamos un vector el cual recorremos y sumamos
    :return: retornamos la factorizacion del vector
    """
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
    """
    (vector) -> vector
    >>> Moda_vec([1, 2, 5, 2, 1, 3, 1])
    [1]
    >>> Moda_vec([2, 1, 2, 2, 5, 3, 3, 1])
    [2]
    >>> Moda_vec([1, 2, 3, 4, 5, 2, 4, 3])
    [2, 3, 4]

    :param nvector: ingresamos un vector el cual recoremos y pasamos los datos repetidos a countador
    :return: retornamos los datos que mas aparecen en el vector
    """
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

