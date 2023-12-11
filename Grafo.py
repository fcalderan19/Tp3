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

    def borrar_vertice(self, v):
        if v in self.vertices:
            del self.vertices[v]

        for vertice in self.vertices:
            adyacentes = self.vertices[vertice]

        for adyacente in adyacentes:
            if adyacente == v:
                del adyacentes[adyacente]

    def borrar_arista(self, v, w):
        if v in self.vertices and w in self.vertices:
            del self.aristas[v][w]
            if not self.dirigido:
                del self.vertices[w][v]

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
        if self.estan_unidos:
            return self.vertices[v][w]
    
    def vertice_aleatorio(self):
        return random.choice(self.vertices)
    
    def verticeExistente(self, v):
        return v in self.vertices
    

    
    
    

    


    