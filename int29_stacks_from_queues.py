# 29. Stack from Queues
# ● Question : Implement a LIFO stack with basic functionality (push and pop) using
# FIFO queues to store the data.


class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
	def set_data(self,data):
		self.data = data
	
	def get_data(self):
		return self.data
		
		
class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
		
	def enqueue(self, node):
		if self.front == None:
			self.front = node
			self.rear = node
		else:
			self.rear.next = node
			self.rear = node
		
	def dequeue(self):
		if self.front is not None:
			temp = self.front
			self.front = temp.next
			return temp
		else:
			print("Empty queue")
			return
	
	def push(self,node):
		if self.front is None:
			self.front = node
			self.rear = node
		else:
			node.next = self.front
			self.front = node
			
	def pop(self):
		return(self.dequeue())
		
	def display(self):
		temp = self.front
		
		if self.front == None:
			print("Queue is Empty")
		else:
			temp = self.front
			print("Front->",end=" ")
			while temp is not None:
				print(temp.data, end=" ")
				temp = temp.next
			print("<-Rear")
			
q = Queue()
q.enqueue(Node(1))
q.display()
q.enqueue(Node(2))
q.display()
q.enqueue(Node(3))
q.display()

print("Dequeuing:- ",q.dequeue().data)
q.display()
print("Dequeuing:- ",q.dequeue().data)
q.display()
print("Dequeuing:- ",q.dequeue().data)
q.display()

q.enqueue(Node(1))
q.enqueue(Node(2))
q.enqueue(Node(3))
q.display()
q.push(Node(4))
q.push(Node(5))
q.display()
print("Popping:- ",q.pop().data)
q.display()
print("Popping:- ",q.pop().data)
print("Popping:- ",q.pop().data)
print("Popping:- ",q.pop().data)
print("Popping:- ",q.pop().data)
q.display()