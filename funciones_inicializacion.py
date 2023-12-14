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

def archivo_a_grafo(archivo: str, grafo:Grafo)-> Grafo:
    with open(archivo, 'r') as tsv:
        for line in tsv:
            line = line.rstrip("\n")
            datos = line.split('\t')
            articulo = datos[0]
            links = datos[1:]
            if not grafo.verticeExistente(articulo):
                grafo.agregar_vertice(articulo)
            for link in links:
                if not grafo.verticeExistente(link):
                    grafo.agregar_vertice(link)
                if not grafo.estan_unidos(articulo, link):
                    grafo.agregar_arista(articulo, link, 1)
    return grafo

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

