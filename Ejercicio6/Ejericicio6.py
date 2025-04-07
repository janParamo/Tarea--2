"""Ejercicio #6 Facturación y reportes de ventas
Crear una clase Factura que simule el proceso de facturación de una venta. Proveer métodos para calcular el total de la venta, generar reportes simples y validar la integridad de la información.

Ejercicio #6: Facturación y reportes de ventas
•	[ ] Se ha creado una clase Factura para simular el proceso de facturación.
•	[ ] La clase Factura incluye métodos para calcular el total de la venta.
•	[ ] Se generan reportes simples de ventas.
•	[ ] Se valida la integridad de la información de la factura.
•	[ ] El código es robusto y maneja posibles errores."""""

# Clase que representa una factura
class Factura:
    def __init__(self):
        self.items = []  # Lista de productos en la factura
        self.iva = 0.16  # Porcentaje de IVA (16%)
        self.descuento = 0.10  # Porcentaje de descuento (10%)

    # Método para agregar un producto a la factura
    def agregar_item(self, descripcion, cantidad, precio_unitario):
        if cantidad <= 0 or precio_unitario < 0:
            print("Error: Cantidad o precio inválido.")
            return

        # Se guarda cada producto como un diccionario
        self.items.append({
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio_unitario': precio_unitario
        })

    # Método que calcula el total de la factura
    def calcular_total(self):
        # Subtotal: suma de (cantidad × precio) de todos los productos
        subtotal = sum(item['cantidad'] * item['precio_unitario'] for item in self.items)
        
        # Se calcula el descuento
        monto_descuento = subtotal * self.descuento
        subtotal_con_descuento = subtotal - monto_descuento

        # Se calcula el IVA sobre el subtotal con descuento
        monto_iva = subtotal_con_descuento * self.iva

        # Total final: subtotal con descuento + IVA
        total = subtotal_con_descuento + monto_iva

        # Devuelve los montos para usarlos en el reporte
        return {
            'subtotal': subtotal,
            'descuento': monto_descuento,
            'iva': monto_iva,
            'total': total
        }

    # Método para imprimir un reporte de la factura
    def generar_reporte(self):
        print("\n--- FACTURA ---")
        
        # Se imprimen todos los productos comprados
        for item in self.items:
            print(f"{item['cantidad']} x {item['descripcion']} @ {item['precio_unitario']:.2f} = {item['cantidad'] * item['precio_unitario']:.2f}")
        
        # Se obtienen los totales
        totales = self.calcular_total()

        # Se imprime el desglose de la factura
        print(f"\nSubtotal: ${totales['subtotal']:.2f}")
        print(f"Descuento (10%): -${totales['descuento']:.2f}")
        print(f"IVA (16%): +${totales['iva']:.2f}")
        print(f"TOTAL A PAGAR: ${totales['total']:.2f}")
        print("-----------------\n")


# Función principal para ejecutar el programa
def main():
    factura = Factura()  # Se crea una instancia de la clase Factura
    print("Ingrese los datos de la factura (deje la descripción vacía para terminar):\n")

    # Bucle para ingresar productos uno por uno
    while True:
        descripcion = input("Descripción del producto: ")
        if descripcion == "":
            break  # Si el usuario deja en blanco, se termina el ingreso

        try:
            # Solicita cantidad y precio
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio unitario: "))
            factura.agregar_item(descripcion, cantidad, precio)  # Agrega el producto
        except ValueError:
            # Si el usuario ingresa un dato no numérico
            print("Error: Ingrese valores numéricos válidos.\n")

    # Si hay productos, se genera el reporte
    if factura.items:
        factura.generar_reporte()
    else:
        print("No se ingresaron productos. No se generó factura.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
