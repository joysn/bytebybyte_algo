# 23. Print Reversed Linked List
# ● Question: Given a linked list, write a function that prints the nodes of the list in
# reverse order.
# ● Eg.


class LinkedList:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def set_data(self,data):
		self.data = data
	
	def get_data(self):
		return self.data
		
		
	def setNext(self,node):
		self.next = node
		
	def getNext(self):
		return self.next
		
	def hasNext(self):
		return self.next != None
		
	def insertAtEnd(self,node):
		temp = self
		while temp.next != None:
			temp = temp.next
		temp.next = node
		
l1 = LinkedList(1)
l2 = LinkedList(2)
l1.insertAtEnd(l2)
l3 = LinkedList(3)
l1.insertAtEnd(l3)

def display(head):
	if head is not None:
		print(head.data,end="->")
		while head.next is not None:
			head = head.next
			print(head.data,end="->")
		print("\n")
			
display(l1)

def reverse(head):
	if head is None:
		return
	else:
		reverse(head.next)
		print(head.data,end="->")

reverse(l1)