class VistaInscripcion:
    def mostrarBienvenida(self):
        print("Bienvenida")

    def getLegajoAlumno(self):
        return input("Ingrese el legajo del alumno: ")

    def getCodigoMateria(self):
        return input("Ingrese el codigo de la materia: ")

    def mostrarDato(self, dato):
        print("Datos desde la inscripción")
        print(dato)
