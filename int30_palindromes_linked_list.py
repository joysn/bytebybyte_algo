# 30. Palindromes
# ● Question : Given a linked list, write a function to determine whether the list is a
# palindrome.
# ● Eg.
# palindrome(1 -> 2 -> 3) = false
# palindrome(1 -> 2 -> 1) = true

class Node:
	def __init__(self,data):
		self.next = None
		self.data = data
		
	def set_data(self,data):
		self.data = data
		
	def get_data(self):
		return self.data
		
	def set_next(self,next):
		self.next = next
		
	def get_next(self):
		return self.next
		
	def has_next(self):
		return self.next != None
		
	
class LinkedList:
	def __init__(self):
		self.head = None
		
		
	def insertAtBegining(self,data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
	
	def insertAtEnd(self,data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			curr = self.head
			while(curr.next != None):
				curr = curr.next
			curr.next = node
			
	def display(self):
		if self.head is None:
			print("The Linked list is empty")
		else:
			curr = self.head
			while(curr is not None):
				print(curr.data,end = "->")
				curr = curr.next
			print()
			
class Stack:
	def __init__(self):
		self.top = None
		
	def push(self,data):
		node = Node(data)
		print(node.data) if debug else None
		if self.top == None:
			self.top = node
		else:
			node.next = self.top
			self.top = node
			
	def pop(self):
		if self.top is None:
			print("Stack is empty")
		else:
			temp = self.top
			self.top = temp.next
			return temp.data
			
	def display(self):
		if self.top is None:
			print("Stack is empty")
		else:
			temp = self.top
			print("Top",end=" ")
			while temp is not None:
				print(temp.data,end="->")
				temp = temp.next
			print("Bottom")
		
def ispalindrome(l1):
	if l1.head is None:
		return True
	front = l1.head
	tor = l1.head
	hare = l1.head
	stack = Stack()
	while (hare is not None):
		stack.push(tor.data)
		tor = tor.next
		if hare.next is not None:
			hare = hare.next.next 
		else:
			hare = None
			stack.pop()
			
	stack.display() if debug else None
		
	while tor is not None:
		temp = stack.pop()
		if tor.data != temp:
			return False
		else:
			tor = tor.next
			
	return True
		
	
	
debug = False
l1 = LinkedList()
l1.insertAtBegining(1)
l1.insertAtEnd(2)
l1.insertAtEnd(3)
print("The list is: ",end="")
l1.display()
print("Is palindrom:",ispalindrome(l1))	
	
l2 = LinkedList()
l2.insertAtBegining(1)
l2.insertAtEnd(2)
l2.insertAtEnd(1)
print("The list is: ",end="")
l2.display()
print("Is palindrom:",ispalindrome(l2))	


l2 = LinkedList()
l2.insertAtBegining(1)
l2.insertAtEnd(2)
l2.insertAtEnd(3)
l2.insertAtEnd(3)
l2.insertAtEnd(2)
l2.insertAtEnd(1)
print("The list is: ",end="")
l2.display()
print("Is palindrom:",ispalindrome(l2))	


l2 = LinkedList()
l2.insertAtBegining(1)
l2.insertAtEnd(2)
l2.insertAtEnd(3)
l2.insertAtEnd(5)
l2.insertAtEnd(3)
l2.insertAtEnd(2)
l2.insertAtEnd(1)
print("The list is: ",end="")
l2.display()
print("Is palindrom:",ispalindrome(l2))	

# (base) D:\>python int30_palindromes_linked_list.py
# The list is: 1->2->3->
# Is palindrom: False
# The list is: 1->2->1->
# Is palindrom: True
# The list is: 1->2->3->3->2->1->
# Is palindrom: True
# The list is: 1->2->3->5->3->2->1->
# Is palindrom: True
