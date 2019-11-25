# 28. Sort Stacks
# ● Question : Given a stack, sort the elements in the stack using one additional
# stack.
# ● Eg.
# sort([1, 3, 2, 4]) = [1, 2, 3, 4]


class Node:
	def __init__(self):
		self.data = None
		self.next = None
		
	def get_data(self):
		return self.data
		
	def set_data(self,data):
		self.data = data
		
	def set_next(self,next):
		self.next = next
		
	def get_next(self):
		return self.next
		
	def has_next(self):
		return self.next != None
		
class Stack:
	def __init__(self,data):
		self.top = None
		if data is not None:
			self.push(data)
			
	def push(self,data):
		node = Node()
		node.set_data(data)
		node.set_next(self.top)
		self.top = node
	
	def pop(self):
		if self.isempty():
			return
		else:
			temp = self.top.get_data()
			self.top = self.top.get_next()
			return temp
	
	def isempty(self):
		return self.top == None
		
		
	def display(self):
		node = self.top
		print("Top:",end= " ")
		while node is not None:
			print(node.data, end = " ")
			node = node.next
		print()
		
		
stack = Stack(None)
stack.push(1)
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(4)

stack.display() # O(n)
stackop = Stack(None)
while stack.isempty() != True: # O(n)
	data = stack.pop()
	if stackop.isempty():
		stackop.push(data)
	else:
		# Commented out code is not required and is not necssary. But it does not affect the efficiency
		#stack.push(100000)
		while stackop.top and stackop.top.data < data: #O(n-i)
			stack.push(stackop.pop())
		stackop.push(data)
		#while stack.top and stack.top.data!= 100000:
		#	stackop.push(stack.pop())
		#stack.pop()
	
stackop.display()
#stack.display()