import random

class Grafo:
    def __init__(self, dirigido = False):
        self.dirigido = dirigido
        self.vertices = {}

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}

    def agregar_arista(self, v, w, peso):
        if v in self.vertices and w in self.vertices:
            self.vertices[v][w] = peso
            if not self.dirigido:
                self.vertices[w][v] = peso
        elif v in self.vertices:
            raise NameError (f"No se pudo agregar la arista debido a que {w} no existe")
        elif w in self.vertices:
            raise NameError (f"No se pudo agregar la arista debido a que {v} no existe")

    def borrar_vertice(self, v):
        if v in self.vertices:
            del self.vertices[v]

            for adyacentes in self.vertices.values():
                adyacentes_ = dict(adyacentes)
                for adyacente in adyacentes_.keys():
                    if adyacente == v:
                        del adyacentes[adyacente]
        else:
            raise NameError (f"No se pudo borrar {v} debido a que no existe")


    def borrar_arista(self, v, w):
        if v in self.vertices and w in self.vertices:
            del self.vertices[v][w]
            if not self.dirigido:
                del self.vertices[w][v]
        else:
            raise NameError (f"No se pudo borrar debido a que no existe la arista entre {v} y {w}")

    def obtener_vertices(self):
        verticesTotales = []
        for vertice in self.vertices.keys():
            verticesTotales.append(vertice)
        return verticesTotales

    def adyacentes(self, v):
        ady = []
        if v in self.vertices.keys():
            for adyacente in self.vertices[v]:
                ady.append(adyacente)
        return ady
    
    def estan_unidos(self, v, w):
        return w in self.vertices[v]
    
    def peso_arista(self, v, w):
        if self.estan_unidos(v, w):
            return self.vertices[v][w]
        raise NameError (f"No se pudo obtener el peso debido a que no existe la arista entre {v} y {w}")
    
    def vertice_aleatorio(self):
        return random.choice(self.vertices)
    
    def verticeExistente(self, v):
        return v in self.vertices
    