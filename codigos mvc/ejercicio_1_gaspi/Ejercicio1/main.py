
from Controllers.ControladorHabitacion import ControladorHabitacion
from Controllers.ControladorPaciente import ControladorPaciente

def main():
    controladorPaciente = ControladorPaciente()
    controladorPaciente.iniciar()
    controlador = ControladorHabitacion(controladorPaciente)
    controlador.iniciar()
    controlador.mostrarMenu()

if __name__ == "__main__":
    main()
