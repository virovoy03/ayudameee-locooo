
from PIL import Image
from Empleado import Empleado
from Mueble import Mueble

lista_de_muebles = []
lista_empleados = []

def mostrar_imagen(url):
    try:
        img = Image.open(url)
        img.show()
    except IOError: # hace que no tire error si no se puede abrir el programa
        print("no se pudo abrir la imagen del muebles")

def cargar_empleados():
    with open("empleados.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            nombre,dni,telefono,contraseña,estado = linea.strip().split(",")
            lista_empleados.append(Empleado(nombre,dni,telefono,contraseña,int(estado)))
            
def iniciar_sesion():
    usuario = input("ingrese su nombre: ")
    for empleado in lista_empleados:
        if empleado.nombre == usuario:
            contraseña = input("ingrese contraseña: \n")
            if empleado.contraseña == contraseña:
                print("")
                print(f"Bienvenido {empleado.nombre}")
                return True
            else:
                print("contraseña incorrecta")
                return False
    print("!! usuario no encontrado !!")
            
def cargar_muebles():   
    with open("muebles.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            nombre,estado,codigo,url = linea.strip().split(",")
            lista_de_muebles.append(Mueble(nombre,int(estado),int(codigo),url))
            
def mostrar_muebles_habilitados():
    for mueble in lista_de_muebles:
        if mueble.is_habilitado():
            print(f"el mueble {mueble.nombre} con Codigo: {mueble.codigo} esta habilitado")
            
def mostrar_muebles_deshabilitados():
    for mueble in lista_de_muebles:
        if not mueble.is_habilitado():
            print(f"el mueble {mueble.nombre} Codigo: {mueble.codigo} esta deshabilitado")

def desabilitar_mueble():
    codigo = -1
    while codigo != 0:
        try:
            codigo = int(input("Ingrese el codigo del mueble a deshabilitar o 0-salir "))
            for mueble in lista_de_muebles:
                if mueble.codigo == codigo:
                    if mueble.is_habilitado():
                        mueble.estado = 0
                        guardar_cambio_en_muebles()
                        print(f"Mueble {mueble.nombre} con codigo {mueble.codigo} deshabilitado.")
                        return
                    print("el mueble ya se encuentra deshabilitado")
                    return
                if codigo == 0:
                    return
            print("Mueble no encontrado.")
        except ValueError:
            print("ingrese numero valido por favor")  
        
def habilitar_mueble():
    codigo = -1
    while codigo != 0:
        try:
            codigo = int(input("Ingrese el codigo del mueble para habilitar o 0-salir:\n"))
            for mueble in lista_de_muebles:
                if mueble.codigo == codigo:
                    if not mueble.is_habilitado():
                        mueble.estado = 1
                        guardar_cambio_en_muebles()
                        print(f"Mueble {mueble.nombre} con codigo {mueble.codigo} habilitado.")
                        return
                    print("el mueble ya se encuentra habilitado")
                    return
                if codigo == 0:
                    return
            print("Mueble no encontrado.")
        except ValueError:
            print("ingrese un numero valido por favor")
            
def guardar_cambio_en_muebles():
    with open("muebles.txt", "w") as archivo:
        for mueble in lista_de_muebles:
            archivo.write(f"{mueble.nombre},{mueble.estado},{mueble.codigo},{mueble.url}\n")
        
def consultar_mueble():
    codigo = -1
    while codigo != 0:
        try:
            mostrar_muebles_habilitados()
            codigo = int(input("ingrese codigo del mueble a consultar o 0-salir\n"))
            mueble_encontrado = False
            for mueble in lista_de_muebles:
                if mueble.codigo == codigo:
                    mueble_encontrado = True
                    if mueble.is_habilitado():
                        url_imagen = mueble.url
                        mostrar_imagen(url_imagen)        
                    else:
                        print("mueble no disponible para consultar")
            if not mueble_encontrado:
                print(" Pareque que pusiste un codigo de mueble inexistente")       
        except ValueError:
            print("ingrese un numero valido por favor")                    

def menu():
    cargar_empleados()
    cargar_muebles()

    op = -1
    while op != 0:
        try:
            op = int(input("ingrese quien desea usar el programa\n 1-empleado\n 2-cliente\n 0-salir "))
            while op >0:
                if op ==1:
                    if iniciar_sesion(): #hace que el programa continua solo si iniciar_sesion() devuelve True                        
                        op = int(input("ingrese que quiere hacer\n 1-habilitar mueble\n 2-desabilitar mueble\n 0-salir "))                        
                        while op >0:
                            if op ==1:
                                mostrar_muebles_deshabilitados()
                                habilitar_mueble()
                            if op ==2:
                                mostrar_muebles_habilitados()
                                desabilitar_mueble()
                            if op > 2:
                                print("ingrese opcion valida")     
                            op = int(input("ingrese que quiere hacer\n 1-habilitar muebles\n 2-desabilitar muebles\n 0-salir "))   
                if op == 2:
                    consultar_mueble()    
                if op > 2:
                    print("ingrese una opcion valida")
                op = int(input("ingrese quien desea usar el programa\n 1-empleado\n 2-cliente\n 0-Salir "))
        except ValueError:
            print("ingrese un numero valido por favor")

def main():
    menu()
    
if __name__ == '__main__':
    main()
