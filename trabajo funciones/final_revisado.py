def menu():
    l
def eliminar_cliente():    
    dni = input("Ingrese DNI que desea eliminar: ")
    agenda = open("agenda_backup.txt", "r")
    lineas = agenda.readlines()
    agenda.close()
    agenda = open("agenda_backup.txt","w")
    cliente_eliminado = False
    for linea in lineas:
        if dni not in linea:
            agenda.write(linea)
        else:
            cliente_eliminado = True
    agenda.close()
    if cliente_eliminado:
        print("El cliente ha sido eliminado correctamente")
    else:
        print("El cliente no se encontró en la base de datos")
def consultar_telefono(dni):
    dni = input("ingrese dni que desea consultar: ")
    agenda = open("agenda_backup.txt", "r")
    lineas = agenda.readlines()
    agenda.close()
    for linea in lineas:
        if dni in linea:
            print("el numero de telefono del cliente ingresado es:")
            return linea.split(",")[1]
    return "Cliente no encontrado."
def agregar():
    lista = open("agenda_backup.txt","r")
    clientes = lista.read()
    nombre=str(input("ingrese el nombre que desea guardar: "))
    numero=str(input("ingrese numero de telefono: "))
    dni=str(input("ingrese DNI: "))
    for linea in clientes:
        if dni in linea:
            print("el cliente ya esta registrado")
            return
    lista_completa = (nombre,",",numero,",",dni,"\n")
    lista = open("agenda_backup.txt","a+")
    lista.writelines(lista_completa)   
    lista.close()
    print("cliente registrado exitosamente")
def restaurar():
   import os
   os.remove("agenda_backup.txt") 
def cargar_agenda():
    agenda = open("agenda.txt","r")
    lista = agenda.read()
    archivo = open("agenda_backup.txt","+a")
    archivo.writelines(lista)
    archivo.writelines("\n")
#if __name__ == "__main__":
#ejecutar siempre primero el main
cargar_agenda()
#agregar()
#print(consultar_telefono("dni"))
#eliminar_cliente() 
#restaurar()