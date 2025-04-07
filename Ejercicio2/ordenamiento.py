def bubble_sort(lista):
    """
    Implementación del algoritmo Bubble Sort.
    Ordena la lista en orden ascendente.
    """
    n = len(lista)
    for i in range(n):
        # Últimos i elementos ya están ordenados
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Programa principal
if __name__ == "__main__":
    # Preguntar al usuario cuántos números quiere en su lista
    print("¿Cuántos números quieres en tu lista?")
    cantidad = int(input("Introduce la cantidad: "))

    # Crear la lista de números solicitándolos uno por uno
    numeros = []
    for i in range(cantidad):
        numero = int(input(f"Introduce el número {i+1}: "))
        numeros.append(numero)

    print("Lista original:", numeros)

    # Ordenar la lista usando bubble_sort
    numeros_ordenados = bubble_sort(numeros)

    print("Lista ordenada:", numeros_ordenados)
