from funciones_inicializacion import *
from TDAS.Grafo import Grafo
from NetStats import *
import sys

g = cargar_grafo()

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
        origen = parametros[0]
        destino = parametros[1]

        recorrido = camino_minimo(grafo, origen, destino)
        if recorrido == None:
            print("No se encontro recorrido")
        else:
            print() #no se como printear las ->
            print("Costo: ", len(recorrido) - 1)

    elif comando == DIAMETRO:
        recorrido, diam = diametroRed(grafo)
        print() #no se como printear las ->
        print("Costo: ", diam)

    elif comando == TODOS_EN_RANGO:

    elif comando == NAVEGACION_POR_PRIMER_LINK:

    elif comando == CONECTIVIDAD:

    elif comando == LECTURA_A_LAS_2_AM:

    elif comando == COMUNIDADES:

    elif comando == ARTICULOS_MAS_IMPORTANTES:

    elif comando == CICLO_DE_N_ARTICULOS:

    else: None







    







main(g)