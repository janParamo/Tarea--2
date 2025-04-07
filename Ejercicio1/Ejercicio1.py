"""
Ejercicio 6: Facturación y reportes de ventas

Crear una clase Factura que simule el proceso de facturación de una venta. 
Proveer métodos para calcular el total de la venta, generar reportes simples y validar la integridad de la información.

•	[ ] Se ha creado una clase Factura para simular el proceso de facturación.
•	[ ] La clase Factura incluye métodos para calcular el total de la venta.
•	[ ] Se generan reportes simples de ventas.
•	[ ] Se valida la integridad de la información de la factura.
•	[ ] El código es robusto y maneja posibles errores.
"""

from functools import reduce

# Lista vacía para almacenar los registros de ventas
ventas = []

# Pedimos al usuario que ingrese la cantidad de ventas a registrar
num_ventas = int(input("¿Cuántas ventas desea registrar? "))

# Pedimos al usuario que ingrese los datos de cada venta
for i in range(num_ventas):
    print(f"\nRegistro de venta #{i + 1}")
    vendedor = input("Nombre del vendedor: ")
    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad vendida: "))
    precio_unitario = float(input("Precio unitario del producto: "))
    
    # Agregamos la venta a la lista como una tupla
    ventas.append((vendedor, producto, cantidad, precio_unitario))

# 1. Usamos map para calcular el total por venta (cantidad * precio_unitario)
totales_por_venta = list(map(lambda venta: venta[2] * venta[3], ventas))

# 2. Usamos reduce para calcular el total general de ventas
total_general = reduce(lambda x, y: x + y, totales_por_venta)

# 3. Calculamos el promedio de ventas
promedio_ventas = total_general / len(totales_por_venta)

# 4. Usamos filter para obtener solo las ventas mayores a 500
ventas_mayores_500 = list(filter(lambda total: total > 500, totales_por_venta))

# Imprimimos los resultados
print("\n----- RESULTADOS -----")
print("Totales por venta:", totales_por_venta)
print("Total general de ventas:", total_general)
print("Promedio de ventas:", promedio_ventas)
print("Ventas mayores a $500:", ventas_mayores_500)
