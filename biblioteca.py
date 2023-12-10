from Cola import *
from Grafo import *
from Pila import *
import random
CANT_ITERACIONES = 10

"""
Una biblioteca de funciones de grafos, que permitan hacer distintas operaciones sobre un grafo que modela Internet, 
sin importar cuál es la red específica.
la biblioteca de funciones debe funcionar para aplicar cualquiera de las funciones implementadas sobre cualquier 
grafo que tenga las características de las de este TP (particularmente, dirigido y no pesado)
"""

def reconstruirCamino(padres: dict, X, Y):
    camino = []
    while Y!=X:
        camino.append(Y)
        Y = padres[Y]
    camino.append(X)
    camino.reverse()
    return camino

def bfs(grafo: Grafo, origen): #O(V + E)
    padres, visitados, distancias = {}, set(), {}
    cola = Cola()
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

def dfs(grafo, v, visitados,  padres, distancias): #O(V + E)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            padres[w] = v
            distancias[w] = distancias[v] + grafo.peso_arista(v,w)
            dfs(grafo, w, visitados,  padres, distancias)


"orden topologico basado en grados de entrada"
def orden_topologico(grafo: Grafo): #o(V+E)
    g_ent = grados_entrada(grafo)
    cola = Cola()
    for v in grafo.obtener_vertices():
        if g_ent[v] == 0:
            cola.Encolar(v)
            print(cola.VerPrimero())
    resultado = []
    while not cola.EstaVacia():
        v = cola.Desencolar()
        resultado.append(v)
        for w in grafo.adyacentes(v):
            g_ent[w] -= 1
            if g_ent[w] == 0:
                cola.Encolar(w)
    return resultado

def grados_entrada(grafo:Grafo):
    g_ent = {}
    for v in grafo.obtener_vertices():
        g_ent[v] = 0
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            g_ent[w] += 1
    return g_ent

def grados_salida(grafo:Grafo, paginas: set):
    g_salida = {}
    for v in grafo.obtener_vertices():
        g_salida[v] = 0

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if w in paginas:
                g_salida[v] += 1
    return g_salida

def obtener_aristas(grafo: Grafo):#o(V+E)
    aristas = []
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            aristas.append((v,w,grafo.peso_arista(v,w)))
    return aristas

def buscarCicloN(grafo: Grafo, origen, vertice_actual, camino_actual: list, visitados: set, N):
    if len(camino_actual) == N:
        if vertice_actual == origen:
            camino_actual.append(vertice_actual)
            return camino_actual.copy()
        return None

    if vertice_actual == origen and len(camino_actual) != 0:
        return None

    camino_actual.append(vertice_actual)
    visitados.add(vertice_actual)

    for vecino in grafo.adyacentes(vertice_actual):
        if vecino not in visitados or vecino == origen:
            ciclo_encontrado = buscarCicloN(grafo, origen, vecino, camino_actual, visitados, N)
            if ciclo_encontrado:
                return ciclo_encontrado

    camino_actual.pop()
    visitados.remove(vertice_actual)
    return None
    
"componentes fuertemente conexas TARJAN "
def cfc_tarjan(grafo: Grafo): #O(V+E)
    cfc = []
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
    pila.Apilar(v)
    apilados.add(v)

    for w in grafo.adyacentes(v):
        if w not in visitados:
            _dfs_cfc(grafo, w, visitados, orden, mas_bajo, pila, apilados, cfc, contador_global)
        if w in apilados:
            mas_bajo[v]= min(mas_bajo[v], mas_bajo[w])
    
    if mas_bajo[v] == orden[v]:
        nueva_cfc = []
        while True:
            w = pila.Desapilar()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        cfc.append(nueva_cfc)
