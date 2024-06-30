def eliminar_cliente():    
    dni = input("Ingrese DNI que desea eliminar: ")
    agenda = open("agenda_backup.txt", "r")
    lineas = agenda.readlines()
    agenda.close()
    agenda = open("agenda_backup.txt","w")
    for linea in lineas:
        if dni not in linea:
            agenda.write(linea)
            print("el cliente no se encontro en la base de datos")
        else:
            print("el cliente a sido eliminado correctamente")
    agenda.close() 
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
def main():
    agenda = open("agendaa.txt","r")
    lista = agenda.read()
    archivo = open("agenda_backup.txt","+a")
    archivo.writelines(lista)
    archivo.writelines("\n")
#if __name__ == "__main__":
main()
agregar()
print(consultar_telefono("dni"))
eliminar_cliente() 
restaurar()