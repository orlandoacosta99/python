class Instrumentos:

    nombre_instrumento = ''
    melodia_armonica = ''
    afinacion = ''
    tipo_instrumento = ''

    def __init__(self, nombre_instrumento, afinacion, melodia_armonica, tipo_instrumento):
        self.nombre_instrumento = nombre_instrumento
        self.afinacion = afinacion
        self.melodia_armonica = melodia_armonica
        self.tipo_instrumento = tipo_instrumento

    def tipo_instrumento(self, cuerdas, percusion):

        if (cuerdas == 'cuerdas' and cuerdas != percusion):

            tipo_ins = cuerdas()

        elif (percusion == 'persucion' and percusion != cuerdas):

            tipo_ins = percusion()
        else:

            raise ValueError('No se encuentra instrumento')

        return tipo_ins

    def cuerdas(self, n_cuerdas, esc_afinacion):
        self.n_cuerdas = n_cuerdas
        self.esc_afinacion = esc_afinacion

        # esc_afinacion = []

        if n_cuerdas < 0:
            raise ValueError('No hay cuerdas negativas')
        # else:
        #     for x in range(1, len(n_cuerdas)):
        #         nom = str(input('ingrese nombre de la cuerda'))
        #         esc_afinacion.append(nom)

        return f'{self.nombre_instrumento} tiene {n_cuerdas} cuerdas y estan afinadas en {esc_afinacion} respectivamente'

    def percusion(self, diametro, frecuencia):
        self.diametro = diametro
        self.frecuencia = frecuencia

        if diametro < 0 or frecuencia < 0:
            raise ValueError('No hay diametros ni frecuencias negativas')
        return f'el instrumento {self.nombre_instrumento} tiene un diametro de {diametro} cm y una frecuencia de vibracion de {frecuencia} Hz'