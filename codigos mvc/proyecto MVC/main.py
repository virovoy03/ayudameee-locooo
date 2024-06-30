
from Vistas.VistaUsuario import VistaUsuario
from Controladores.ControladorUsuario import Controlador

def llamada_controlador_usuario():
    controlador = Controlador(VistaUsuario())
    controlador.crear_nuevo_objeto()
    controlador.mostrar_informacion()
    controlador.actualizar_informacion()
    controlador.mostrar_informacion()

def main():
    llamada_controlador_usuario()

if __name__ == "__main__":
    main()
