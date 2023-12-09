from funciones_inicializacion import *
from Grafo import *
from comandos import *
import sys

#Lista de operaciones
LISTAR_OPERACIONES = "listar_operaciones"
CAMINO_MAS_CORTO = "camino"
DIAMETRO = "diametro"
TODOS_EN_RANGO = "rango"
NAVEGACION_POR_PRIMER_LINK = "navegacion"
CONECTIVIDAD = "conectados"
LECTURA_A_LAS_2_AM = "lectura"
COMUNIDADES = "comunidad"
ARTICULOS_MAS_IMPORTANTES = "mas_importantes"
CICLO_DE_N_ARTICULOS = "ciclo"


def main(grafo):
    for linea in sys.stdin:
        comando, parametros = leer_linea(linea)

        if comando == LISTAR_OPERACIONES:
            listado_operaciones()

        elif comando == CAMINO_MAS_CORTO:
            parametros = parametros.split(",")
            origen = parametros[0]
            destino = parametros[1]

            recorrido = camino(grafo, origen, destino)
            if recorrido == None:
                print("No se encontro recorrido")
            else:
                print(" -> ".join(recorrido))
                print("Costo: ", len(recorrido) - 1)

        elif comando == DIAMETRO:
            recorrido, diam = diametroRed(grafo)
            print(" -> ".join(recorrido))
            print("Costo: ", diam)

        elif comando == TODOS_EN_RANGO:
            parametros = parametros.split(",")
            pagina = parametros[0]
            range = parametros[1]
            print(rango(grafo, pagina, range))

        elif comando == NAVEGACION_POR_PRIMER_LINK:
            pagina = parametros
            print(" -> ".join(navegacion(grafo, pagina)))    

        elif comando == CONECTIVIDAD:
            pagina = parametros[0]
            dicc_paginas = dicc_paginas if "dicc_paginas" in locals() else {} 
            conectados(grafo, pagina, dicc_paginas) 

        elif comando == LECTURA_A_LAS_2_AM:
            paginas = parametros #el usuario puede poner la cantidad de paginas que quiera como parametro
            lectura_orden(grafo, paginas)
        elif comando == COMUNIDADES:
            comunidad(grafo, pagina)

        elif comando == CLUSTERING:
            clustering(grafo, pagina)

        else: None

if __name__ == '__main__':
    stdin = sys.argv
    if len(stdin) != 2:
        raise Exception("Parametros invalidos")

    grafo = Grafo(dirigido = True)
    archivo = sys.argv[1]
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
                
    main(grafo)