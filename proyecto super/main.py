
from Producto import Producto

lista_productos = []

def cargar_productos():
    with open("productos.txt") as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        datos = linea.strip().split(",")
        lista_productos.append(Producto(datos[0],float(datos[1]),int(datos[2]),int(datos[3])))
        
def consultar_productos():
    for producto in lista_productos:
        if (producto.cantidad_disponible > 0):
            print(f"producto: {producto.nombre}, stock: {producto.cantidad_disponible}")
            
def buscar_producto():
    producto_seleccionado = input("ingrese producto que desea: ")
    for producto in lista_productos:
        return producto

def registar_venta():
    producto = buscar_producto()
    if (producto):
        if (producto.cantidad_disponible > producto.cantidad_vendida):
            if (producto.nombre == producto):
                producto.cantidad_vendida +=1
                producto.cantidad_disponible-=1 
                return print("La venta se realizo con exito")
        else:
            print("el producto no tiene cantidad disponble para vender")
    else:
        return print("no es posible vender este producto")

def reabastecer_producto():
    producto = buscar_producto()
    if(producto):
        cantiadad_a_sumar = int(input("ingrese cantidad de productos que desea reabastecer"))
        producto.cantidad_disponible += cantiadad_a_sumar

def main():
    cargar_productos()
    print(lista_productos)
    op = int(input(" 1-consultar disponible\n 2-registrar venta\n 3-reabastecer producto\n 0-salir\n"))
    while (op >0):
        if (op ==1):
            consultar_productos()
        if (op ==2):
            registar_venta()
        if (op == 3): 
            reabastecer_producto()
        if (op > 3):
            print("ingrese una opcion valida")
        op = int(input("1-consultar disponible\n 2-registrar venta\n 3-reabastecer producto\n 0-salir\n "))
    
    
    
if __name__ == "__main__":
    main()