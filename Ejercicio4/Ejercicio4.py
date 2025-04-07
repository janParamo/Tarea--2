"""
Ejercicio 4: Gestión de productos e inventario

Diseñe una clase Producto que incluya atributos como código, nombre, precio y cantidad. 
Debe implementar una clase Inventario que administre una colección de objetos Producto, 
incorporando métodos para agregar, buscar, actualizar y eliminar productos.

•	[ ] Se ha diseñado una clase Producto con los atributos requeridos.
•	[ ] Se ha implementado una clase Inventario para gestionar la colección de productos.
•	[ ] La clase Inventario incluye métodos para agregar, buscar, actualizar y eliminar productos.
•	[ ] El código sigue los principios de la programación orientada a objetos.

"""

import os # Importar el módulo os para limpiar la pantalla

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la pantalla de la consola

class Producto: # Definición de la clase Producto
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self): # Método para representar el objeto como una cadena
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}"


class Inventario: # Definición de la clase Inventario
    def __init__(self): # Inicialización de la clase Inventario
        self.productos = [] # Lista para almacenar los productos

    def agregar_producto(self):# Método para agregar un producto al inventario
        limpiar_pantalla()
        print(".    Agregar Producto")
        while True: # Bucle para validar el código del producto
            codigo = input("Ingrese el código del producto: ").strip()
            if not codigo:
                print("El código no puede estar vacío.")
                continue
            if self.buscar_producto_por_codigo(codigo):
                print("Ya existe un producto con ese código.")
                return

            break

        while True: # Bucle para validar el nombre del producto
            nombre = input("Ingrese el nombre del producto: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
            else:
                break

        while True: # Bucle para validar el precio del producto
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    raise ValueError
                break
            except ValueError:
                print("Precio inválido. Ingrese un número positivo.")

        while True: # Bucle para validar la cantidad del producto
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                if cantidad < 0:
                    raise ValueError
                break
            except ValueError:
                print("Cantidad inválida. Ingrese un número entero positivo.")

        nuevo = Producto(codigo, nombre, precio, cantidad) # Crear un nuevo objeto Producto
        self.productos.append(nuevo)
        print("Producto agregado correctamente.")

    def buscar_producto(self): # Método para buscar un producto en el inventario
        limpiar_pantalla()
        if not self.productos:
            print("No hay productos registrados.")
            return

        print(" Buscar Producto ") # Mostrar los productos registrados
        opcion = input("Desea buscar Producto por \n (1) Código \n (2) Nombre? ").strip()

        if opcion == "1": # Buscar por código
            codigo = input("Ingrese el código del producto: ").strip()
            producto = self.buscar_producto_por_codigo(codigo)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")
        elif opcion == "2": # Buscar por nombre
            nombre = input("Ingrese el nombre del producto: ").strip().lower()
            encontrados = [p for p in self.productos if p.nombre.lower() == nombre]
            if encontrados:
                for p in encontrados:
                    print(p)
            else:
                print("Producto no encontrado.")
        else:
            print("Opción inválida.")

    def buscar_producto_por_codigo(self, codigo): # Método para buscar un producto por su código
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self): # Método para actualizar un producto en el inventario
        limpiar_pantalla()
        if not self.productos:
            print("No hay productos registrados.")
            return

        print(" Actualizar Producto ")
        codigo = input("Ingrese el código del producto a actualizar: ").strip()
        producto = self.buscar_producto_por_codigo(codigo)

        if producto: # Si se encuentra el producto, se procede a actualizarlo
            print("Producto actual:", producto)

            while True: # Bucle para validar el nuevo código del producto
                nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip()
                if nuevo_nombre != "":
                    producto.nombre = nuevo_nombre
                    break

            while True: # Bucle para validar el nuevo precio del producto
                nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
                if not nuevo_precio:
                    break
                try:
                    nuevo_precio = float(nuevo_precio)
                    if nuevo_precio < 0:
                        raise ValueError("El precio no puede ser negativo")
                    producto.precio = nuevo_precio
                    break
                except ValueError:
                    print("Precio inválido.")

            while True: # Bucle para validar la nueva cantidad del producto
                nueva_cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ").strip()
                if not nueva_cantidad:
                    break
                try:
                    nueva_cantidad = int(nueva_cantidad)
                    if nueva_cantidad < 0:
                        raise ValueError("La cantidad no puede ser negativa")
                    producto.cantidad = nueva_cantidad
                    break
                except ValueError:
                    print("Cantidad inválida.")

            print("Producto actualizado correctamente.")
        else:
            print("No se encontró ningún producto con ese código.")

    def eliminar_producto(self): # Método para eliminar un producto del inventario
        limpiar_pantalla()
        if not self.productos:
            print("No hay productos registrados.")
            return

        print(" Eliminar Producto ")
        codigo = input("Ingrese el código del producto a eliminar: ").strip()
        producto = self.buscar_producto_por_codigo(codigo)

        if producto:
            self.productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")


def menu(): # Función para mostrar el menú principal
    inventario = Inventario()

    while True: # Bucle para mostrar el menú y manejar las opciones
        print("\n Menú de Inventario ")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()
        limpiar_pantalla()

        if opcion == "1":
            inventario.agregar_producto()
        elif opcion == "2":
            inventario.buscar_producto()
        elif opcion == "3":
            inventario.actualizar_producto()
        elif opcion == "4":
            inventario.eliminar_producto()
        elif opcion == "5":
            print("fin")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu() # Llamar a la función menu para iniciar el programa