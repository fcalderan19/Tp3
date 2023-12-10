class _Nodo:
	def __init__(self,dato, proximo = None):
		self.dato = dato
		self.prox = proximo

class Pila:
	def __init__(self):
		self.tope = None

	def Apilar(self,dato):
		self.tope = _Nodo(dato,self.tope)

	def EstaVacia(self):
		return self.tope is None

	def Desapilar(self):
		dato = self.tope.dato
		self.tope = self.tope.prox
		return dato

	def VerTope(self):
		return self.tope.dato