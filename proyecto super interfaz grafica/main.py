
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from Producto import Producto

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Productos")
        self.ventana.geometry('300x200')  # Establece el tamaño de la ventana

        # Estilo de los botones
        style = ttk.Style()
        style.configure("TButton",
                        foreground="midnight blue",
                        background="light sky blue",
                        font=("Helvetica", 16),
                        padding=10)

        # Botones del menú
        self.boton_consultar = ttk.Button(self.ventana, text="Consultar Productos", command=self.consultar_productos)
        self.boton_consultar.pack(side=tk.TOP, fill=tk.X)

        self.boton_registrar = ttk.Button(self.ventana, text="Registrar Venta", command=self.registar_venta)
        self.boton_registrar.pack(side=tk.TOP, fill=tk.X)

        self.boton_reabastecer = ttk.Button(self.ventana, text="Reabastecer Producto", command=self.reabastecer_producto)
        self.boton_reabastecer.pack(side=tk.TOP, fill=tk.X)

        self.lista_productos = []
        self.cargar_productos()  # Carga los productos al iniciar la aplicación

        self.ventana.mainloop()

    def cargar_productos(self):
        with open("productos.txt") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            self.lista_productos.append(Producto(datos[0],float(datos[1]),int(datos[2]),int(datos[3])))
        messagebox.showinfo("Información", "Productos cargados con éxito")

    def consultar_productos(self):
        for producto in self.lista_productos:
            print(producto.nombre)

    def buscar_producto(self, nombre):
        for producto in self.lista_productos:
            if producto.nombre == nombre:
                return producto
        return None

    def registar_venta(self):
        nombre = simpledialog.askstring("Producto", "Ingrese el nombre del producto")
        cantidad = simpledialog.askinteger("Cantidad", "Ingrese la cantidad vendida")
        producto = self.buscar_producto(nombre)
        if producto and producto.cantidad >= cantidad:
            producto.cantidad -= cantidad
            messagebox.showinfo("Información", "Venta registrada con éxito")
        else:
            messagebox.showerror("Error", "Producto no disponible o cantidad insuficiente")

    def reabastecer_producto(self):
        nombre = simpledialog.askstring("Producto", "Ingrese el nombre del producto")
        cantidad = simpledialog.askinteger("Cantidad", "Ingrese la cantidad para reabastecer")
        producto = self.buscar_producto(nombre)
        if producto:
            producto.cantidad += cantidad
            messagebox.showinfo("Información", "Producto reabastecido con éxito")
        else:
            messagebox.showerror("Error", "Producto no encontrado")

if __name__ == "__main__":
    Aplicacion()
