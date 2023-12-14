#!/usr/bin/python3

from funciones_inicializacion import *
from operaciones import *
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
            operacion_camino(parametros, grafo)

        elif comando == DIAMETRO:
            operacion_diametro(grafo)

        elif comando == TODOS_EN_RANGO:
            operacion_rango(parametros, grafo)

        elif comando == NAVEGACION_POR_PRIMER_LINK:
            operacion_navegacion(parametros, grafo)

        elif comando == CONECTIVIDAD:
            operacion_conectividad(parametros, grafo)

        elif comando == LECTURA_A_LAS_2_AM:
            operacion_lectura(parametros, grafo)
            
        elif comando == COMUNIDADES:
            operacion_comunidades(parametros, grafo)

        elif comando == CLUSTERING:
            operacion_clustering(parametros, grafo)

        elif comando == CICLO_DE_N_ARTICULOS:
            operacion_ciclos(parametros, grafo)

        else: None


if __name__ == '__main__':
    stdin = sys.argv
    #if len(stdin) != 2:
        #raise Exception("Parametros invalidos")

    grafo = Grafo(dirigido = True)
    #archivo = sys.argv[1]
    with open("wiki-reducido-75000.tsv", 'r') as tsv:
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
