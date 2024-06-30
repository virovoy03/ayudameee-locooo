class VistaHabitacion:
    def mostrarLista(self, lista):
        print(lista)

    def mostrarHabitaciones(self, lista):
        for i in lista:
            print(i)

    def mostrarMenu(self):
        print("1-op")

    def getOpcion(self):
        return input("Ingrese una opcion: ")
