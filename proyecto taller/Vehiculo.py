
class Vehiculo:
    def __init__(self,codigo,patente,tipo,marca,modelo,propietario):
        self.codigo = codigo
        self.patente = patente
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.propietario = propietario

    def __str__(self):
        return f"El vehiculo: {self.marca} modelo: {self.modelo} Propietario: {self.propietario}"
    
    def __repr__(self):
        return f"El vehiculo: {self.marca} modelo: {self.modelo} Propietario: {self.propietario} \n\n"