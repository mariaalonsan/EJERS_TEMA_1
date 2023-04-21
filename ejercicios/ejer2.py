from ast import main
import sys


numero_magico = 12345679

def excepcion(numero):  
    try:
        numero=int(numero) 
        if 1<=int(numero)<=9:
            return int(numero)
        else:
            raise ValueError("El número no está entre 1 y 9")
    except:
        raise ValueError("El caracter no aceptado")
    
def num(numero):
    numero=excepcion(numero)
    return f'Resultado: {numero*9*numero_magico}'