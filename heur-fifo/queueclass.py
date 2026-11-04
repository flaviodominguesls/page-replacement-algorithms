class Queue:
	
	def __init__(self, length):	
		self.length = length
		self.items = []
		
	def is_empty(self):
		return len(self.items) == 0
		
	def is_full(self):
		return len(self.items) == self.length

	def enqueue(self, element):
		self.items.append(element)

	def dequeue(self):
		if self.is_empty():
			return IndexError("POP PROIBIDO: não há como remover algo de uma pilha vazia")
		return self.items.pop(0)

	def head(self):
		if self.is_empty():
			return IndexError("PEEK PROIBIDO: não existe topo em pilha vazia")
		return self.items[0]

	def size(self):
		return len(self.items)

	def __str__(self):
		return f'Fila Atual: {list(self.items)}'
