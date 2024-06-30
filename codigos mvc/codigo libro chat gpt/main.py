
class Cliente:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail
        self.reclamos = []

class Reclamo:
    def __init__(self, cliente, servicio, detalle, fecha):
        self.cliente = cliente
        self.servicio = servicio
        self.detalle = detalle
        self.fecha = fecha
        self.estado = "registrado"

class Sistema:
    def __init__(self):
        self.clientes = []
        self.reclamos = []

    def agregar_cliente(self, nombre, telefono, mail):
        cliente = Cliente(nombre, telefono, mail)
        self.clientes.append(cliente)
        return cliente

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    def agregar_reclamo(self, cliente, servicio, detalle, fecha):
        reclamo = Reclamo(cliente, servicio, detalle, fecha)
        cliente.reclamos.append(reclamo)
        self.reclamos.append(reclamo)

    def cambiar_estado_reclamo(self, reclamo, nuevo_estado):
        reclamo.estado = nuevo_estado

    def contar_reclamos_por_estado(self, estado):
        return sum(1 for reclamo in self.reclamos if reclamo.estado == estado)

