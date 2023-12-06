from TDAS.Grafo import Grafo
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
    terminal = terminal.rstrip().split(" ")
    comando = terminal[0]
    parametros = terminal[1:]

    parametros = " ".join(parametros).split(",")
    for i in range(len(parametros)):
        parametros[i] = parametros[i].lstrip()

    return comando, parametros


def listado_operaciones():
    print("camino") 
    print("mas_importantes") 
    print("conectados") 
    print("ciclo") 
    print("lectura") 
    print("diametro")  
    print("rango") 
    print("comunidad")
    print("navegacion") 
    print("clustering") 

