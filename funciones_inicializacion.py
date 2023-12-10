from Grafo import *
import sys

def leer_linea(linea):
    linea = linea.rstrip("\n")
    terminal = linea.split(" ", 1)
    comando = terminal[0]
    if len(terminal) > 1:
        parametros = terminal[1]
        return comando, parametros

    return comando, None


def listado_operaciones():
    print("camino")
    print("diametro")
    print("ciclo") 
    print("navegacion") 
    print("mas_importantes") 
    print("conectados") 
    print("lectura") 
    print("rango") 
    print("comunidad")
    print("clustering") 

