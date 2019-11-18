# 20. Reverse Stack
# ● Question: Given a stack, reverse the items without creating any additional data
# structures.
# ● Eg.
# reverse(1->2->3) = 3->2->1

class Node:
	def __init__(self):
		self.data = None
		self.next = None
		# method for setting the data field of the node    
	def set_data(self, data):
		self.data = data
		# method for getting the data field of the node   
	def get_data(self):
		return self.data
		# method for setting the next field of the node
	def set_next(self, next):
		self.next = next
		# method for getting the next field of the node    
	def get_next(self):
		return self.next
	# returns true if the node points to another node
	def has_next(self):
		return self.next != None
		
		

class Stack:
	def __init__(self,data):
		self.top = None
		if data is not None:
			for e in data:
				self.push(e)
		
	def push(self, n):
		node = Node()
		node.set_data(n)
		node.set_next(self.top)
		self.top = node
		
	
	def pop(self):
		if self.top is None:
			return "Empty"
		temp = self.top.get_data()
		self.top = self.top.get_next()
		return temp
		
	def isempty(self):
		if self.top is None:
			return True
		else:
			return False
			
	def peek(self):
		if self.top is None:
			return "Empty"
		return self.top.get_data()
	
	def display(self):
		curr = self.top
		while curr is not None:
			print(curr.get_data())
			curr = curr.get_next()
		
s1 = Stack([1,2,3])
# print(s1.peek())
# print(s1.pop())
# print(s1.peek())
s1.display()
print("********")


def reverse(s1):
	if s1.isempty():
		return s1
	temp = s1.pop()
	s1 = reverse(s1)
	pushatbottom(s1,temp)
	return s1
	
def pushatbottom(s1,x):
	debug = False
	print("Pushing t",x) if debug else None
	if s1.isempty():
		s1.push(x)
		return
	temp = s1.pop()
	pushatbottom(s1,x)
	s1.push(temp)
		
		
reverse(s1)
s1.display()