from ast import main
import sys


def num(numeros):
    try:
        numeros=int(numeros)
        return str(numeros)
        sys.exit()
    except:
        raise ValueError("El caracter no aceptado")

def descomponer(numeros):
    numeros=num(numeros)
    numero=numeros[::-1]
    lista=[]
    ceros_izquierda=0
    while True:
        for i in str(numero):
            ceros_izquierda+=1
            k=((i.ljust(int(ceros_izquierda),'0')).zfill(len(numero)))
            print(k)
            lista.append(k)
        if ceros_izquierda >= len(numero):
            break
    return lista