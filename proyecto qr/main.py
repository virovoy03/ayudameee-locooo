from Mascota import Mascota
import qrcode
from PIL import Image

mascotas = []

def cargar_desde_archivo():
    with open("mascota.txt", 'r') as f:
        for linea in f:
            datos = linea.strip().split(',')
            mascotas.append(Mascota(datos[0],datos[1],datos[2],datos[3]))

def registrarMascota():
    codigo = input("Ingrese el codigo: ")
    nombre = input("Ingrese el nombre de la mascota: ")
    propietario = input("Ingrese el nombre del propietario: ")
    telefono = input("Ingrese el telefono: ")
    mascotas.append(Mascota(codigo,nombre,propietario,telefono))

def consultar_mascotas():
    for mascota in mascotas:
        print(mascota)
def seleccionarMascota():
    codigo = input("Ingrese el codigo de la mascota a buscar: ")
    for mascota in mascotas:
        if(mascota.codigo==codigo):
            return mascota

def generarQr(mascota):
    data = mascota.getInformacionQr()
    path = "qr_code"+mascota.codigo+".png"

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)

    mostrarQr(path)

def mostrarQr(pathImagen):
    imagen = Image.open(pathImagen)
    imagen.show()
def main():
    #cargar_desde_archivo()

    while True:
        print("\n1. Consultar mascotas")
        print("2. Registrar mascota")
        print("3. Generar QR")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            consultar_mascotas()
        elif opcion == '2':
            registrarMascota()
        elif opcion == '3':
            generarQr(seleccionarMascota())
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == '__main__':
    main()

