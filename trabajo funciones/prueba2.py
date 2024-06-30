
def eliminar_cliente():
    dni = input("Ingrese DNI que desea eliminar: ")
    agenda = open("agendaa.txt", "r")
    lineas = agenda.readlines()
    agenda.close()
    agenda = open("agendaa.txt", "w")
    for linea in lineas:
        if dni not in linea:
            agenda.write(linea)
            print("el cliente no se encontro en la base de datos")
        else:
            print("el cliente a sido eliminado correctamente")
    agenda.close() 
def consultar_telefono(dni):
    dni = input("ingrese dni que desea consultar: ")
    agenda = open("agendaa.txt", "r")
    lineas = agenda.readlines()
    agenda.close()
    for linea in lineas:
        if dni in linea:
            print("el numero de telefono del cliente ingresado es:")
            return linea.split(",")[1]
    return "Cliente no encontrado."
def agregar():
    lista = open("agendaa.txt","r")
    clientes = lista.readlines()
    nombre=str(input("ingrese el nombre que desea guardar: "))
    numero=str(input("ingrese numero de telefono: "))
    dni=str(input("ingrese DNI: "))
    for linea in clientes:
        if dni in linea:
            print("el cliente ya esta registrado")
            return
    lista_completa = (nombre,",",numero,",",dni,"\n")
    lista = open("agendaa.txt","a+")
    lista.writelines(lista_completa)   
    lista.close()
    print("cliente registrado exitosamente")
if __name__ == "__main__":
    agregar()
    #print(consultar_telefono("dni")) anda no tocar
    #eliminar_cliente() anda no tocar