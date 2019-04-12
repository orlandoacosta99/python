# def product_escalar(escalar, vector):
#     """
#     >>> product_escalar(2, [1, 3, 4])
#     [2, 6, 8]
#
#     :param escalar:
#     :param vector:
#     :return:
#     """
#     res=[]
#     cont=0
#
#     while cont < len(vector):
#         res.append(escalar*vector[cont])
#         cont +=1
#     return res


# vectores = {}
#
# def ingresar_vector():
#     """Permite leer un vector del ususario..."""
#     vector =[input ('Ingrese su escalaer o "s" para terminar ')]
#     while True:
#         num = input('Ingrese su escalar o "s" para terminar ')
#         if num.lower() != 's':
#             try:
#                 num= int(num)
#                 vector.append(num)
#             except:
#                 print(num, 'no es un escalar')
#         else:
#             break
#     return vector
#
# def mostrar_vecotores():
#     for vector in vectores:
#         print('nombre del vector ', vector)
# def op_producto_escalar():
#
#
# def principal( ):
#     MENSAJE = ''' Seleccione una opcion:
#     0. Salir
#     1. Ingresar valor
#     2. Producto escalar
#     '''
#     while True:
#         opcion = input(MENSAJE)
#         if opcion== '0':
#             print('Gracias')
#             break
#
#         elif opcion == '1':
#             vector = ingresar_vector()
#             vectores[vector[0]] = vector[1:]
#             print('su vector', vector[0], 'es', vectores[vector[0]])
#         elif opcion=='2':
#             mostrar_vectores()
#         elif opcion=='3':
#             op_producto_escalar()
#         else:
#             print('Seleccione una opcion valida')


# if __name__ =='__main__':
#     principal()

# def suma_vectores():

# def producto_punto():
#
# def mayor_elemento():
#
# def menor_elemento():
#
# def promedio():
#
# def desviacion_estandar():
#
# def comparar():
#
# def norma():
#
# def moda():


# def menu():
#
#     MENSAJE = ''' Seleccione una opcion:
#         0. Salir
#         1. Suma
#         2. mayor
#         3. menor
#         4. promedio
#         5. desviacion estandar
#         6. norma
#
#         '''
#     while True:
#         opcion = input(MENSAJE)
#         if opcion == '0':
#                 print('Gracias')
#                 break
#
#         elif opcion == '1':
#
#
# if __name__ =='__main__':
#     menu()