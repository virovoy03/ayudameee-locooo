
class Vista_general:
    
    def eleccion_menu(self):
        print("Menu: \n1-Listado de jugadores"
              "\n2-Registro de jugador"
              "\n3-listado por club"
              "\n4-Evaluciones de desempeño"
              "\n5-consultar categoria y club"
              "\n6-mostrar cantidad por categoria"
              "\n7-mostrar detalles por categoria"
              "\n0-Salir")
        op = int(input("ingrese la opcion deseada: "))
        return op
    
    def mensaje_de_error(self):
       print("no ingreso un valor adecuado")

    def solicitar_dato(self,nombre_dato):
        return input("ingrese "+nombre_dato+" del jugador: ")