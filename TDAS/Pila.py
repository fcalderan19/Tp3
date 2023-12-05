class _Nodo:
	def __init__(self,dato, proximo = None):
		self.dato = dato
		self.prox = proximo

class Pila:
	def __init__(self):
		self.tope = None

	def apilar(self,dato):
		self.tope = _Nodo(dato,self.tope)

	def esta_vacia(self):
		return self.tope is None

	def desapilar(self):
		dato = self.tope.dato
		self.tope = self.tope.prox
		return dato

	def ver_tope(self):
		return self.tope.dato