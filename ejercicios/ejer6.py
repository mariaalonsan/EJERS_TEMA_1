def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

if __name__ == "__main__":
    pares, impares = separar([6,5,2,1,7])
    print(pares)
    print(impares)