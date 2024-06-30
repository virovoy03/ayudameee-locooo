class Persona:
    def __init__(self, c, n, e, t):
        self.codigo = c
        self.__nombre = n
        self.telefono = t
        self.estado = e

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    def get_datos_contacto(self):
        return f"{self.codigo} Nombre: {self.nombre} - Telefono: {self.telefono}"

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

class Cliente(Persona):
    def __init__(self, c, n, e, t,mail):
        super().__init__(c,n,e,t)
        self.mail=mail
        self.disfraces_alquilados = []

    def get_datos_contacto(self):
        return f"Nombre: {self.nombre} - E-mail: {self.mail}"

    def alquilar_disfraz(self, disfraz):
        self.disfraces_alquilados.append(disfraz)

    def devolver_disfraz(self, disfraz):
        if disfraz in self.disfraces_alquilados:
            self.disfraces_alquilados.remove(disfraz)

    def __str__(self):
        return self.codigo + " / "+self.nombre + " " + self.mail

    def __repr__(self):
        return self.codigo + " / "+self.nombre + " " + self.mail


class Encargado(Persona):
    def __init__(self, c, n, e, t, legajo):
        super().__init__(c, n, e, t)
        self.legajo = legajo

    def __str__(self):
        return self.codigo + " / "+self.nombre + " " + self.legajo

    def __repr__(self):
        return self.codigo + " / "+self.nombre + " " + self.legajo