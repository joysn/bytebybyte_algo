# 38. Linked List Cycles
# ● Question : Given a linked list, determine whether it contains a cycle.
# ● Eg.
# 1 ‑> 2 ‑> 3 ‑> 4
# ^ |
# |_________|

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
	def setData(self,data):
		self.data = data
		
	def setNext(self,next):
		self.next = next
		
	def getData(self):
		return self.data
		
	def getNext(self):
		return self.next
		
		
class LinkedList:
	def __init__(self,front = None, rear=None):
		self.front = front
		self.rear = front
		
	def add(self,n):
		if self.front is None:
			self.front = n
			self.rear = n
		else:
			self.rear.next = n
			self.rear = n
		
	def delete(self):
		if self.rear is None:
			print("Linked List is empty")
		else:
			n = self.rear
			if self.rear == self.front:
				self.rear = None
				self.front = None
			else:
				prev = self.front
				while prev.next != self.rear:
					prev = prev.next
				prev.next = None
				self.rear = prev
			return n
		
	def display(self):
		if self.front is None:
			print("Linked List is empty")
		else:
			temp = self.front
			while temp is not None:
				print(temp.getData(),end="->")
				temp = temp.next
			print()
			
	def hasCircle(self):
		if self.front is None:
			print("Linked List is empty, so no question of cycles")
		elif self.front == self.rear:
			if self.rear.next is not None:
				print("Has cycle")
			else:
				print("No cycles")
		else:
			hare = self.front.next if self.front else None
			rabbit = self.front.next.next if self.front.next else None
			print(hare.getData(), rabbit.getData()) if debug else None
			while hare != rabbit:
				if hare is None:
					print("No cycles")
					return
				elif rabbit is None:
					print("No cycles")
					return
				else:
					hare = hare.next if hare else None
					rabbit = rabbit.next.next if rabbit.next else None
			print("Has cycle")
			
		
		
debug = True
ll = LinkedList()
n1 = Node(1)
ll.add(n1)
n2 = Node(2)
ll.add(n2)
n3 = Node(3)
ll.add(n3)
ll.display()
n4 = Node(4)
n4.setNext(n2)
print("Last Node:",n4.data,"Has next node:", n4.getNext().data) if debug else None
ll.add(n4)
ll.hasCircle()
#ll.hasCircle()
#ll.display()