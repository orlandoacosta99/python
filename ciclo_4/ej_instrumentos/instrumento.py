from ciclo_4.ej_instrumentos.Inventario import Instrumentos

class Tipo_Instrimento(Instrumentos):

    def __init__(self, nombre_instrumento, afinacion, melodia_armonica):

        super().__init__(nombre_instrumento, afinacion, melodia_armonica)

    def tipo_instrumento(self, cuerdas, percusion):
        return super().tipo_instrumento(cuerdas, percusion)


