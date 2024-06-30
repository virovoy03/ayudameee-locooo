class Libro:
    def __init__(self, codigo, titulo, autor, cantEjemPrest, cantEjem):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._cantEjemPrest = cantEjemPrest
        self._cantEjem = cantEjem

    def __str__(self):
        return f"Código: {self._codigo}, título: {self._titulo}, autor: {self._autor}, cantidad de ejemplares: {self._cantEjem}"

    def __repr__(self):
        return f"Código: {self._codigo}, título: {self._titulo}, autor: {self._autor}, cantidad de ejemplares: {self._cantEjem}"

    def getCodigo(self):
        return self._codigo

    def getTitulo(self):
        return self._titulo

    def getAutor(self):
        return self._autor

    def getCantPrest(self):
        return self._cantEjemPrest

    def getCantEjem(self):
        return self._cantEjem

    def setCantPrest(self, dato):
        self._cantEjemPrest = dato
        return self._cantEjemPrest

    def setCantEjem(self, dato):
        self._cantEjem = dato
        return self._cantEjem

    def poseeEjemPrest(self):
        pass
