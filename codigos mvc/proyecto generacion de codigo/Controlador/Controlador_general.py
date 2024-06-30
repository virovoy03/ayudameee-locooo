

from Vista.Vista_general import Vista_general
from Controlador.Controlador_categoria import Controlador_categoria
from Controlador.Controlador_club import Controlador_club
from Controlador.Controlador_jugador import Controlador_jugador

class Controlador_general:
    def __init__(self):
        self.vista= Vista_general()
        self.controlador_club = Controlador_club()
        self.controlador_categoria = Controlador_categoria()
        self.controlador_jugador = Controlador_jugador(self.controlador_club,self.controlador_categoria)

    def cargar_archivos(self):
        self.controlador_club.cargar_club()
        #self.controlador_club.mostrar_lista_club()
        self.controlador_categoria.cargar_categoria()
        #self.controlador_categoria.mostrar_lista_categoria()
        self.controlador_jugador.cargar_jugador()
        #self.controlador_jugador.mostrar_lista_jugador()

    def iniciar(self):
        self.cargar_archivos()
        op = -1
        try:
            op = self.vista.eleccion_menu()
        except ValueError:
            self.vista.mensaje_de_error
        while op != 0:
            if op == 1:
                self.controlador_jugador.listar_jugadores_detallados()
            elif op == 2:
                self.controlador_jugador.registrar_jugador()
            elif op == 3:
                self.controlador_club.mostrar_lista_club()
                codigo = self.vista.solicitar_dato("codigo del club")
                objeto = self.controlador_club.buscar_objeto(codigo)
                self.controlador_club.lista_jugadores_del_club(objeto,self.controlador_jugador.lista_jugador)
            elif op == 4:
                self.controlador_jugador.mostrar_desempeño()
            elif op == 5:
                self.controlador_club.mostrar_lista_club()
                codigo_club = self.vista.solicitar_dato("el codigo del club")
                self.controlador_categoria.mostrar_lista_categoria()
                codigo_categoria = self.vista.solicitar_dato("el codigo de la categoria")
                objeto_club = self.controlador_club.buscar_objeto(codigo_club)
                objeto_categoria = self.controlador_categoria.buscar_objeto(codigo_categoria)
                self.controlador_jugador.mostrar_club_categoria(objeto_club,objeto_categoria)
            elif op == 6:
                self.controlador_categoria.mostrar_lista_categoria()
                codigo = self.vista.solicitar_dato("codigo de categoria")
                objeto = self.controlador_categoria.buscar_objeto(codigo)
                self.controlador_categoria.listar_jugadores_de_categoria(objeto,self.controlador_jugador.lista_jugador)
            elif op == 7:
                self.controlador_categoria.mostrar_lista_categoria()
                codigo = self.vista.solicitar_dato("codigo de categoria")
                objeto = self.controlador_categoria.buscar_objeto(codigo)
                self.controlador_categoria.listar_jugadores_detallados_por_categoria(objeto,self.controlador_jugador.lista_jugador)
            elif op == 0:
                break
                #probando git
            else:
                self.vista.mensaje_de_error()
            try:
                op = self.vista.eleccion_menu()
            except ValueError:
                self.vista.mensaje_de_error