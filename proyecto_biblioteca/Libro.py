
class libro:
    def __init__(self,nombre,autor,cant_ejemplares,cant_prestados):
        self.nombre = nombre
        self.autor = autor
        self.cant_ejemplares = cant_ejemplares
        self.cant_prestados = cant_prestados

    def __str__(self):
        return self.nombre
    
    def is_posible_prestar(self):
        return self.cant_prestados < self.cant_ejemplares

    def prestar(self):
        if self.is_posible_prestar():
            self.cant_prestados += 1
        else:
            print("no se puede prestar") 

    def devolver(self):
        pass

    
