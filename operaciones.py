from funciones_inicializacion import *
from Grafo import *
from comandos import *
import sys

global diametro_g, diametro_recorrido
diametro_g = 0
diametro_recorrido = []

def operacion_camino(parametros: str, grafo: Grafo):
    parametros = parametros.split(",")
    origen = parametros[0]
    destino = parametros[1]

    recorrido = camino(grafo, origen, destino)
    if recorrido == None:
        print("No se encontro recorrido")
    else:
        print(" -> ".join(recorrido))
        print("Costo: ", len(recorrido) - 1)

def operacion_diametro(grafo: Grafo):
    global diametro_g, diametro_recorrido
    if diametro_g == 0 and diametro_recorrido == []:
        diametro_recorrido = diametroRed(grafo)
        diametro_g = len(diametro_recorrido) - 1
    
    print(" -> ".join(diametro_recorrido))
    print("Costo: ", diametro_g)


def operacion_rango(parametros: str, grafo: Grafo):
    parametros = parametros.split(",")
    pagina = parametros[0]
    range = parametros[1]
    print(rango(grafo, pagina, int(range)))

def operacion_conectividad(parametros: str, grafo:Grafo):
    pagina = parametros
    dicc_paginas = dicc_paginas if "dicc_paginas" in locals() else {} 
    conectados(grafo, pagina, dicc_paginas)

def operacion_navegacion(parametros: str, grafo: Grafo):
    pagina = parametros
    print(" -> ".join(navegacion(grafo, pagina)))

def operacion_lectura(parametros: str, grafo: Grafo):
    paginas = parametros
    orden = lectura_orden(grafo, paginas)
    if orden == None:
        print("No existe forma de leer las paginas en orden")
    else:
        print(",".join(orden))

def operacion_comunidades(parametros: str, grafo: Grafo):
    pagina = parametros
    comunidad(grafo, pagina)

def operacion_clustering(parametros: str, grafo: Grafo):
    pagina = parametros
    clustering(grafo, pagina)

def operacion_ciclos(parametros: str, grafo: Grafo):
    params = parametros.split(",")
    vertice = params[0]
    n = int(params[1])
    ciclo = Nciclos(grafo, vertice, n)
    if ciclo == None:
        print("No se encontro recorrido")
    else:
        print(" -> ".join(ciclo))
