
from TDAS.Cola import Cola
from TDAS.Pila import Pila
from TDAS.Grafo import Grafo
import random

CANT_ITERACIONES = 10
"""
Una biblioteca de funciones de grafos, que permitan hacer distintas operaciones sobre un grafo que modela Internet, 
sin importar cuál es la red específica.
la biblioteca de funciones debe funcionar para aplicar cualquiera de las funciones implementadas sobre cualquier 
grafo que tenga las características de las de este TP (particularmente, dirigido y no pesado)
"""

def bfs(grafo: Grafo, origen, padres, visitados, distancias): #o(V+E)
    cola =  Cola()
    cola.Encolar(origen)
    padres[origen] = None
    visitados.add(origen)
    distancias[origen] = 0
    while not cola.EstaVacia():
        v = cola.Desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                distancias[w] = distancias[v] + grafo.peso_arista(v,w)
                cola.Encolar(w)

    return distancias, padres

def dfs(grafo: Grafo, v, visitados,  padre, distancia): #o(V+E)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            padre[w] = v
            distancia[w] = distancia[v] + grafo.peso_arista(v,w)
            dfs(grafo, w, visitados,  padre, distancia)

"orden topologico basado en grados de entrada"
def orden_topologico(grafo: Grafo): #o(V+E)
    g_ent = grados_entrada(grafo)
    cola =  Cola()
    for v in grafo.obtener_vertices():
        if g_ent[v] == 0:
            cola.Encolar(v)
    resultado =[]
    while not cola.EstaVacia():
        v = cola.Desencolar()
        resultado.append(v)
        for w in grafo.adyacentes(v):
            g_ent[w] -= 1
            if g_ent[w] == 0:
                cola.Encolar(w)
    return resultado

def grados_entrada(grafo:Grafo):
    g_ent= {}
    for v in grafo.obtener_vertices():
        g_ent[v] = 0
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            g_ent[w] += 1
    return g_ent

def grados_salida(grafo:Grafo):
    g_salida=[]
    for v in grafo.obtener_vertices():
        g_salida =len(grafo.adyacentes(v))
    return g_salida

"camino minimo- grafo no pesado bfs"
def bfs_caminoMinimo(grafo: Grafo, origen): #o(V+E)
    visitado, padre, distancia = set(), {}, {}
    cola =  Cola()
    visitado.add(origen)
    padre[origen] = None
    distancia[origen] = 0
    cola.Encolar(origen)
    while not cola.EstaVacia():
        v = cola.Desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitado:
                visitado.add(w)
                distancia[w] = distancia[v] + grafo.peso_arista(v,w)
                padre[w] = v
                cola.Encolar(w)
    return padre, distancia 

def obtener_aristas(grafo: Grafo):#o(V+E)
    aristas = []
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            aristas.append((v,w,grafo.peso_arista(v,w)))
    return aristas

def reconstruir_camino(padre, destino):
    recorrido = []
    while destino is not None:
        recorrido.append(destino)
        destino = padre[destino]
    return recorrido[::-1]
    
"componentes fuertemente conexas TARJAN "
def cfc_tarjan(grafo: Grafo): #O(V+E)
    cfc= []
    visitados = set()
    contador_global = [0]
    for v in grafo.obtener_vertices():
        if v not in visitados:
            _dfs_cfc(grafo, v, visitados, {},{}, Pila(), set(), cfc,contador_global)
    return cfc

def _dfs_cfc(grafo: Grafo, v, visitados, orden, mas_bajo, pila: Pila, apilados, cfc, contador_global):
    orden[v] = mas_bajo[v] = contador_global[0]
    contador_global[0] += 1
    visitados.add(v)
    pila.apilar(v)
    apilados.add(v)

    for w in grafo.adyacentes(v):
        if w not in visitados:
            _dfs_cfc(grafo, w, visitados, orden, mas_bajo, pila, apilados, cfc, contador_global)
        if w in apilados:
            mas_bajo[v]= min(mas_bajo[v], mas_bajo[w])
    
    if mas_bajo[v] == orden[v]:
        nueva_cfc = []
        while True:
            w = pila.desapilar()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        cfc.append(nueva_cfc)


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
                

"""
Coeficiente de Clustering:
por cada par de adyacentes al vértice en cuestión, si existe la arista yendo de uno al otro (si además está la recíproca, lo contamos
otra vez). A esa cantidad de aristas lo dividimos por K(K-1) siendo K  el grado de salida del vértice i. En caso de tener menos
de 2 adyacentes, se define que el coeficiente de clustering de dicho vértice es 0. Considerar que el coeficiente de clustering 
es siempre un número entre 0 y 1.

Permite obtener el coeficiente de clustering de la página indicada. En caso de no indicar página, se deberá informar el clustering promedio 
de la red. En ambos casos, informar con hasta 3 dígitos decimales.
"""

def contar_aristas_vecinos(grafo: Grafo, vecinos):
    """ toma una lista de nodos vecinos y cuenta cuántas aristas existen entre esos nodos."""
    contador = 0

    for i in range (len(vecinos)):
        for j in range(i+1, len(vecinos)):
            if grafo.estan_unidos(vecinos[i], vecinos[j]):
                contador += 1
    return contador 


def calcular_clustering_pagina(grafo: Grafo, pagina):
    vecinos = grafo.adyacentes(pagina)
    cantidad_enlaces = contar_aristas_vecinos(grafo, vecinos)
    g_salida = grados_salida(grafo)[pagina]
    if g_salida < 2:
        return 0.0
    else:
        return 2.0 * cantidad_enlaces / (g_salida *(g_salida - 1)) #cantidad de aristas / K(K-1)

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

