class _Nodo:
	def __init__(self,dato, proximo = None):
		self.dato = dato
		self.prox = proximo

class Cola:

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def EstaVacia(self):
		return self.primero is None

	def Encolar(self,dato):
		nuevo = _Nodo(dato)
		if self.ultimo is None:
			self.primero = nuevo
		else:
			self.ultimo.prox = nuevo
			
		self.ultimo = nuevo

	def Desencolar(self):
		dato = self.primero.dato
		self.primero = self.primero.prox
		if not self.primero:
			self.ultimo = None
		return dato

	def VerPrimero(self):
		return self.primero.dato
