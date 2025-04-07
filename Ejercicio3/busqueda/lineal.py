def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en la lista.
    Retorna el índice del elemento si se encuentra, de lo contrario -1.
    """
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1