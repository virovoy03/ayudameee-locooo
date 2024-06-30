class Libro:
    def __init__(self, titulo, autor, ejemplares_total, ejemplares_prestados):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_total = ejemplares_total
        self.ejemplares_prestados = ejemplares_prestados


    def disponible_para_prestamo(self):
        return self.ejemplares_prestados < self.ejemplares_total


    def prestar(self):
        if self.disponible_para_prestamo():
            self.ejemplares_prestados += 1
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"No hay ejemplares disponibles del libro '{self.titulo}'.")


    def devolver(self):
        if self.ejemplares_prestados > 0:
            self.ejemplares_prestados -= 1
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"No hay ejemplares prestados del libro '{self.titulo}'.")

    def __str__(self):
        return f"- {self.titulo} ({self.autor})"