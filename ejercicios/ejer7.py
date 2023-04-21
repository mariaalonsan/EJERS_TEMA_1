def agregar_una_vez(lista, el):
    if el not in lista:
        lista.append(el)
    else:
        raise ValueError(f'Error: Imposible añnadir elementos duplicados=>{el}')
    return lista


if __name__ == "__main__":
    print(agregar_una_vez([1,2,8,"g"], 6))