"""
Ejercicio #2: Módulo de ordenamiento

Diseñe un módulo independiente que contenga implementaciones de algoritmos de ordenamiento simples (bubble sort). 
Invoque los métodos del módulo para ordenar una lista de números.

•	[ ] Se ha creado un módulo independiente para los algoritmos de ordenamiento.
•	[ ] El módulo contiene una implementación funcional de bubble sort.
•	[ ] Se invoca correctamente el método del módulo para ordenar una lista de números.
•	[ ] El código es eficiente y está bien estructurado

"""

from ordenamiento import bubble_sort  # Importas la función desde tu módulo

if __name__ == "__main__":
    print("¿Cuántos números quieres en tu lista?")
    cantidad = int(input("Introduce la cantidad: "))

    numeros = []
    for i in range(cantidad):
        numero = int(input(f"Introduce el número {i+1}: "))
        numeros.append(numero)

    print("Lista original:", numeros)

    numeros_ordenados = bubble_sort(numeros)

    print("Lista ordenada:", numeros_ordenados)
