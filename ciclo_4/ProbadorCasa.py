from ciclo_4.poo import Casa
mi_casa = Casa('cll 123 cr 434')
casa_vecino = Casa('cll 124 cr 456')
casa_homero = Casa('Avenida Siempreviva 742, Springfield')
print( f'mi casa es {mi_casa}, la casa de mi vecino es {casa_vecino} y la casa de homero es {casa_homero}' )

# mi_casa.num_banos = 2
# mi_casa.num_abitaciones = 4

mi_casa.num_banos = 3
mi_casa.num_abitaciones = 6


setattr(casa_vecino, 'num_banos', 3)
setattr(casa_vecino, 'num_abitaciones', 6)

print(f'Mi casa tiene {mi_casa.num_abitaciones} abitaciones \n'
      f'La del veciono tiene {getattr(casa_vecino, "num_abitaciones")}')


atributos = casa_homero.__dict__

for llave in atributos:
    print(f'Atributos {llave}  con el valor {atributos[llave]} en la casa de homero')

if mi_casa == casa_vecino:
    print('mi casa y la del vecino son iguales')
else:
    print('mi casa y la del veciono son diferentes')


