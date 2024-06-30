

class Vista_club:
    
    def listar(self,lista):
        print(lista)

    def listar_detalle(self,lista):
        for i in lista:
            print(i.get_mostrar_informacion())
