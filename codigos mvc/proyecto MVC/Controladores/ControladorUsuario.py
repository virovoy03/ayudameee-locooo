
from Modelos.Usuario import Usuario

class Controlador:
    def __init__(self,vista):
        self.vista = vista
    
    def crear_nuevo_objeto(self):
        self.modelo = Usuario(
            self.vista.solicitar_nombre_usuario(),
            self.vista.solicitar_correo_usuario()
        )

    def actualizar_informacion(self):
        self.modelo.nombre = self.vista.solicitar_nombre_usuario(),
        self.modelo.correo = self.vista.solicitar_correo_usuario()
    
    def mostrar_informacion(self):
        data = self.modelo.get_info_usuario()
        self.vista.mostrar_informacion(data)
        

    

