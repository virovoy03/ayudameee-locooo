class Materia:
    def __init__(self, codigo=0, nombre="", materias=[]):
        self._codigo = codigo
        self._nombre = nombre
        self._correlativas = materias

    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def getCorrelativas(self):
        return self._correlativas

    def setCodigo(self, dato):
        self._codigo = dato

    def setNombre(self, dato):
        self._nombre = dato

    def setCorrelativas(self, dato):
        self._correlativas = dato

    def __str__(self):
        return str(self._codigo) + " - " + str(self._nombre)

    def isPosibleInscribirse(self, aprobadas):
        cant = 0
        for correlativa in self._correlativas:
            if correlativa in aprobadas:
                cant += 1
        if cant == len(self._correlativas):
            return 0
        return 1
