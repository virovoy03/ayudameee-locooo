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
        marca = buscar_objeto(lista_marca,(datos[3]))
        modelo = buscar_objeto(lista_modelo,(datos[4]))
        propietario = buscar_objeto(lista_propietario,(datos[5]))     
        lista_vehiculo.append(Vehiculo(datos[0],datos[1],datos[2],marca,modelo,propietario))

def cargar_marcas():
    with open("marcas.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
        lista_marca.append(Marca(datos[0],datos[1]))
        
def cargar_modelos():
    with open("modelos.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
        lista_modelo.append(Modelo(datos[0],datos[1]))

def cargar_propietarios():
    with open("propietarios.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
        lista_propietario.append(Propietario(datos[0],datos[1],datos[2]))

def buscar_objeto(lista,codigo):
    for objeto in lista:
        if objeto.codigo == codigo:
            return objeto

def contar_marcas():
    marca_usuario = input("ingrese la marca que desee para saber cuantos vehiculos ingresaron de cada marca\n")
    conteo = 0
    for vehiculo in lista_vehiculo:
        if vehiculo.marca.nombre == marca_usuario:
            conteo += 1
    print(f"hay: {conteo} vehiculos pertenecientes a la marca: {marca_usuario}")

def obtener_tipos_de_vehiculos_disponibles():
    tipos_de_vehiculos = []
    for vehiculo in lista_vehiculo:
        if vehiculo.tipo not in tipos_de_vehiculos:
            tipos_de_vehiculos.append(vehiculo.tipo)
    print(tipos_de_vehiculos)

def contar_por_tipo_de_vehiculo():
    tipo_usuario = input("ingrese el tipo de vehiculo que desee para saber cuantos vehiculos ingresaron de cada tipo: ")
    conteo = 0
    for vehiculo in lista_vehiculo:
        if vehiculo.tipo == tipo_usuario:
            conteo += 1
    print(f"hay: {conteo} pertenecientes al tipo {tipo_usuario}")

def menu():
    cargar_marcas()
    cargar_modelos()
    cargar_propietarios()
    cargar_vehiculos()
    print(lista_vehiculo)
    op = -1
    while op != 0:
        try:
            op = int(input("ingrese que desea hacer\n 1-consultar por marca la cantidad de vehiculos ingresados\n 2-consultar por ""tipo de vehiculo la cantidad de vehiculos"" ingresados\n 0-salir "))
            if op == 0:
                break
            if op ==1:
                print(lista_marca)         
                contar_marcas()   
            if op == 2:
                obtener_tipos_de_vehiculos_disponibles()
                contar_por_tipo_de_vehiculo()    
            if op > 2:
                print("ingrese una opcion valida")
            #op = int(input("ingrese que desea hacer\n 1-consultar por marca la cantidad de vehiculos ingresados\n 2-consultar por ""tipo de vehiculo la cantidad de vehiculos"" ingresados\n 0-salir "))     
        except ValueError:
            print("ingrese un numero valido por favor")
def main():
    menu()

if __name__ == "__main__":
    main()
