
with  open("clientes.txt","w") as archivo:
    op= input("¿desea registrar un cliente? (s/n): ")
    while op.lower() == "s":
        apellido = input("ingrese el apellido del cliente ")
        nombre = input("ingrese el nombre del cliente ")
        dni = input("ingrese el dni del cliente ")
        mail = input("ingrese el mail del cliente ")
            
        archivo.write(f"{apellido},{nombre},{dni},{mail}\n")
        op= input("¿desea registrar otro cliente? (s/n): ")
    print("registro de cliente finalizado")