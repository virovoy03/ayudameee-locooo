
from Vista.Vista_club import Vista_club
from Modelo.Club import Club

class Controlador_club:
    def __init__(self):
        self.vista = Vista_club()
        self.lista_club = []
    
    def cargar_club(self):
        with open("clubes.txt") as archivo:
           lineas = archivo.readlines() 
        for i in lineas:
            codigo,denominacion = i.strip().split(",")
            self.lista_club.append(Club(codigo,denominacion))

    def mostrar_lista_club(self):
        self.vista.listar(self.lista_club)

    def buscar_objeto(self,codigo):
        for o in self.lista_club:
            if o.codigo == codigo:
                return o
            
    def lista_jugadores_del_club(self,club,lista):
        lista = club.get_lista_jugadores(lista)
        self.vista.listar_detalle(lista)