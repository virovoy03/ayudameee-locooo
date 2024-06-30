class Prestamo:
    def __init__(self, codigo, socio, libro, cantDias):
        self._codigo = codigo
        self._socio = socio
        self._libro = libro
        self._cantDias = cantDias

    def __str__(self):
        return f"Código del prestamo: {self._codigo}, socio: {self._socio}, libro: {self._libro}, cantidad de días prestado: {self._cantDias}"

    def __repr__(self):
        return f"Código del prestamo: {self._codigo}, socio: {self._socio}, libro: {self._libro}, cantidad de días prestado: {self._cantDias}"

    def getCodigo(self):
        return self._codigo

    def getSocio(self):
        return self._socio

    def getLibro(self):
        return self._libro

    def getCantDias(self):
        return self._cantDias
