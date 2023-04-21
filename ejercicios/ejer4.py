cola= [
        {'tarea 3': 'ir a clase', 'prioridad':'3'},
        {'tarea 1': 'levantarme', 'prioridad':'1'},
        {'tarea 2': 'comer', 'prioridad':'2'}
    ]

def ordenar(c):
    return c['prioridad']


def estructura_cola(cola):
    cola.sort(key=ordenar)
    lista=[]
    for i in cola:
        print(i)
        lista.append(i)
    return lista

if __name__=="main_":
    estructura_cola(cola)