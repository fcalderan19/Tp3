from TDAS import Grafo
from funciones_inicializacion import *
import biblioteca

#--------- Camino mas corto ---------
def camino(grafo, origen, destino): #O(V + E)
    padre, distancia = biblioteca.bfs(grafo, origen, destino)
    if destino in distancia:
        return biblioteca.reconstruir_camino(padre, origen, destino)
    return None

#--------- Diametro Red --------- 
def diametroRed(grafo: Grafo): #O(V * (V + E))

    distancia_max = 0
    dist = 0
    recorrido = []

    for v in grafo.obtener_vertices():
        padres, distancias = biblioteca.bfs(grafo, v)
        for distancia in distancias:
            dist += distancias[distancia]
        if dist > distancia_max:
            distancia_max = dist
            recorrido += biblioteca.reconstruir_camino(padres)

    return distancia_max

#--------- Todos en rango N --------- 
def rango(grafo, p, n):
    cantidad = 0
    _, distancias = biblioteca.bfs(grafo, p, None)
    for v in distancias:
        if distancias[v] == n:
            cantidad +=1

    return cantidad

#--------- Navegacion por primer link --------- 
def navegacion(grafo, origen):
    navegacion = []
    navegacion.append(origen)

    while len(grafo.adyacentes(origen)) > 0:
        link_actual = grafo.adyacentes(origen)[0]
        navegacion.append(link_actual)
        if len(navegacion) == 21: #21 porque estamos appendeando el origen entonces serian 20 a partir desde el origen
            break

    return navegacion

#--------- Conectividad ---------
def conectados(grafo, pagina, dicc_paginas):
    """nos muestra todos las páginas a los que podemos llegar desde la página pasado 
    por parámetro y que, a su vez, puedan también volver a dicha página."""
    if pagina in dicc_paginas: #como tiene que ser constante en la segunda consulta, lo vamos guardando en un dicc 
        paginas_conectadas = dicc_paginas[pagina]
        print(f"Páginas conectadas a '{pagina}': {', '.join(paginas_conectadas)}.")
        return         
    cfc = biblioteca.cfc_tarjan(grafo)
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

#--------- lectura de 2 am ---------

def lectura_orden(grafo, *paginas):
    """Permite obtener un orden en el que es válido leer las páginas indicados"""

    paginas = list(paginas)
    ordenTopologico = biblioteca.orden_topologico(grafo)
    if ordenTopologico is None :
        print("No existe forma de leer las paginas en orden.")
    else:
        orden = [pagina for pagina in ordenTopologico if pagina in paginas]
        print("Orden de lectura válido: ", ", ".join(orden))

#--------- comunidades ---------

def comunidad(grafo, pagina):
    """ permite obtener la comunidad dentro de la red a la que pertenezca la página pasada por parámetro. Para esto, utilizaremos el sencillo algoritmo
    de Label Propagation."""
    etiquetas= biblioteca.label_propagation(grafo)
    comunidad_pagina = etiquetas.get(pagina)
    if comunidad_pagina is not None:
        print(f"La página {pagina} pertenece a la comunidad {comunidad_pagina}. ")    
    else:
        print(f"No se pudo determinar la comunidad de la pagina {pagina}")

#--------- coeficiente de clustering ---------
def clustering(grafo, pagina):
    """ Permite obtener el coeficiente de clustering de la página indicada. En caso de no indicar página,
    se deberá informar el clustering promedio de la red. En ambos casos, informar con hasta 3 dígitos decimales."""
    if pagina is not None:
        clustering_pagina = biblioteca.calcular_clustering_pagina(grafo, pagina)
        print(f"El coeficiente de clustering de la pagina {pagina} es:{clustering_pagina:.3f}")
    else:
        clustering_promedio= biblioteca.calcular_clustering_promedio(grafo)
        print(f"El clustering promedio de la red es:{clustering_promedio:.3f}")
