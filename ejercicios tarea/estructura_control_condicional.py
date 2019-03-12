def esParentesis(caracter):
    '''
    (str of len == 1) -> str
    >>> esParentesis('(')
    'Es paréntesis'

    >>> esParentesis('k')
    'No es paréntesis'

    >>> esParentesis('as')
    Traceback (most recent call last):
    ..
    TypeError: as no es parentesis

    :param caracter:
    :return:
    '''

    esCaracter = len(caracter)

    if(esCaracter != 1):
        raise TypeError(str(caracter) + ' no es parentesis')

    elif(caracter == '(' or caracter == ')'):
        return 'Es paréntesis'
    else:
        return 'No es paréntesis'

def division(dividendo, divisor):
    '''
    (num, num) -> num
    >>> division(4, 2)
    2.0
    >>> division(15, 3)
    5.0
    >>> division(5, 0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError: La división en cero no es posible
    >>> division('as', 5)
    Traceback (most recent call last):
    ..
    TypeError: as no es numerico
    >>> division(4,'h')
    Traceback (most recent call last):
    ..
    TypeError: h no es numerico

    :param divisor:
    :param dividendo:
    :return:
    '''

    if (type(dividendo) != float  and type(dividendo) != int):
        raise TypeError(str(dividendo) + ' no es numerico')
    elif (type(divisor) != float and type(divisor) != int):
        raise TypeError(str(divisor) + ' no es numerico')
    elif (divisor == 0):
       raise ZeroDivisionError('La división en cero no es posible')
    else:
        return dividendo / divisor
def impar_par(num):
    """
    num-> str
    >>> impar_par(4)
    'es par'
    >>> impar_par(7)
    'es impar'
    >>> impar_par('as')
    Traceback (most recent call last):
    ..
    TypeError: as no es numerico

    :param num:
    :return:
    """
    if (type(num) != float  and type(num) != int):
        raise TypeError(str(num) + ' no es numerico')
    elif (num % 2 == 0):
        return 'es par'
    else:
        return 'es impar'


def esDobledeunImpar(num):
    '''
    (num of type == int) -> str

    >>> esDobledeunImpar(14)
    '14 es doble de 7, que es impar'
    >>> esDobledeunImpar(2.6)
    Traceback (most recent call last):
    ..
    TypeError: 2.6 no es numero o entero
    >>> esDobledeunImpar('asd')
    Traceback (most recent call last):
    ..
    TypeError: asd no es numero o entero

    :param mumero:
    :return:
    '''


    if (type(num) != int):
        raise TypeError(str(num) + ' no es numero o entero')
    else:
        impar = num / 2

    if (impar % 2) != 0:
         return str(num) + ' es doble de ' + str(int(impar)) + ', que es impar'
