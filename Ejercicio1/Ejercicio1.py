""""
Ejercicio 1: Análisis de datos de ventas

Desarrollar un programa que procese un conjunto de registros de ventas para extraer información relevante. 
Deben aplicar funciones internas como map, 
filter y reduce para transformar y filtrar los datos, calculando totales y promedios.

•	[ ] El programa procesa correctamente un conjunto de registros de ventas.
•	[ ] Se utilizan las funciones map, filter y reduce para transformar y filtrar los datos.
•	[ ] Se calculan correctamente los totales de ventas.
•	[ ] Se calculan correctamente los promedios de ventas.
•	[ ] El código es legible y está bien documentado.

"""

from functools import reduce # Importamos reduce para realizar operaciones de reducción en listas

# Lista de registros de ventas (cada venta es una tupla: (vendedor, producto, cantidad, precio_unitario))
ventas = [
    ("Ana", "Laptop", 2, 800),
    ("Luis", "Mouse", 5, 20),
    ("Ana", "Monitor", 1, 300),
    ("Carlos", "Teclado", 3, 50),
    ("Luis", "Laptop", 1, 800),
    ("Carlos", "Mouse", 10, 20),
]

# 1. Usamos map para calcular el total por venta (cantidad * precio_unitario)
totales_por_venta = list(map(lambda venta: venta[2] * venta[3], ventas))
# Resultado: [1600, 100, 300, 150, 800, 200]

# 2. Usamos reduce para calcular el total general de ventas
total_general = reduce(lambda x, y: x + y, totales_por_venta)

# 3. Calculamos el promedio de ventas
promedio_ventas = total_general / len(totales_por_venta)

# 4. Usamos filter para obtener solo las ventas mayores a 500
ventas_mayores_500 = list(filter(lambda total: total > 500, totales_por_venta))

# Imprimimos los resultados
print("Totales por venta:", totales_por_venta)
print("Total general de ventas:", total_general)
print("Promedio de ventas:", promedio_ventas)
print("Ventas mayores a $500:", ventas_mayores_500)
