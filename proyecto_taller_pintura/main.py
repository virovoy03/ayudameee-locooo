from Vehiculo import Vehiculo
from Marca import Marca
from Modelo import Modelo
from Propietario import Propietario

lista_vehiculo = []
lista_marca = []
lista_modelo = []
lista_propietario = []

def cargar_vehiculos():
    with open("vehiculos.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
        marca = buscar_objeto(lista_vehiculo,int(datos[3]))
        modelo= buscar_objeto(lista_modelo,int(datos[4]))
        propietario = buscar_objeto(lista_propietario,int(datos[5]))     
        lista_vehiculo.append(Vehiculo(datos[0],datos[1],datos[2],marca,modelo,propietario))

def buscar_objeto(lista,codigo):
    for objeto in lista:
        if objeto.codigo == codigo:
            return objeto

def main():
    pass

if __name__ == "__main__":
    main()
