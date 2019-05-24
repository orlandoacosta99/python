class Instrumentos:

    nombre_instrumento = ''
    tipo_instrumento = ''
    n_instrumentos = 0

    def __init__(self, nombre_instrumento, tipo_instrumento, n_instrumentos):
        self.nombre_instrumento = nombre_instrumento
        self.tipo_instrumento = tipo_instrumento
        self.n_instrumentos = n_instrumentos

    afinacion = ''
    melodia = ''
    def clas_instrumento(self, afinacion, melodia):
        self.afinacion = afinacion
        self.melodia = melodia


        if (self.tipo_instrumento == 'cuerdas'):
            return f'el instrumento {self.nombre_instrumento} es de {self.tipo_instrumento}, tiene afinacion {self.afinacion} y melodia {self.melodia}'

        elif (self.tipo_instrumento == 'percusion'):

            return f'el instrumento {self.nombre_instrumento} es de {self.tipo_instrumento} y tiene melodia {self.melodia}'
        else:

            raise ValueError('No se encuentra el tipo de instrumento')

    def cantidad(self):
        if self.n_instrumentos < 0:
            raise ValueError('el numero de instrumentos es negativo')

        return f'el instrumento {self.nombre_instrumento} es de {self.tipo_instrumento} y tinene la cantidad de {self.n_instrumentos} instrumentos'

class Cuerdas(Instrumentos):
    n_cuerdas = 0
    esc_afinacion = ''

    def cuerdas(self, n_cuerdas, esc_afinacion):
        #super(Cuerdas, self).__init__(nombre_instrumento, tipo_instrumento, n_instrumentos, n_cuerdas, esc_afinacion)
        self.n_cuerdas = n_cuerdas
        self.esc_afinacion = esc_afinacion

        if self.n_cuerdas < 0:
            raise ValueError(f'el {self.nombre_instrumento} no puede tener cuerdas negativas')
        return f'el instrumento {self.nombre_instrumento}  es de {self.tipo_instrumento}, tiene {self.n_cuerdas} cuerdas y estan afinadas en {self.esc_afinacion} y tiene  la cantidad de {self.n_instrumentos} instrumentos'

class Percusion(Instrumentos):
    diametro = 0
    frecuencia = 0

    def percusion(self, diametro, frecuencia):

        self.diametro = diametro
        self.frecuencia = frecuencia

        if diametro < 0 or frecuencia < 0:
            raise ValueError('No hay diametros ni frecuencias negativas')

        return f'el instrumento {self.nombre_instrumento} es de {self.tipo_instrumento},  tiene un diametro de {diametro} cm y una frecuencia de vibracion es de {frecuencia} hz y tiene  la cantidad de {self.n_instrumentos} instrumentos'