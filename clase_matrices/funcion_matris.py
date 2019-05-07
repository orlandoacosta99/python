from Semana_10.menu import ingresar_vector
from clase_matrices  import uso_archivos


matrices = uso_archivos.leer('Matrices.json')

def leer_matriz():
    """
    leer una matriz por teclado
    :return:
    """
    resultado = []
    while True:
        entrada = input('Desea ingresar una fila? s/n ')
        if entrada == 'n':
            break
        resultado.append(ingresar_vector()[1:])
    return resultado

while True:


    MENU = """
    **********Menu**********
    0. Salir
    1. Ingresar Matriz
    2. Ver Matrices
    ************************
    """

    seleccion = input(MENU)
    if seleccion == '0':
        print('Suerte')
        uso_archivos.guardar('Matrices.json', matrices)

        break
    elif seleccion == "1":
        nombre = input('cual es el nombre de su matriz ')
        matriz = leer_matriz()
        matrices[nombre[0]] = matriz

    elif seleccion == "2":
        print('Sus matrices')
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