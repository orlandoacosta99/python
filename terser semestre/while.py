def invertir_lista(lista):
    """
    resorrer una lista e invertirla
    >>> invertir_lista(['a',10,'jose',True])
    [True, 'jose', 10, 'a']

    :param lista:
    :return:
    """
    #resultado=[]
    #for i in range(-1, -len(lista) -1,-1):
    #    resultado.append(lista[i])
    #return resultado


    resultado = []
    copia = lista.copy()

    while copia:
        resultado.append(copia.pop())
    return resultado