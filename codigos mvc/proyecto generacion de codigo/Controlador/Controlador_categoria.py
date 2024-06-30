
from Vista.Vista_categoria import Vista_categoria
from Modelo.Categoria import Categoria

class Controlador_categoria:
    def __init__(self):
        self.vista = Vista_categoria()
        self.lista_categoria = []
    
    def cargar_categoria(self):
        with open("categorias.txt") as archivo:
           lineas = archivo.readlines() 
        for i in lineas:
            codigo,denominacion = i.strip().split(",")
            self.lista_categoria.append(Categoria(codigo,denominacion))

    def mostrar_lista_categoria(self):
        self.vista.listar(self.lista_categoria)

    def buscar_objeto(self,codigo):
        for o in self.lista_categoria:
            if o.codigo == codigo:
                return o
    
    def listar_jugadores_de_categoria(self,categoria,lista):
        self.vista.mostrar_info(categoria.get_cantidad_jugadores_categoria(lista))

    def listar_jugadores_detallados_por_categoria(self,categoria,lista):
        self.vista.listar_detalle(categoria.get_lista_jugadores(lista))