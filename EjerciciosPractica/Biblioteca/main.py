from Libro import Libro

libros = []

def cargar_libros_desde_archivo():
    with open("libros.txt", 'r') as f:
        for linea in f:
            datos = linea.strip().split(',')
            titulo, autor, ejemplares_total, ejemplares_prestados = datos
            libro = None#Libro(titulo, autor, int(ejemplares_total), int(ejemplares_prestados))
            if(libro):
                libros.append(libro)


def consultar_libros_disponibles():
    libros_disponibles = [libro for libro in libros if libro.disponible_para_prestamo()]
    if libros_disponibles:
        print("Libros disponibles para préstamo:")
        for libro in libros_disponibles:
            print(libro)
    else:
        print("No hay libros disponibles para préstamo en este momento.")


def prestar_libro(titulo):
    for libro in libros:
        if libro.titulo == titulo:
            libro.prestar()
            return
    print(f"No se encontró el libro '{titulo}' en la biblioteca.")


def devolver_libro(titulo):
    for libro in libros:
        if libro.titulo == titulo:
            libro.devolver()
            return
    print(f"No se encontró el libro '{titulo}' en la biblioteca.")


def main():

    cargar_libros_desde_archivo()

    while True:
        print("\n1. Consultar libros disponibles")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            consultar_libros_disponibles()
        elif opcion == '2':
            titulo = input("Ingrese el título del libro que desea prestar: ")
            prestar_libro(titulo)
        elif opcion == '3':
            titulo = input("Ingrese el título del libro que desea devolver: ")
            devolver_libro(titulo)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    main()