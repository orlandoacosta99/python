import math
def area_circulo(radio):
    '''
     (num) -> float
    Calcula el area de un circulo dado el radio

     >>> area_circulo(1)
     3.141592653589793

    :param radio: num que representa el radio del circulo
    :return:  float que representa el area del circulo
    '''
    area = radio * math.pi
    return area