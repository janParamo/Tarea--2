"""
Ejercicio 3: Paquete de algoritmos de búsqueda

Desarrolle un programa para organizar diferentes algoritmos de búsqueda en un paquete estructurado. 
Los estudiantes deberán crear al menos dos módulos que contengan implementaciones de búsqueda lineal y búsqueda binaria, 
configurando adecuadamente el archivo init.py. Utilice estas funciones para localizar elementos específicos en una colección de datos.

•	[] Se ha creado un módulo independiente para los algoritmos de ordenamiento.
•	[] El módulo contiene una implementación funcional de bubble sort.
•	[] Se invoca correctamente el método del módulo para ordenar una lista de números.
•	[] El código es eficiente y está bien estructurado
"""

# Importar las funciones necesarias de los módulos
from busqueda.lineal import busqueda_lineal
from busqueda.binaria import busqueda_binaria
from ordenamiento import bubble_sort

# Lista de ejemplo
datos = [34, 7, 23, 32, 5, 62]

# Ordenar la lista
print("Lista original:", datos)
datos_ordenados = bubble_sort(datos)
print("Lista ordenada:", datos_ordenados)

# Búsqueda lineal
elemento = 23
indice_lineal = busqueda_lineal(datos_ordenados, elemento)
print(f"Búsqueda lineal: El elemento {elemento} está en el índice {indice_lineal}")

# Búsqueda binaria
indice_binaria = busqueda_binaria(datos_ordenados, elemento)
print(f"Búsqueda binaria: El elemento {elemento} está en el índice {indice_binaria}")