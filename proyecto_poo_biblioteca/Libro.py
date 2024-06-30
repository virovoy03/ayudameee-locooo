
class Libro:
    def __init__(self, titulo, autor, num_ejemplares, num_prestados):
        self.titulo = titulo
        self.autor = autor
        self.num_ejemplares = num_ejemplares
        self.num_prestados = num_prestados

    def puede_prestarse(self):
        return self.num_ejemplares > self.num_prestados

    def prestar(self):
        if self.puede_prestarse():
            self.num_prestados += 1
            return True
        else:
            return False

    def devolver(self):
        if self.num_prestados > 0:
            self.num_prestados -= 1
            return True
        else:
            return False

