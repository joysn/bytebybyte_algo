# Nth to the Last Element
# ● Question: Given a linked list, and an input n, write a function that returns the
# nth-to-last element of the linked list.
# ● Eg. Given a linked list, and an input n, write a function that returns the nth-to-last
# element of the linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
	def setData(self,data):
		self.data = data
		
	def setNext(self,n):
		self.next = n
		
	def getNext(self):
		return self.next
	
	def getData(self):
		return self.data
		
		
		
class LinkedList:
	
	def __init__(self,front=None, rear= None):
		self.front = front
		self.rear = rear
		self.count = 0
		
	def add(self,node):
		if self.front is None:
			self.front = node
			self.rear = node
			self.count += 1
		else:
			self.rear.next = node
			self.rear = node
			self.count += 1
			
	def delete(self):
		if self.rear is None:
			print("No node to delete")
		else:
			n = self.rear
			if self.rear == self.front:
				self.front = None
				self.rear = None
				self.count -= 1
			else:
				prev = self.front
				while prev.next != self.rear:
					prev = prev.next
				prev.next = None
				self.rear = prev
				self.count -= 1
			return n
			
	def display(self):
		if self.rear is None:
			print("No nodes present",self.count)
		else:
			p = self.front
			print("[Front]",end="")
			while p.next is not None:
				print(p.data,end="->")
				p = p.next
			print(p.data,"[Rear] Total Elements:-",self.count)
			
			
	def nth_to_last(self,n):
		if n < 0:
			print("Invalid value of n:",n)
		elif n >= self.count:
			print("No element to delete ",n,"th element from last")
		else:
			count_from_front = self.count - n
			#print(n,self.count,count_from_front)
			ele = self.front
			for i in range(1,count_from_front):
				ele = ele.next
			print(n,"th element from last is:",ele.data)
			
		
		
ll = LinkedList()
n1 = Node(1)
ll.add(n1)
n2 = Node(2)
ll.add(n2)
n3 = Node(3)
ll.add(n3)
n4 = Node(4)
ll.add(n4)
n5 = Node(5)
ll.add(n5)
ll.display()
for i in range(6):
	ll.nth_to_last(i)
ll.delete()
ll.display()
for i in range(6):
	ll.nth_to_last(i)
	
	
# (base) D:\>python algo42_nth_last_ele.py
# [Front]1->2->3->4->5 [Rear] Total Elements:- 5
# 0 th element from last is: 5
# 1 th element from last is: 4
# 2 th element from last is: 3
# 3 th element from last is: 2
# 4 th element from last is: 1
# No element to delete  5 th element from last
# [Front]1->2->3->4 [Rear] Total Elements:- 4
# 0 th element from last is: 4
# 1 th element from last is: 3
# 2 th element from last is: 2
# 3 th element from last is: 1
# No element to delete  4 th element from last
# No element to delete  5 th element from last

		
			