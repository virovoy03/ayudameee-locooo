class Alumno:
    def __init__(self, dni=0, nombre="", materias=[]):
        self._dni = dni
        self._nombre = nombre
        self._aprobadas = materias

    def getDni(self):
        return self._dni

    def getNombre(self):
        return self._nombre

    def getAprobadas(self):
        return self._aprobadas

    def setDni(self, dato):
        self._dni = dato

    def setNombre(self, dato):
        self._nombre = dato

    def setAprobadas(self, dato):
        self._aprobadas = dato

    def __str__(self):
        return str(self._dni + " - " + self._nombre)
