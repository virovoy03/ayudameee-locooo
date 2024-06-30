class Socio:
    def __init__(self, codigo, nombre, apellido, estado, listaSociosHabilitados=[]):
        self._codigo = codigo
        self._nombre = nombre
        self._apellido = apellido
        self._estado = estado
        self._listaSociosHabilitados = listaSociosHabilitados

    def __str__(self):
        return f"Código de socio: {self._codigo}, nombre: {self._nombre}, apellido: {self._apellido}, estado: {self._estado}"

    def __repr__(self):
        return f"Código de socio: {self._codigo}, nombre: {self._nombre}, apellido: {self._apellido}, estado: {self._estado}"

    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def getApellido(self):
        return self._apellido

    def getEstado(self):
        return self._estado

    def isHabilitado(self):
        if self._model.getEstado() == "1":
            return "Habilitado"
        return "No habilitado"
