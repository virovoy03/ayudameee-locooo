from PIL import Image
from Empleado import Empleado
from Mueble import Mueble

lista_de_muebles = []
lista_empleados = []


def mostrar_imagen(url):
    try:
        img = Image.open(url)
        img.show()
    except IOError:  # hace que no tire error si no se puede abrir el programa
        print("No se pudo abrir la imagen del mueble.")


def cargar_empleados():
    with open("empleados.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            nombre, dni, telefono, contraseña, estado = linea.strip().split(",")
            lista_empleados.append(
                Empleado(nombre, dni, telefono, contraseña, int(estado))
            )


def iniciar_sesion():
    usuario = input("Ingrese su nombre: ")
    for empleado in lista_empleados:
        if empleado.nombre.lower() == usuario.lower():
            contraseña = input("Ingrese contraseña:")
            if empleado.contraseña == contraseña:
                print("")
                print(f"Bienvenido {empleado.nombre}")
                return True
            else:
                print("Contraseña incorrecta.")
                return False
    print("¡¡ Usuario no encontrado !!")


def cargar_muebles():
    with open("muebles.txt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            nombre, estado, codigo, url = linea.strip().split(",")
            lista_de_muebles.append(Mueble(nombre, int(estado), int(codigo), url))


def mostrar_muebles_habilitados():
    for mueble in lista_de_muebles:
        if mueble.is_habilitado():
            print(
                f"El mueble {mueble.nombre} con Codigo: {mueble.codigo} esta habilitado."
            )


def mostrar_muebles_deshabilitados():
    for mueble in lista_de_muebles:
        if not mueble.is_habilitado():
            print(
                f"El mueble {mueble.nombre} Codigo: {mueble.codigo} esta deshabilitado."
            )


def desabilitar_mueble():
    codigo = -1
    while codigo != 0:
        try:
            codigo = int(
                input("Ingrese el codigo del mueble a deshabilitar o 0-salir: ")
            )
            for mueble in lista_de_muebles:
                if mueble.codigo == codigo:
                    if mueble.is_habilitado():
                        mueble.estado = 0
                        guardar_cambio_en_muebles()
                        print(
                            f"Mueble {mueble.nombre} con codigo {mueble.codigo} deshabilitado."
                        )
                        return
                    print("El mueble ya se encuentra deshabilitado.")
                    return
                if codigo == 0:
                    return
            print("Mueble no encontrado.")
        except ValueError:
            print("Ingrese numero valido por favor.")


def habilitar_mueble():
    codigo = -1
    while codigo != 0:
        try:
            codigo = int(
                input("Ingrese el codigo del mueble para habilitar o 0-salir: ")
            )
            for mueble in lista_de_muebles:
                if mueble.codigo == codigo:
                    if not mueble.is_habilitado():
                        mueble.estado = 1
                        guardar_cambio_en_muebles()
                        print(
                            f"Mueble {mueble.nombre} con codigo {mueble.codigo} habilitado."
                        )
                        return
                    print("El mueble ya se encuentra habilitado.")
                    return
                if codigo == 0:
                    return
            print("Mueble no encontrado.")
        except ValueError:
            print("Ingrese un numero valido por favor.")


def guardar_cambio_en_muebles():
    with open("muebles.txt", "w") as archivo:
        for mueble in lista_de_muebles:
            archivo.write(
                f"{mueble.nombre},{mueble.estado},{mueble.codigo},{mueble.url}\n"
            )


def consultar_mueble():
    codigo = -1
    while codigo != 0:
        try:
            mostrar_muebles_habilitados()
            codigo = int(input("Ingrese codigo del mueble a consultar o 0-salir: "))
            if codigo == 0:
                return
            mueble_encontrado = False
            for mueble in lista_de_muebles:
                if mueble.codigo == codigo:
                    mueble_encontrado = True
                    if mueble.is_habilitado():
                        url_imagen = mueble.url
                        mostrar_imagen(url_imagen)
                    else:
                        print("Mueble no disponible para consultar.")
            if not mueble_encontrado:
                print("Parece que pusiste un codigo de mueble inexistente.")

        except ValueError:
            print("Ingrese un numero valido por favor.")


def menu():
    cargar_empleados()
    cargar_muebles()

    op = -1
    while op != 0:
        try:
            op = int(
                input(
                    "Ingrese quien desea usar el programa\n1-empleado\n2-cliente\n0-salir\n: "
                )
            )
            while op > 0:
                if op == 1:
                    if (
                        iniciar_sesion()
                    ):  # hace que el programa continua solo si iniciar_sesion() devuelve True
                        op = int(
                            input(
                                "Ingrese que quiere hacer\n1-habilitar mueble\n2-desabilitar mueble\n0-salir\n: "
                            )
                        )
                        while op > 0:
                            if op == 1:
                                mostrar_muebles_deshabilitados()
                                habilitar_mueble()
                            if op == 2:
                                mostrar_muebles_habilitados()
                                desabilitar_mueble()
                            if op > 2:
                                print("Ingrese opcion valida.")
                            op = int(
                                input(
                                    "Ingrese que quiere hacer\n1-habilitar muebles\n2-desabilitar muebles\n0-salir\n: "
                                )
                            )
                if op == 2:
                    consultar_mueble()
                if op > 2:
                    print("Ingrese una opcion valida.")
                op = int(
                    input(
                        "Ingrese quien desea usar el programa\n1-empleado\n2-cliente\n0-Salir\n: "
                    )
                )
        except ValueError:
            print("Ingrese un numero valido por favor.")


def main():
    print("Bienvenido! ")
    menu()


if __name__ == "__main__":
    main()
