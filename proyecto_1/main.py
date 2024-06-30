m = []
with open("clientes.txt","r") as archivo:
    for line in archivo.readlines():
        m.append(line.split(","))
    for i in range(len(m)):
        if m[i][5] == "1":
            print(f"El usuario {m[i][0]} esta habilitado")
            for j in range(len(m)):
                passw = m[j][4]
                if len(passw) >= 6:
                    minuscula = 0
                    mayuscula = 0
                    numeros = 0
                    for i in range (len(passw)):
                        if passw[i].isdigit():
                            numeros = numeros + 1
                        elif passw[i].islower():
                            minuscula = minuscula + 1
                        elif passw[i].isupper():
                            mayuscula = mayuscula + 1
                    if minuscula >= 1 and mayuscula >= 1 and numeros >= 4:
                        print("Su contraseña es fuerte")
                    else:
                        print("Su contraseña no es fuerte")
                else:
                    print("La contraseña no es fuerte")
        else:
            print(F"El usuario {m[i][0]} no esta habilitado")
                    

