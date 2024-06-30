
class VistaPaciente:
    def mostrar(self, lista):
        print(lista)

    def mostrarPacientes(self, lista):
        for i in lista:
            print(i)

    def getcodigo(self):
        return input("Ingrese el codigo del paciente: ")
