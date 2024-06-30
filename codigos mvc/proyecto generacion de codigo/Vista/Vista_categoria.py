
class Vista_categoria:
    
    def listar(self,lista):
        print(lista)

    def mostrar_info(self,info):
        print(info)

    def listar_detalle(self,lista):
        for i in lista:
            print(i.get_mostrar_informacion())