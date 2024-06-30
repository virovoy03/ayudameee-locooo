
class Jugador:
    def __init__(self,dni,apellido_nombre,club,categoria,goles,amonestaciones,expulsiones):
        self.dni = dni
        self.apellido_nombre = apellido_nombre
        self.club = club
        self.categoria = categoria
        self.goles = goles
        self.amonestaciones = amonestaciones
        self.expulsiones = expulsiones  

    def get_mostrar_informacion(self):
        return (f"Dni: {self.dni} - Apellido y Nombre: {self.apellido_nombre} - Club: {self.club.__str__()} - Categoria: {self.categoria.__str__()} - Goles: {self.goles} - Amonestaciones: {self.amonestaciones} - Expulsiones: {self.expulsiones} ")  
    
    def get_puntos_desempeño(self):
        return int(self.goles)*10-int(self.amonestaciones)*2-int(self.expulsiones)*5

    def get_datos_desempeño(self):
        return (f"Dni: {self.dni} - Apellido y Nombre: {self.apellido_nombre} - Club: {self.club.__str__()} - Categoria: {self.categoria.__str__()} - puntos: {self.get_puntos_desempeño()}")
    
    def __str__(self):
        return self.apellido_nombre
    
    def __repr__(self):
        return self.apellido_nombre