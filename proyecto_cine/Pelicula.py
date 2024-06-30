
class Pelicula:
    def __init__(self,nombre,precio_general,habilitada,semanal):
        self.nombre = nombre
        self.precio_general = precio_general
        self.__habilitada = habilitada
        self.semanal = semanal
    def is_habilitado(self):
        if self.__habilitada ==1:
            return False
        else:
            return True
    def __str__(self):
        return self.nombre
    #si se quiere mostar algo dentro de una lista se usa rpr
    def __repr__(self):
        return self.nombre