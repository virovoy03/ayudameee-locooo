import Vehiculo

ListaVehiculos = []
ListaPropietarios = []
ListaModelos = []
ListaMarcas = []


def BuscarObjeto(lista, codigo):
    for objeto in lista:
        if objeto.codigo == codigo:
            return objeto


def CargarPropietarios():
    with open("propietario.txt") as archivo:
        linea = archivo.readlines()
    for line in linea:
        datos = line.strip().split(",")
        ListaPropietarios.append(Vehiculo.Propietario(datos[0], datos[1], datos[2]))


def CargarModelos():
    with open("modelo.txt") as archivo:
        linea = archivo.readlines()
    for line in linea:
        datos = line.strip().split(",")
        ListaModelos.append(Vehiculo.Modelo(datos[0], datos[1]))


def CargarMarca():
    with open("marca.txt") as archivo:
        linea = archivo.readlines()
    for line in linea:
        datos = line.strip().split(",")
        ListaModelos.append(Vehiculo.Marca(datos[0], datos[1]))


def CargarVehiculos():
    with open("vehiculos.txt") as archivo:
        linea = archivo.readlines()
    for line in linea:
        datos = line.strip().split(",")
        objetoMarca = BuscarMarcas(int(datos[4]))
        if objetoMarca:
            ListaVehiculos.append(
                Vehiculo.Vehiculo(
                    int(datos[0]),
                    datos[1],
                    datos[2],
                    datos[3],
                    objetoMarca,
                    objetoModelo,
                    objetoPropietario,
                )
            )
        objetoModelo = BuscarObjeto(ListaModelos, int(datos[5]))
        objetoPropietario = BuscarObjeto(ListaPropietarios, int(datos[6]))
        ListaVehiculos.append(
            Vehiculo.Vehiculo(
                int(datos[0]),
                datos[1],
                datos[2],
                datos[3],
                objetoMarca,
                objetoModelo,
                objetoPropietario,
            )
        )


def MostarPropietarios(lista):
    for objeto in lista:
        print(objeto)


def MostarModelos(lista):
    for objeto in lista:
        print(objeto)


def MostarMarcas(lista):
    for objeto in lista:
        print(objeto)


def MostarVehiculos(lista):
    for objeto in lista:
        print(objeto)


def BuscarMarcas(codigo):
    for marca in ListaMarcas:
        if marca.codigo == codigo:
            return marca
        else:
            print("La marca no existe.")


def main():
    CargarPropietarios()
    CargarModelos()
    CargarMarca()
    CargarVehiculos()
    MostarVehiculos(ListaVehiculos)
    MostarPropietarios(ListaPropietarios)
    MostarModelos(ListaModelos)
    MostarMarcas(ListaMarcas)


if __name__ == "__main__":
    main()
