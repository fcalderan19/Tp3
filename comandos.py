from Cola import *
from Grafo import *
from Pila import *
from funciones_inicializacion import *
from biblioteca import *
import sys

#--------- Camino mas corto ---------
def camino(grafo: Grafo, origen, destino): #O(V + E)
    
    distancia, padres = bfs(grafo, origen)
    if destino in padres:
        return reconstruirCamino(padres, origen, destino)
    return None

#--------- Diametro Red --------- 
def diametroRed(grafo: Grafo): #O(V * (V + E))
    distMax = 0
    diametro = (None, None)
    bfs_diametro = None

    for v in grafo.obtener_vertices():
        distancias, padres = bfs(grafo, v)
        for w in distancias:
            if distancias[w] != None and distancias[w] > distMax:
                distMax = distancias[w]
                diametro = (v, w)
                bfs_diametro = padres

    return reconstruirCamino(bfs_diametro, diametro[0], diametro[1])

#--------- Todos en rango N --------- 
def rango(grafo, p, n): #O(V + E)
    cantidad = 0
    distancias, _ = bfs(grafo, p)
    for v in distancias:
        if distancias[v] == n:
            cantidad +=1

    return cantidad

#--------- Navegacion por primer link --------- 
def navegacion(grafo, origen): #O(V + E)
    navegacion = []
    navegacion.append(origen)
    cant_ady = len(grafo.adyacentes(origen))

    while len(grafo.adyacentes(origen)) > 0:
        link_actual = grafo.adyacentes(origen)[0]
        origen = link_actual
        cant_ady = len(grafo.adyacentes(origen))
        navegacion.append(link_actual)
        if len(navegacion) == 21: #21 porque estamos appendeando el origen entonces serian 20 a partir desde el origen
            break

    return navegacion

#--------- Conectividad ---------
def conectados(grafo, pagina, dicc_paginas):
    sys.setrecursionlimit(75000)

    if pagina in dicc_paginas: #como tiene que ser constante en la segunda consulta, lo vamos guardando en un dicc 
        paginas_conectadas = dicc_paginas[pagina]
        print(f"{', '.join(paginas_conectadas)}.")
        return
    
    cfc = cfc_tarjan(grafo)
    componente_pagina = None
    for componente in cfc: #encontrar el componente al que pertenece la pagina
        if pagina in componente:
            componente_pagina = componente
            break
        
    if componente_pagina is None: #si la pag no esta en ninguna comp, tirar un error
        print(f"No se encontraron páginas conectadas a {pagina}.")
        return 

    dicc_paginas[pagina] = componente_pagina #almaceno los resultados de cfc
    print(f"{', '.join(componente_pagina)}.")

#--------- Lectura de 2 am ---------
def lectura_orden(grafo, paginas: str):
    paginas_list = paginas.split(",")
    paginas_set = set(paginas_list)
    salidas = grados_salida(grafo, paginas_set)
    entradas = padres_entrada(grafo, paginas_set)
    cola = Cola()

    for vertice in paginas_set:
        if salidas[vertice] == 0:
            cola.Encolar(vertice)

    orden = []
    while not cola.EstaVacia():
        vertice = cola.Desencolar()
        orden.append(vertice)
        for v in entradas[vertice]:
            if v in paginas_set:
                salidas[v] -= 1
                if salidas[v] == 0:
                    cola.Encolar(v)

    if len(orden) != len(paginas_list): # Hay ciclo o no hay suficientes
        return None
    
    return orden

def padres_entrada(grafo: Grafo, paginas: set):
    g_ent = {}
    for v in grafo.obtener_vertices():
        g_ent[v] = set()

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if v in paginas and w in paginas:
                g_ent[w].add(v)

    return g_ent

#--------- Comunidades ---------
def comunidad(grafo, pagina):
    etiquetas= label_propagation(grafo)
    comunidad_pagina = etiquetas.get(pagina)
    if comunidad_pagina is not None:
        print(f"comunidad {comunidad_pagina}. ")    
    else:
        print(f"No se pudo determinar la comunidad de la pagina {pagina}")

#--------- Coeficiente de Clustering ---------
def clustering(grafo, pagina):
    """ Permite obtener el coeficiente de clustering de la página indicada. En caso de no indicar página,
    se deberá informar el clustering promedio de la red. En ambos casos, informar con hasta 3 dígitos decimales."""
    if pagina is not None:
        if not esta_pagina(grafo, pagina):
            print(f"{pagina} no esta en el grafo")
            return
        clustering_pagina = calcular_clustering_pagina(grafo, pagina)
        print(f"{clustering_pagina:.3f}")
    else:
        clustering_promedio= calcular_clustering_promedio(grafo)
        print(f"{clustering_promedio:.3f}")


#--------- Ciclo de N artículos ---------
def Nciclos(grafo: Grafo, vertice, n):
    visitados = set()
    camino = []
    return buscarCicloN(grafo, vertice, vertice, camino, visitados, n)


#https://algoritmos-rw.github.io/algo2/material/apuntes/label_propagation/
def label_propagation(grafo: Grafo):
    etiquetas = {v : v for v in grafo.obtener_vertices()}
    for _ in range (CANT_ITERACIONES):
        vertices = list(grafo.obtener_vertices())
        random.shuffle(vertices)

        for v in vertices:
            vecinos = grafo.adyacentes(v)
            if vecinos:
                etiquetas_vecino= [etiquetas[w] for w in vecinos] #obtengo las etiquetas de los vecinos
                etiquetas[v]= max(set(etiquetas_vecino), key= etiquetas_vecino.count) #asigno la etiqueta mas comun al nodo actual
    return etiquetas

def contar_aristas_vecinos(grafo: Grafo, vertice):
    contador = 0
    for w in grafo.adyacentes(vertice):
        if grafo.estan_unidos(vertice, w):
            contador += 1
        if grafo.estan_unidos(w, vertice):
            contador += 1

    return contador 

def esta_pagina(grafo, pagina):
    for v in grafo.obtener_vertices():
        if v == pagina:
            return True
    return False

def calcular_clustering_pagina(grafo: Grafo, pagina):
    cantidad_enlaces = contar_aristas_vecinos(grafo, pagina)
    g_salida = grados_salida(grafo, None)
    grado = g_salida[pagina]
    if grado < 2:
        return 0.0
    else:
        return cantidad_enlaces / (grado *(grado - 1))

def calcular_clustering_promedio(grafo: Grafo):
    """calculo el clustering promedio de la red"""
    clustering_total = 0.0
    vertices = grafo.obtener_vertices()
    for nodo in vertices:
        clustering_total += calcular_clustering_pagina(grafo, nodo)
    
    if not vertices:
        return 0.0
    else: 
        return clustering_total / len(vertices)