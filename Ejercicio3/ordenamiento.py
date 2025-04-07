def bubble_sort(lista):
    """
    Ordena una lista de números utilizando el algoritmo Bubble Sort.
    Retorna la lista ordenada.
    """
    n = len(lista) # n almacena la longitud de la lista
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]# intercambia los elementos
    return lista