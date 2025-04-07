def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en la lista ordenada.
    Retorna el índice del elemento si se encuentra, de lo contrario -1.
    """
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1