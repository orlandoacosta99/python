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

def numprimos(num):
    """
    num-> str
    >>> numprimos(7)
    'si es primo'
    >>> numprimos(4)
    'no es primo'
    >>> numprimos('ad')
    Traceback (most recent call last):
    ..
    TypeError: ad no es numero o entero
    >>> numprimos(2.1)
    Traceback (most recent call last):
    ..
    TypeError: 2.1 no es numero o entero

    :param num:
    :return:
    """
    if (type(num) != int):
        raise TypeError(str(num) + ' no es numero o entero')
    else:
        x = 0
        for i in range(1, num + 1):
            if (num % i == 0):
                x = x + 1
        if (x != 2):
            return ('no es primo')
        else:
            return ('si es primo')

def Billetes(num):
    """
    num -> str
    >>> Billetes(434)
    2 billetes de 200 euros.
    1 billetes de 20 euros.
    1 billetes de 10 euros.
    2 monedas de 2 euros.

    :param valor:
    :return:
    """

    mensaje = ''

    if (num // 500) != 0:
        mensaje += str((num // 500)) + ' billetes de 500 euros.'
        mensaje += '\n'
        num = num - (num // 500) * 500

    if (num // 200) != 0:
        mensaje += str((num // 200)) + ' billetes de 200 euros.'
        mensaje += '\n'
        num = num - (num // 200) * 200

    if (num // 100) != 0:
        mensaje += str((num // 100)) + ' billetes de 100 euros.'
        mensaje += '\n'
        num = num - (num // 100) * 100

    if (num // 50) != 0:
        mensaje += str((num // 50)) + ' billetes de 50 euros.'
        mensaje += '\n'
        num = num - (num // 50) * 50

    if (num // 20) != 0:
        mensaje += str((num // 20)) + ' billetes de 20 euros.'
        mensaje += '\n'
        num = num - (num // 20) * 20

    if (num // 10) != 0:
        mensaje += str((num // 10)) + ' billetes de 10 euros.'
        mensaje += '\n'
        num = num - (num // 10) * 10

    if (num // 5) != 0:
        mensaje += str((num // 5)) + ' billetes de 5 euros.'
        mensaje += '\n'
        num = num - (num // 5) * 5

    if (num // 2) != 0:
        mensaje += str((num // 2)) + ' monedas de 2 euros.'
        mensaje += '\n'
        num = num - (num // 2) * 2

    if (num // 1) != 0:
        mensaje += str((num // 1)) + ' monedas de 1 euros.'
        num = num - (num // 1) * 1

    print('%s' % mensaje.rstrip('\n'))


def dias(num):
    """
    num->str

    >>> dias(5)
    'viernes'
    >>> dias('as')
    Traceback (most recent call last):
    ..
    TypeError: as no es numero o entero
    >>> dias(8)
    'debe ser mayor que 0 y menor que 8'

    :param num:
    :return:
    """
    if (type(num) != int):
        raise TypeError(str(num) + ' no es numero o entero')
    else:
        if (num <= 7 and num > 0 and num != int):

            if num == 7:
                return str('domingo')
            elif num == 6:
                return str('sabado')
            elif num == 5:
                return str('viernes')
            elif num == 4:
                return str('jueves')
            elif num == 3:
                return str('miercoles')
            elif num == 2:
                return str('martes')
            elif num == 1:
                return str('lunes')
        else:
            return 'debe ser mayor que 0 y menor que 8'


