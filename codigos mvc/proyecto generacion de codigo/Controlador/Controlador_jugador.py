
from Vista.Vista_jugador import Vista_jugador
from Modelo.Jugador import Jugador

from Controlador.Controlador_club import Controlador_club
from Controlador.Controlador_categoria import Controlador_categoria

class Controlador_jugador:
    def __init__(self,controlador_club,controlador_categoria):
        self.vista = Vista_jugador()
        self.lista_jugador = []
        self.controlador_club = controlador_club
        self.controlador_categoria = controlador_categoria        
    
    def cargar_jugador(self):
        with open("jugadores.txt") as archivo:
           lineas = archivo.readlines() 
        for i in lineas:
            dni,apellido_nombre,codigo_club,codigo_categoria,goles,amonestaciones,expulsiones = i.strip().split(",")
            objeto_club = self.controlador_club.buscar_objeto(codigo_club)
            objeto_categoria = self.controlador_categoria.buscar_objeto(codigo_categoria)
            self.lista_jugador.append(Jugador(dni,apellido_nombre,objeto_club,objeto_categoria,goles,amonestaciones,expulsiones))

    def mostrar_lista_jugador(self):
        self.vista.listar(self.lista_jugador)

    def listar_jugadores_detallados(self):
        self.vista.listar_detalle(self.lista_jugador)

    def registrar_jugador(self):
        dni = self.vista.pedir_dato("dni")
        apellido_nombre = self.vista.pedir_dato("apellido y nombre")
        self.controlador_club.mostrar_lista_club()
        codigo_club = self.vista.pedir_dato("el codigo del club")
        self.controlador_categoria.mostrar_lista_categoria()
        codigo_categoria = self.vista.pedir_dato("el codigo de la categoria")
        goles = self.vista.pedir_dato("goles")
        amonestaciones = self.vista.pedir_dato("amonestaciones")
        expulsiones = self.vista.pedir_dato("expulsiones")
        objeto_club = self.controlador_club.buscar_objeto(codigo_club)
        objeto_categoria = self.controlador_categoria.buscar_objeto(codigo_categoria) 
        self.lista_jugador.append(Jugador(dni,apellido_nombre,objeto_club,objeto_categoria,goles,amonestaciones,expulsiones))

    def mostrar_desempeño(self):
        for i in self.lista_jugador:
            self.vista.mostrar(i.get_datos_desempeño())

    def mostrar_club_categoria(self,club,categoria):
        lista_jugadores_club_categoria = []
        for i in self.lista_jugador:
            if i.club.codigo == club.codigo and i.categoria.codigo == categoria.codigo:
                lista_jugadores_club_categoria.append(i)
        self.vista.listar_detalle(lista_jugadores_club_categoria)