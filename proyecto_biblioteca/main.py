
from Libro import Libro

lista = []

def consultar_libros():
    for libro in lista:
        if libro.is_posible_prestar():
            print(libro)
