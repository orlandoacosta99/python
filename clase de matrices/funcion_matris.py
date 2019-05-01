from tersersemestre_vectores.menu import ingresar_vector

matrices={}

def leer_matriz():
    """
    leer una matriz por teclado
    :return:
    """
    resultado=[]

    while True:
        entrada = input('desea ingresar una fila s/n:  ')
        if entrada == 'n':
            break
        resultado.append(ingresar_vector()[1:])
        return resultado

    matriz = leer_matriz()
    print(matriz)


while True:

    Menu = """ 
    ******* Menu *******
    0. Salir
    1. Ingresar Matriz
    2. Ver Matrices
    ********************
    """
    seleccion = input(Menu)
    if seleccion == "0":
        print('Gracias')
        break
    elif seleccion == "1":
        nombre= input('cual es el nombre de su matriz: ')
        matriz = leer_matriz()
        matrices[nombre] = matriz

    elif seleccion == "2":
        print('Sus matrices son: ')
        for matriz in matrices:
            print(matriz, "=")
            print(matrices[matriz])

    elif seleccion == "3":
        print('Sus matrices cuatrada es: ')


    elif seleccion == "4":
        print('guardar matriz en un archivo plano : ')

    elif seleccion == "5":
        print('consultar: ')

    elif seleccion == "6":
        print('suma de matrices: ')
    elif seleccion == "7":
        print('producto punto: ')
    elif seleccion == "5":
        print('producto de un escalar: ')
    else:
        print('Seleccione una opcion valida')