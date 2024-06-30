
class VistaUsuario:
    def solicitar_nombre_usuario(self):
        return input("ingrese el nombre del usuario")
    
    def solicitar_correo_usuario(self):
        return input("ingrese el correo del usuario")
    
    def mostrar_informacion(self,data):
        print("Informacion del usuario:")
        print(f"Nombre:{data['nombre']} - Correo: {data['correo']}")