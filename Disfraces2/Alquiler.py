class Alquiler:
    def __init__(self, c, disfraz, cliente,encargado,total=0):
        self.codigo = c
        self.disfraz = disfraz
        self.cliente = cliente
        self.encargado = encargado
        self.total = total


    def __str__(self):
        return self.codigo + " / "+self.cliente.__str__() + " / "+ self.encargado.__str__() + " $"+ str(self.total)

    def __repr__(self):
        return self.codigo