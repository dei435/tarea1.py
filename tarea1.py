class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
	
	def top(self):
		return self.items[len(self.items)-1]
	
	def size(self):
		return len(self.items)

arreglo = [5, -7, 8, 3, -11, 22, 6]
print("Arreglo:", arreglo)

def my_stack_function(entrada):
	pila = Stack()
	while entrada != []:
		auxiliar1 = entrada[len(entrada)-1]
		entrada.pop()
		while pila.isEmpty() == False and auxiliar1 < pila.top():
			auxiliar2 = pila.top()
			entrada.append(auxiliar2)
			pila.pop()
		else:
			pila.push(auxiliar1)

	print("Pila:", pila.items)

my_stack_function(arreglo)
