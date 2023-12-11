#!/usr/bin/python3

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
CLUSTERING = "clustering"
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
            global diametro_g, diametro_recorrido
            if diametro_g == 0 and diametro_recorrido == []:
                diametro_recorrido = diametroRed(grafo)
                diametro_g = len(diametro_recorrido) - 1
            
            print(" -> ".join(diametro_recorrido))
            print("Costo: ", diametro_g)

        elif comando == TODOS_EN_RANGO:
            parametros = parametros.split(",")
            pagina = parametros[0]
            range = parametros[1]
            print(rango(grafo, pagina, int(range)))

        elif comando == NAVEGACION_POR_PRIMER_LINK:
            pagina = parametros
            print(" -> ".join(navegacion(grafo, pagina))) 

        elif comando == CONECTIVIDAD:
            pagina = parametros
            dicc_paginas = dicc_paginas if "dicc_paginas" in locals() else {} 
            conectados(grafo, pagina, dicc_paginas) 

        elif comando == LECTURA_A_LAS_2_AM:
            paginas = parametros
            orden = lectura_orden(grafo, paginas)
            if orden == None:
                print("No existe forma de leer las paginas en orden")
            else:
                print(",".join(orden))
            
        elif comando == COMUNIDADES:
            pagina = parametros
            comunidad(grafo, pagina)

        elif comando == CLUSTERING:
            pagina = parametros
            print(f"{clustering(grafo, pagina):.3f}")

        elif comando == CICLO_DE_N_ARTICULOS:
            params = parametros.split(",")
            vertice = params[0]
            n = int(params[1])
            ciclo = Nciclos(grafo, vertice, n)
            if ciclo == None:
                print("No se encontro recorrido")
            else:
                print(" -> ".join(ciclo))

        else: None


if __name__ == '__main__':
    stdin = sys.argv
    #if len(stdin) != 2:
        #raise Exception("Parametros invalidos")

    diametro_g = 0
    diametro_recorrido = []

    grafo = Grafo(dirigido = True)
    #archivo = sys.argv[1]
    with open("wiki-reducido-5000.tsv", 'r') as tsv:
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
