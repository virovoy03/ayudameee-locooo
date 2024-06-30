
class Mueble:
    def __init__(self,nombre,estado,codigo,url):
        self.nombre = nombre
        self.estado = estado
        self.codigo = codigo
        self.url = url
        
    def is_habilitado(self):
        return self.estado == 1
    
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.nombre