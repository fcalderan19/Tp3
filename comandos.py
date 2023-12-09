from Cola import *
from Grafo import *
from Pila import *
from funciones_inicializacion import *
from biblioteca import *

#--------- Camino mas corto ---------
def camino(grafo: Grafo, origen, destino): #O(V + E)
    
    distancia, padres = bfs(grafo, origen)
    if destino in padres:
        return reconstruirCamino(padres, origen, destino)
    return None

#--------- Diametro Red --------- 
def diametroRed(grafo: Grafo): #O(V * (V + E))

    distancia_max = 0
    dist = 0
    recorrido = []

    for v in grafo.obtener_vertices():
        distancias, padres = bfs(grafo, v)
        for distancia in padres:
            if distancias[distancia] != None:
                dist += distancias[distancia]

        if dist > distancia_max:
            distancia_max = dist
            recorrido = reconstruirCamino(padres)

    return recorrido, distancia_max

#--------- Todos en rango N --------- 
def rango(grafo, p, n): #O(V + E)
    cantidad = 0
    _, distancias = bfs(grafo, p)
    for v in distancias:
        if distancias[v] == n:
            cantidad +=1

    return cantidad

#--------- Navegacion por primer link --------- 
def navegacion(grafo, origen): #O(V + E)
    navegacion = []
    navegacion.append(origen)

    while len(grafo.adyacentes(origen)) > 0:
        link_actual = grafo.adyacentes(origen)[0]
        origen = link_actual
        navegacion.append(link_actual)
        if len(navegacion) == 21: #21 porque estamos appendeando el origen entonces serian 20 a partir desde el origen
            break

    return navegacion

#--------- Conectividad ---------
def conectados(grafo, pagina, dicc_paginas):
    sys.setrecursionlimit(75000)

    if pagina in dicc_paginas: #como tiene que ser constante en la segunda consulta, lo vamos guardando en un dicc 
        paginas_conectadas = dicc_paginas[pagina]
        print(f"Páginas conectadas a '{pagina}': {', '.join(paginas_conectadas)}.")
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
    print(f"Páginas conectadas a '{pagina}': {', '.join(componente_pagina)}.")

#--------- Lectura de 2 am ---------
def lectura_orden(grafo, paginas: str):
    #cambiando cosas
    paginas = set(paginas.split(","))

#--------- Comunidades ---------
def comunidad(grafo, pagina):
    etiquetas= label_propagation(grafo)
    comunidad_pagina = etiquetas.get(pagina)
    if comunidad_pagina is not None:
        print(f"La página {pagina} pertenece a la comunidad {comunidad_pagina}. ")    
    else:
        print(f"No se pudo determinar la comunidad de la pagina {pagina}")

#--------- Coeficiente de Clustering ---------
def clustering(grafo, pagina):
    if pagina is not None:
        clustering_pagina = calcular_clustering_pagina(grafo, pagina)
        print(f"El coeficiente de clustering de la pagina {pagina} es:{clustering_pagina:.3f}")
    else:
        clustering_promedio = calcular_clustering_promedio(grafo)
        print(f"El clustering promedio de la red es:{clustering_promedio:.3f}")
    """ Permite obtener el coeficiente de clustering de la página indicada. En caso de no indicar página,
    se deberá informar el clustering promedio de la red. En ambos casos, informar con hasta 3 dígitos decimales."""
    if pagina is not None:
        clustering_pagina = calcular_clustering_pagina(grafo, pagina)
        print(f"El coeficiente de clustering de la pagina {pagina} es:{clustering_pagina:.3f}")
    else:
        clustering_promedio= calcular_clustering_promedio(grafo)
        print(f"El clustering promedio de la red es:{clustering_promedio:.3f}")



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
        return 2.0 * cantidad_enlaces / (g_salida *(g_salida - 1))

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

