def mejorar_receta(pizza, toppping):
    """

    >>> mejorar_receta(['pollo', 'carne', 'salami', 'peperoni'], "champiñon")
    ['carne', 'champiñon', 'peperoni', 'pollo', 'salami']

    :param pizza:
    :param toppping:
    :return:
    """
    nueva_pizza=pizza.copy()
    if not (toppping in pizza):

         nueva_pizza.append(toppping)

    return sorted(nueva_pizza)

#######################################################################################

def doble_queso(pizza):
    """
    >>> doble_queso(['carne', 'salami', 'peperoni'])
    ['queso', 'carne', 'salami', 'peperoni', 'queso']
    >>> doble_queso(['queso', 'jamon', 'pollo'])
    ['queso', 'jamon', 'pollo', 'queso']
    >>> doble_queso(['carne', 'salami','pollo'])
    ['queso', 'carne', 'salami', 'pollo', 'queso']

    :param pizza:
    :return:
    """
    nueva_pizza = pizza.copy()

    if not nueva_pizza[0]=='queso':
        nueva_pizza.insert(0, 'queso')
    if not ('queso'== nueva_pizza[-1]):
        nueva_pizza.append('queso')
    return nueva_pizza































































































































