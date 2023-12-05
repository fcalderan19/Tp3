from TDAS import Cola,Grafo,Pila

"""
Una biblioteca de funciones de grafos, que permitan hacer distintas operaciones sobre un grafo que modela Internet, 
sin importar cuál es la red específica.
la biblioteca de funciones debe funcionar para aplicar cualquiera de las funciones implementadas sobre cualquier 
grafo que tenga las características de las de este TP (particularmente, dirigido y no pesado)
"""


def _bfs(grafo: Grafo, origen, padres, visitados, distancias): #o(V+E)
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

def _dfs(grafo, v, visitados,  padres, distancias): #o(V+E)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.add(w)
            padres[w] = v
            distancias[w] = distancias[v] + grafo.peso_arista(v,w)
            _dfs(grafo, w, visitados,  padres, distancias)

"orden topologico basado en grados de entrada"
def orden_topologico(grafo): #o(V+E)
    g_ent = grados_entrada(grafo)
    colas =  cola.CrearColaEnlazada()
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

def grados_entrada(grafo):
    g_ent= {}
    for v in grafo.obtener_vertices():
        g_ent[v] = 0
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            g_ent[w] += 1
    return g_ent

"camino minimo- grafo no pesado bfs"
def bfs_caminoMinimo(grafo, origen): #o(V+E)
    visitado, padre, distancia = set(), {}, {}
    colas =  cola.CrearColaEnlazada()
    visitado.add(origen)
    padre[origen] = None
    distancia[origen] = 0
    cola.Encolar(origen)
    while not cola.EstaVacia():
        v = cola.Desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitado:
                visitado.add(w)
                distancia[w] = distancia[v] + 1
                padre[w] = v
                cola.Encolar(w)
    return padre, distancia 

def obtener_aristas(grafo):#o(V+E)
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
def cfc_tarjan(grafo): #O(V+E)
    cfc= []
    visitados = set()
    contador_global = [0]
    for v in grafo.obtener_vertices():
        if v not in visitados:
            _dfs_cfc(grafo, v, visitados, {},{}, Pila(), set(), cfc,contador_global)
    return cfc

def _dfs_cfc(grafo, v, visitados, orden, mas_bajo, pila, apilados, cfc, contador_global):
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












