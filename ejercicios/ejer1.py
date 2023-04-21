from ast import main 

class Alumno:
    def __init__(self, cadena):
        self.cadena = cadena

    @staticmethod
    def formatear_cadena(cadena):
        cadena_correcta = cadena[::-1]
        frase = cadena_correcta.split(",")
        nota = frase[0]
        nombre = frase[1]
        return f"{nombre} ha sacado un {nota}"
    
# cadena = "zeréP nauJ,01"
nombre1=Alumno("zeréP nauJ,01")

if __name__ == "__main__":
    print(Alumno.formatear_cadena(nombre1.cadena))