from Grafo import *
import sys

def cargar_grafo():
    stdin = sys.argv
    if len(stdin) != 2:
        raise Exception("Parametros invalidos")

    grafo = Grafo()
    archivo = sys.argv[1]
    with open(archivo, 'r') as tsv:
        for line in tsv:
            datos = line.strip().split('\t')
            articulo = datos[0]
            links = datos[1:]
            grafo.agregar_vertice(articulo)
            for link in links:
                grafo.agregar_arista(articulo, link)
    return grafo

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

