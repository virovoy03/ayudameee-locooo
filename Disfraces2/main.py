import Disfraz
import Persona
from Alquiler import Alquiler

listaPiezas=[]
listaDisfraces=[]
listaCategorias=[]
listaClientes=[]
listaEncargados=[]

def cargarClientes():
    with open("clientes.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
        listaClientes.append(Persona.Cliente(datos[0],datos[1],datos[2],datos[3],datos[4]))

def cargarEncargado():
    with open("encargados.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
        listaEncargados.append(Persona.Encargado(datos[0],datos[1],datos[2],datos[3],datos[4]))

def cargarPiezas():
    with open("piezas.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
#        objeto=buscarObjeto(listaDisfraces,int(datos[4]))
#       if(objeto):
        listaPiezas.append(Disfraz.Pieza(datos[0],datos[1],datos[2],datos[3]))

def cargarDisfraces():
    with open("disfraces.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(";")
        objeto = buscarObjeto(listaCategorias, int(datos[3]))
        disfrazObjeto=Disfraz.Disfraz(int(datos[0]),datos[1],datos[2],objeto)

        #recorro la lista de piezas que tiene asociada
        codigoPiezasAsociadas=datos[4]

        # Elimino los corchetes del principio y del final
        codigoPiezasAsociadas = codigoPiezasAsociadas.strip('[]')

        # Divide la cadena en elementos individuales separados por comas
        elementos = codigoPiezasAsociadas.split(',')

        for codigoPieza in elementos:
            piezaObjeto=buscarObjeto(listaPiezas,codigoPieza)
            if(piezaObjeto):
                disfrazObjeto.piezas.append(piezaObjeto)

        listaDisfraces.append(disfrazObjeto)

def cargarCategoria():
    with open("categorias.txt") as archivo:
        renglones = archivo.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
        listaCategorias.append(Disfraz.Categoria(int(datos[0]), datos[1], datos[2]))


def consultarDatos(lista):
    for objeto in lista:
        if(objeto.estado=="0"):
            print(objeto)

def consultarDatosPersona(lista):
    for objeto in lista:
        print(objeto)

def consultarDatosContactoPersona(lista):
    for objeto in lista:
        print(objeto)
def buscarObjeto(lista,codigo):
    for objeto in lista:
        if (objeto.codigo == codigo):
            return objeto
    else:
        print("El codigo no existe")

def registrarDisfraz():
    codigo=input("Ingrese el codigo")
    nombre = input("Ingrese el nombre")
    estado = input("Ingrese el estado")
    consultarDatos(listaCategorias)
    codigoCategoria=input("Ingrese el codigo de la categoria: ")
    categoria=buscarObjeto(listaCategorias,codigoCategoria)
    disfrazNuevo=Disfraz.Disfraz(codigo,nombre,estado,categoria)

    consultarDatos(listaPiezas)
    while True:
        codigoPieza = input("Ingrese el codigo de la pieza / 0-salir: ")
        if codigoPieza=="0":
            break
        pieza = buscarObjeto(listaPiezas, codigoPieza)
        if(pieza):
            disfrazNuevo.piezas.append(pieza)

    listaDisfraces.append(disfrazNuevo)

def registrarAlquiler():
    codigo=input("Ingrese el codigo")
    consultarDatosPersona(listaClientes)
    codigoCliente = input("Ingrese el codigo del cliente: ")
    cliente = buscarObjeto(listaClientes, codigoCliente)
    consultarDatosPersona(listaEncargados)
    codigoEncargado = input("Ingrese el codigo del encargado: ")
    encargado = buscarObjeto(listaEncargados, codigoEncargado)
    consultarDatos(listaDisfraces)
    codigoDisfraz=input("Ingrese el codigo del disfraz: ")
    disfraz=buscarObjeto(listaDisfraces,int(codigoDisfraz))
    alquiler=Alquiler(codigo,disfraz,cliente,encargado,disfraz.getPrecio())
    print(alquiler)

def main():
    cargarClientes()
    cargarEncargado()
    cargarCategoria()
    #invierto la carga
    cargarPiezas()
    cargarDisfraces()

    opcion=int(input("1-Consultar Disfraces \n"
                     "2-Consultar Piezas \n"
                     "3-Consultar Categoria \n"
                     "4-Registrar Disfraz \n"
                     "5-Consultar Clientes \n"
                     "6-Consultar Encargado \n"
                     "7-Registrar Alquiler \n"
                     "0-Salir"))
    while(opcion>0):
        if (opcion==1):
            consultarDatos(listaDisfraces)
        if (opcion==2):
            consultarDatos(listaPiezas)
        if (opcion==3):
            consultarDatos(listaCategorias)
        if (opcion==4):
            registrarDisfraz()
        if (opcion==5):
            consultarDatosPersona(listaClientes)
        if (opcion==6):
            consultarDatosPersona(listaEncargados)
        if (opcion==7):
            registrarAlquiler()
        if (opcion>8):
            print("Opcion incorrecta")
        opcion = int(input("1-Consultar Disfraces \n"
                           "2-Consultar Piezas \n"
                           "3-Consultar Categoria \n"
                           "4-Registrar Disfraz \n"
                           "5-Consultar Clientes \n"
                           "6-Consultar Encargado \n"
                           "7-Registrar Alquiler \n"
                           "0-Salir"))

if __name__ == '__main__':
    main()
