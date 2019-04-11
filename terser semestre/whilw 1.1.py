# dato = 0
# while dato % 2 == 0:
#     dato = input("ingrese un dato ")
#     print (dato)
#
#     try:
#         dato=int(dato)
#     except:
#         dato=2

# while True:
#     dato = input("ingrese un dato ")
#     print (dato)
#     if dato.isnumeric() and int(dato) % 2 !=0:
#         break

lista=[]
while True:
    dato = input("ingrese ingredientes ")
    if (str != dato):
        datos = dato.lower()
        print(dato)
        lista.append(datos)
        if (datos == 'no mas'):
            lista.pop()
            print (lista)
            break
