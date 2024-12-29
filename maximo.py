def encontrar_maximo(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo
