def un_segundo(hora, minutos, segundos):
    """
    (int,int, int)->str
    calcula la hora un segundo despues de los valores ingresados
    >>> un_segundo(10,23,42)
    'son la 10 horas 23 minutos y 43 segundos'

    :param hora: la hora actual
    :param minutos: los minutos
    :param segundos: los segundos
    :return: str
    """
    s_s = segundos +1
    s_m = minutos
    s_h = hora

    if s_s >= 60:
        s_s = 0
        s_m += 1
        if s_m >= 60:
            s_m = 0
            s_h += 1
            if s_h >= 24:
                s_h += 0
    return 'son la {0} horas {1} minutos y {2} segundos'. format(s_h, s_m, s_s)

#def palabra_num(palabra,num1,num2):
    """
    (num1, num2)->srt
    srt->str
    >>> palabra('hola', 1, 4)

    :param palabra:
    :param num1:
    :param num2:
    :return:
    """
#    pl = len(palabra)
#    num_1 = num1
#    num_2 = num2
#    if num_1 >= num_2:

 #       return str('el {1} es >= que {2}')

  #  else:

  #      return str('la longitud de esta palabra esta en este rango de {0} y los numeros son {1} y {2}').fotmat(pl, num_1, num_2)

def adecuada(palabra,desde,hasta):
    """
    >>> adecuada('hola',1,4)
    'la longitud de hola,  esta entre 1 y 4'

    :param palabra:
    :param desde:
    :param hasta:
    :return:
    """
    return 'la longitud de {0}, {1} esta entre {2} y {3}'\
    .format(palabra,""if desde <= len(palabra) <= hasta else "no", desde, hasta)

def numero_try(num):
    """
    >>> numero_try('hola')
    "'hola' no es un numero"

    :param num:
    :return:
    """
    try:
       return ("'{0}' no es u numero {1}").format(num, float(num)**2)

    except:
        return ("'{0}' no es un numero". format(num))












