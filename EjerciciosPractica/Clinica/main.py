from Paciente import Paciente
from Habitacion import Habitacion

habitaciones = []
pacientes = []

def buscarHabitacion(numero):
    for h in habitaciones:
        if(h.numero==int(numero)):
            return h

def buscarPaciente(nombre):
    for p in pacientes:
        if(p.nombre==nombre):
            return p

def cargar_pacientes():
    with open("pacientes.txt", 'r') as f:
        for linea in f:
            datos = linea.strip().split(',')
            nombre = datos[0]
            edad = datos[1]
            numeroHabitacion = datos[2]
            habitacion = buscarHabitacion(numeroHabitacion)
            paciente = Paciente(nombre, edad, habitacion)
            pacientes.append(paciente)

def cargar_habitaciones_desde_archivo():
    with open("habitacion.txt", 'r') as f:
        for linea in f:
            datos = linea.strip().split(',')
            numero = int(datos[0])
            enfermera = datos[1]
            ubicacion = datos[2]
            camas = int(datos[3])
            estado = datos[4]
            ocupacion = int(datos[5])
            habitacion = Habitacion(numero, enfermera, ubicacion, camas, estado, ocupacion)
            habitaciones.append(habitacion)

def visualizar_habitaciones():
    print("Habitaciones:")
    for habitacion in habitaciones:
        print(f"Número: {habitacion.numero}, Estado: {habitacion.estado}, Camas disponibles: {habitacion.camas_disponibles()}")
def listar_habitaciones_con_camas_disponibles():
    print("Habitaciones con camas disponibles:")
    for habitacion in habitaciones:
        if habitacion.camas_disponibles() > 0:
            print(f"Número: {habitacion.numero}, Camas disponibles: {habitacion.camas_disponibles()}")

def registrar_paciente_en_habitacion(paciente, habitacion):
    paciente.habitacion.sacar_paciente() #lo saco al pacientes.txt de esa habitacion
    habitacion.registrar_paciente() #ocupo una cama mas en la habitacion
    paciente.habitacion = habitacion #cambio al pacientes.txt de habitacion

def main():
    cargar_habitaciones_desde_archivo()
    cargar_pacientes()

    while True:
        print("\n1. Visualizar habitaciones")
        print("2. Consultar Habitaciones Disponibles")
        print("3. Registrar Paciente en Habitacion")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            visualizar_habitaciones()
        elif opcion == '2':
            listar_habitaciones_con_camas_disponibles()
        elif opcion == '3':
            nombre=input("Ingrese el nombre del pacientes.txt")
            numero = input("Ingrese el numero de habitacion asignada")
            registrar_paciente_en_habitacion(buscarPaciente(nombre),buscarHabitacion(numero))
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


    visualizar_habitaciones()



    opcion = input("¿Desea listar solo las habitaciones con camas disponibles? (s/n): ")
    if opcion.lower() == 's':
        listar_habitaciones_con_camas_disponibles()


    habitacion_seleccionada = int(input("Ingrese el número de la habitación donde desea registrar al pacientes.txt: "))
    registrar_paciente_en_habitacion(paciente, habitacion_seleccionada)

if __name__ == '__main__':
    main()
