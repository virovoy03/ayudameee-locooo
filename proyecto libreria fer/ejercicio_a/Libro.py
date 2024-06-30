class Libro:
    def __init__(self, t, a, n, np):
        self.titulo = t
        self.autor = a
        self.num_ejemplares = n
        self.num_prestados = np

    def __repr__(self):
        return f'{self.titulo} {self.autor} {self.num_ejemplares} {self.num_prestados}'

    def esPosiblePrestar(self):
        return self.num_prestados < self.num_ejemplares

    def prestarLibro(self):
        if self.esPosiblePrestar():
            self.num_prestados += 1
            print("Libro prestado")
        else:
            print("el libro no puede ser prestado")

    def devolverLibro(self):
        if self.num_prestados >0:
            self.num_prestados -= 1
            print("Libro devuelto")



