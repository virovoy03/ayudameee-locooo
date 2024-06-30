class Vehiculo:
    def __init__(self, codigo, nombre, patente, tipo, marca, modelo, propietario):
        self.codigo = codigo
        self.nombre = nombre
        self.patente = patente
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.propietario = propietario


    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Patente: {self.patente}, Tipo: {self.tipo}"

    def __repr__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Patente: {self.patente}, Tipo: {self.tipo}"


class Propietario:
    def __init__(self, codigo, nombre, telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return (
            f"Código: {self.codigo}, Nombre: {self.nombre}, Teléfono: {self.telefono}"
        )

    def __repr__(self):
        return (
            f"Código: {self.codigo}, Nombre: {self.nombre}, Teléfono: {self.telefono}"
        )


class Modelo:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"Código: {self.codigo}, Modelo: {self.nombre}"

    def __repr__(self):
        return f"Código: {self.codigo}, Modelo: {self.nombre}"


class Marca:
    def __init__(self, codigo, marca):
        self.codigo = codigo
        self.marca = marca

    def __str__(self):
        return f"Código: {self.codigo}, Marca: {self.marca}"

    def __repr__(self):
        return f"Código: {self.codigo}, Marca: {self.marca}"
