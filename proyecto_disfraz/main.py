from Cliente import Cliente
from Disfraz import Disfraz
from Pieza import Pieza

lista_clientes = []
lista_disfraces = []
lista_piezas = []

def cargar_clientes():
    with open("clientes.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            nombre,telefono,mail,dni,estado = linea.strip().split(",")
            lista_clientes.append(Cliente(nombre,telefono,mail,dni,int(estado)))
def cargar_disfraz():
    with open("disfraz.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            categoria,nombre,estado,id = linea.strip().split(",")
            lista_clientes.append(Disfraz(categoria,nombre,int(estado),id))
def cargar_piezas():
    with open("pieza.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            descripcion,talle,precio,estado,id = linea.strip().split(",")
            lista_clientes.append(Pieza(descripcion,talle,int(estado),int(precio),int(id)))


def main():
    cargar_clientes()
    cargar_disfraz()
    cargar_piezas()
if __name__ == "__main__":
    main()