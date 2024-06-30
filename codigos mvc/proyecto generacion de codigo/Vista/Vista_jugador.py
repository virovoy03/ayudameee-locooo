
class Vista_jugador:
    
    def listar(self,lista):
        print(lista)

    def listar_detalle(self,lista):
        for i in lista:
            print(i.get_mostrar_informacion())
    
    def pedir_dato(self,nombre_dato):
        return input("ingrese "+nombre_dato+" del jugador: ")
    
    def mostrar(self,info):
        print(info)
        