matriz=[[1,2,3],
       [2,3,4],
       [5,4,6]]
# print(matriz)

# for recorrer in matriz:
#     print(recorrer)

# for fila in matriz:
    # for elemento in fila:
    #     print (elemento)

# for x in range(len(matriz)):
#     print (matriz[x])

for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        print(matriz[x][y])