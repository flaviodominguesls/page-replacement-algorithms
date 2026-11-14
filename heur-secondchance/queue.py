class Queue:
	
	def __init__(self, length):	
		self.length = length
		self.items = []
		
	def is_empty(self):
		return len(self.items) == 0
		
	def is_full(self):
		return len(self.items) == self.length

	def enqueue(self, pagina):
		self.items.append(pagina)

	def dequeue(self):
		if self.is_empty():
			return IndexError("PROIBIDO DESENFILERAR: não há como remover algo de uma fila vazia")
		return self.items.pop(0)

	def head(self):
		if self.is_empty():
			return IndexError("SEM CABECA: não existe head em fila vazia")
		return self.items[0]

	def size(self):
		return len(self.items)
    
    # Metodo Novo: buscar uma página pelo número
    def search(self, num):
        for page in self.items:
            if page.number == num:
                return page
        return None

	def __str__(self):
		return f'Fila Atual: {list(self.items)}'
