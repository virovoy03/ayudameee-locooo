
class Vehiculo:
    def __init__(self,codigo,patente,tipo,marca=None,modelo=None,propietario=None):
        self.codigo = codigo
        self.patente = patente
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.propietario = propietario

    def __str__(self):
        return str(self.codigo)+"-"+self.nombre

    def __repr__(self):
        return self.nombre