
from Pelicula import Pelicula

lista = []

def cargar_peliculas():
    with open ("pelicula.txt") as f:
        lista = f.readlines()
    for r in lista:
        nombre,precio_general,habilitada,semanal = r.strip().split(",")
        lista.append(Pelicula(nombre,float(precio_general),habilitada,semanal))
def visualizar_habilitada():
    for p in lista:
        if p.is_habilitada():
            print(p)

def seleccionar_pelicula():
    pelicula = input("ingrese la pelicula")


def main():
    cargar_peliculas()
if __name__ == "__main__":
    main()