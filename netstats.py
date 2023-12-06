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
        pagina = parametros[0]
        range = parametros[1]
        print(rango(grafo, pagina, range))

    elif comando == NAVEGACION_POR_PRIMER_LINK:
        pagina = parametros[0]
        print(" -> ".join(navegacion(grafo, pagina)))    

    #elif comando == CONECTIVIDAD:

    #elif comando == LECTURA_A_LAS_2_AM:

    #elif comando == COMUNIDADES:

    #elif comando == ARTICULOS_MAS_IMPORTANTES:

    #elif comando == CICLO_DE_N_ARTICULOS:


if __name__ == '__main__':
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
                if link not in grafo:
                    grafo.agregar_vertice(link)
                    
                grafo.agregar_arista(articulo, link)

    main(grafo)
