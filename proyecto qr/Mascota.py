class Mascota:
    def __init__(self, codigo, nombre, propietario, telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.propietario = propietario
        self.telefono = telefono

    def getInformacionQr(self):
        return self.telefono

    def __str__(self):
        return f"- {self.codigo} ({self.nombre})"