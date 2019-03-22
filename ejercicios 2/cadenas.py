#cadena = "qwertyuiopasdfghjklñzxcvbnmwetghkl"

#for letra in cadena:
 #  print(letra)
#pizza = ['tomate', 'queso', 'peperroni', 'jamon', 'masa']

#for letra in cadena:
 #  print(letra)


def mejorar_receta(pizza, toppping):
   """

       >>> mejorar_receta(['pollo', 'carne', 'salami', 'peperoni'], "champiñon")
       c
       h
       a
       m
       p
       i
       ñ
       o
       n
       ['carne', 'champiñon', 'peperoni', 'pollo', 'salami']

       :param pizza:
       :param toppping:
       :return:
       """
   nueva_pizza = pizza.copy()
   if not (toppping in pizza):
      nueva_pizza.append(toppping)

   for pizza_nueva in toppping:
         print(pizza_nueva)

   return sorted(nueva_pizza)

def es_vocal(letra):
   """
   validar si es una letra o vocal
   >>> es_vocal('ea')
   Traceback (most recent call last):
   ..
   ValueError: ea no es una letra
   >>> es_vocal('a')
   True
   >>> es_vocal('1')
   Traceback (most recent call last):
   ..
   ValueError: 1 no es una letra

   :param letra:
   :return:
   """
   if(len(letra)==1  and letra.isalpha()):
      return letra in 'aeiouAEIOU'
   raise ValueError(letra+ ' no es una letra')

def contar_vocales(cadena):
   """
   >>> contar_vocales('hola')
   2

   :param cadena:
   :return:
   """
   cont=0
   for letras in cadena:
      if es_vocal(letras):
         cont += 1
   return cont
def cadena_consonates (cadena):
   """
   >>> cadena_consonates('hola')
   2

   :param cadena:
   :return:
   """

   cont=0
   for letra in cadena:
      if not (es_vocal(letra)):
         cont += 1
   return cont

def cadena_contar(lista):
   """
   >>> cadena_contar(['hola', 'perdido'])
   [5, 6]

   :param lista:
   :return:
   """
   vocales = 0
   consonantes = 0
   for palabra in lista:
      vocales += contar_vocales(palabra)
      consonantes += cadena_consonates(palabra)
   return [vocales, consonantes]