from tersersemestre_vectores.vectores import *

vectores = {}

def ingresar_vector():
    """
    Permite leer un vector del usuario

    :return: list of num el vector ingresado por el usuario
    """
    vector = [input('¿Cual es el nombre de su vector? ')]

    while True:
        num = input('Ingrese su escalar o "s" para terminar ')
        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print(num, 'no es un escalar')
        else:
            break
    print('su vector', vector[0], 'es', vector[1:])
    return vector


def mostrar_vectores():
    for nombre in vectores:
        print(nombre, 'contiene', vectores[nombre])

def op_producto_escalar():
    while True:
        escalar = input('Ingrese su escalar ')
        try:
            escalar = int(escalar)
            break
        except:
            print(escalar, 'no es un escalar')

    print('Cual es el nombre de su vector')
    mostrar_vectores()
    seleccion = input()

    print('El producto escalar es', producto_escalar(escalar, vectores[seleccion]))

    nombreVector = input('Indique el nombre del vector: ')

    print('El vector', nombreVector, 'contiene', vectores[nombreVector])


def Suma_vectores():

    while True:
        vector1 = input('Indique el nombre del vector 1: ')
        print('El vector 1', vector1, 'contiene', vectores[vector1])

        vector2 = input('Indique el nombre del vector 2: ')
        print('El vector 2', vector2, 'contiene', vectores[vector2])

        if len(vectores[vector1]) == len(vectores[vector2]):
            print('La suma de los vectores es:', suma_productos(vectores[vector1], vectores[vector2]))
            break
        else:
            print('Los vectores no tiene la misma longitud.')


def Producto_punto ():

    while True:
        vector1 = input('Indique el nombre del vector 1: ')
        print('El vector 1', vector1, 'contiene', vectores[vector1])

        vector2 = input('Indique el nombre del vector 2: ')
        print('El vector 2', vector2, 'contiene', vectores[vector2])

        if len(vectores[vector1]) == len(vectores[vector2]):
            print('El producto punto de los vectores es:', producto_puntos(vectores[vector1], vectores[vector2]))
            break
        else:
            print('Los vectores no tiene la misma longitud.')

def Mayor_elemento():

        vector = input('Indique el nombre del vector: ')
        print('El vector ', vector, 'contiene', vectores[vector])
        print('El mayor elemento del vector es: ', elemento_mayor(vectores[vector]))

def Menor_elemento ():

    vector = input('Indique el nombre del vector: ')
    print('El vector ', vector, 'contiene', vectores[vector])
    print('El menor elemento del vector es: ', elemento_menor(vectores[vector]))

def Promedio ():

    vector = input('Indique el nombre del vector: ')
    print('El vector ', vector, 'contiene', vectores[vector])
    print('El promedio del vector es: ', prom(vectores[vector]))

def Desviacion_estandar():
    vector = input('Indique el nombre del vector: ')
    print('El vector ', vector, 'contiene', vectores[vector])
    print('La desviacion estandar del vector es: ', desviacion_est(vectores[vector]))

def Comparar ():
    vector = input('Indique el nombre del vector: ')
    print('El vector ', vector, 'contiene', vectores[vector])
    print('El mayor elemento del vector es: ', elemento_mayor(vectores[vector]))
    print('El menor elemento del vector es: ', elemento_menor(vectores[vector]))
    print('El elemento igual del vector es: ', elemento_igual(vectores[vector]))

def Norma ():
    vector = input('Indique el nombre del vector: ')
    print('El vector ', vector, 'contiene', vectores[vector])
    print('La norma del vector es: ', Norma_vec(vectores[vector]))


def Moda():
    vector = input('Indique el nombre del vector: ')
    print('El vector ', vector, 'contiene', vectores[vector])
    print('La moda del vector es: ', Moda_vec(vectores[vector]))



def principal():

    MENSAJE = '''Seleccione una opcion:
    0. Salir
    1. Ingresar Vector
    2. Mostrar Vectores
    3. Producto escalar
    4. Suma de vectores
    5. Producto punto
    6. Mayor elemnto
    7. Menor elemento
    8. Promedio
    9. Desviación estandar
    10. Comparar
    11. Norma
    12. Moda del vector
    '''

    while True:
        opcion = input(MENSAJE)

        if opcion == '0':
            print('Gracias')
            break
        elif opcion == '1':
            vector = ingresar_vector()
            vectores[vector[0]] = vector[1:]

        elif opcion == '2':
            mostrar_vectores()

        elif opcion == '3':
            op_producto_escalar()

        elif opcion == '4':
            Suma_vectores()

        elif opcion == '5':
            Producto_punto()

        elif opcion == '6':
            Mayor_elemento()

        elif opcion == '7':
            Menor_elemento()

        elif opcion == '8':
            Promedio()

        elif opcion == '9':
            Desviacion_estandar()

        elif opcion == '10':
            Comparar()

        elif opcion == '11':
            Norma()

        elif opcion == '12':
            Moda()

        elif opcion == '13':
            Media()

        else:
            print('Seleccione una opcion valida')


if __name__ == '__main__':
    principal()