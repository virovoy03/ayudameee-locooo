class Pieza:
    def __init__(self,c,n,e,p):
        self.codigo=c
        self.nombre = n
        self.estado = e
        self.precio = p
       # self.disfraz = d

    def __str__(self):
        return str(self.codigo)+"-"+self.nombre

    def __repr__(self):
        return self.nombre


class Disfraz:
    def __init__(self, c, n, e,cat):
        self.codigo = c
        self.nombre = n
        self.estado = e
        self.categoria = cat
        self.piezas = []

    def getPrecio(self):
        total=0
        for p in self.piezas:
            total+=int(p.precio)
        return total

    def __str__(self):
        return str(self.codigo) + " / "+self.nombre + self.piezas.__str__() + " $"+ str(self.getPrecio())

    def __repr__(self):
        return str(self.codigo) + " / "+self.nombre

class Categoria:
    def __init__(self, c, n, e):
        self.codigo = c
        self.nombre = n
        self.estado = e

    def __str__(self):
        return str(self.codigo)+"-"+self.nombre

    def __repr__(self):
        return self.nombre