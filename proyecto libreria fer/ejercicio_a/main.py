from Libro import Libro

lista_libros = []
def cargarLibros():
    with open("libros.txt") as archivo:
        lineas = archivo.readlines()
        for line in lineas:
            titulo, autor, num_ejemplares, num_prestados = line.strip().split(",")
            lista_libros.append(Libro(titulo, autor ,int(num_ejemplares), int(num_prestados)))


def consultarLibro():
    for libro in lista_libros:
        if libro.esPosiblePrestar():
            print(f'Libro: {libro.titulo}  Autor: {libro.autor}')

def buscarObjetoLibro(nombre):
    for libro in lista_libros:
        if libro.titulo == nombre:
            return libro

def prestarLibro():
    nombre = input("Ingrese el nombre del libro: ")
    objetoLibro = buscarObjetoLibro(nombre)
    objetoLibro.prestarLibro()

def devolverLibro():
    libro_buscado = input("Ingrese el nombre del libro: ")
    objetoLibro = buscarObjetoLibro(libro_buscado)
    objetoLibro.devolverLibro()
    
def actualizar_archivo():
    with open("libros.txt","w") as archivo:
        for libro in lista_libros:
            linea = f"{libro.titulo},{libro.autor},{libro.num_ejemplares},{libro.num_prestados}\n" 
            archivo.write(linea)
        
            
def mostrar_menu():
    print("Selecciones la opcion que desee entre 1, 2 , 3 o 4")
    print("1. Consultar un libro")
    print("2. Solicitar un libro")
    print("3. Devolver un libro")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion
def main():
    cargarLibros()
    pregunta = "a"
    while pregunta != "N":
        opcion = mostrar_menu()
        if opcion == "1":
            consultarLibro()
            pregunta = input("Desea realizar otra acción: S/N")
            pregunta.lower()
        elif opcion == "2":
            prestarLibro()
            pregunta = input("Desea realizar otra acción: S/N")
            pregunta.lower()
            actualizar_archivo()
        elif opcion == "3":
            devolverLibro()
            pregunta = input("Desea volver realizar otra acción: S/N")
            pregunta.lower()
            actualizar_archivo()
        elif opcion == "4":
            pregunta = "N"
        else:
            print("Ingrese una de las OPCIONES VÁLIDAS ")

if __name__ == '__main__':
    main()


