from Pelicula import Pelicula
peliculas = []


def cargar_peliculas_desde_archivo():
    with open("peliculas.txt", 'r') as f:
        for linea in f:
            datos = linea.strip().split(',')
            titulo = datos[0]
            precio_entrada = float(datos[1])
            pelicula_semana = datos[2]
            estado = datos[3]
            pelicula = Pelicula(titulo, precio_entrada, pelicula_semana, estado)
            peliculas.append(pelicula)


def mostrar_peliculas_habilitadas():
    print("Peliculas habilitadas:")
    i=1
    for pelicula in peliculas:
        if(pelicula.isHabilitada()):
            print(str(i)+" - " + pelicula.titulo)
            i+=1


def procesar_venta_entrada(cliente, pelicula_seleccionada):
    pelicula = peliculas[pelicula_seleccionada - 1]
    precio_final = pelicula.precio_entrada_final(cliente)
    print(f"El importe de la entrada para la película '{pelicula.titulo}' es: ${precio_final}")

    with open("registro_entradas.txt", "a") as f:
        f.write(f"Pelicula: {pelicula.titulo}, Cliente: {cliente}, Precio Final: ${precio_final}\n")


def main():
    cargar_peliculas_desde_archivo()

    print("¡Bienvenidos!")
    mostrar_peliculas_habilitadas()

    cliente = input("Ingrese el tipo de cliente (1-2x1, 2-jubilado, 3-discapacitado o 0-ninguno): ")
    opcion = int(input("Seleccione la película deseada: "))

    procesar_venta_entrada(cliente, opcion)

if __name__ == '__main__':
    main()


