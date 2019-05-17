from ciclo_4.poo import Punto

punto1 = Punto(5, 2)
# punto2 = Punto(5, 2)
punto2 = Punto(8, 5)

print(f'las cordenadas del punto uno son {punto1} y las cordenadas del punto dos son {punto2}')

if punto1 == punto2:
    print('los puntos son iguales')
else:
    print('los puntos son diferentes')

print(punto1.desplazarX(5))

print(punto1.desplazarY(2))

print('la pendiente de los puntos es', Punto.hallar_pendiente(punto1, punto2))

print('la pendiente de los puntos es', Punto.hallar_distancia(punto1, punto2))