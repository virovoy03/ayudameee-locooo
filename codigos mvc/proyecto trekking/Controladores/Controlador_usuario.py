
from Modelos.Usuario import Usuario

from Vistas.Vista_usuario import Vista_usuario

class Controlador_usuario:
    def __init__(self):
        self.vista = Vista_usuario() 
        self.lista_usuarios = []

    def cargar_archivos(self):
        with open("usuarios.txt") as archivo:
            lineas = archivo.readlines
        for r in lineas:
            nombre,apellido,dni = r.strip().split(";")
            self.lista_usuarios.append(Usuario(nombre,apellido,dni))
            