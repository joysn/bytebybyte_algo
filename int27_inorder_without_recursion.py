# 27. Inorder Traversal
# ● Question : Given a binary search tree, print out the elements of the tree in order
# without using recursion


class BinaryTree:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		
	def get_right(self):
		return self.right
		
	def get_left(self):
		return self.left
		
	def set_right(self,node):
		if self.right == None:
			self.right = node
		else:
			temp = self.right
			self.right = node
			node.right = temp
			
	def set_left(self,node):
		if self.left == None:
			self.left = node
		else:
			temp = self.left
			self.left = node
			node.left = temp
	
class Node:
	def __init__(self):
		self.data = None
		self.next = None
	
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

class Stack:
	def __init__(self,data):
		self.top = None
		if data is not None:
			self.push(data)
				
	def push(self,n):
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
	
#         1	
#    2	       3	
# 4    5     6      7
#        8 9  10 11  12
#		 13
b8 = BinaryTree(8)
b5 = BinaryTree(5)
b5.set_right(b8)
b4 = BinaryTree(4)
b2 = BinaryTree(2)
b2.set_left(b4)
b2.set_right(b5)

b13 = BinaryTree(13)
b9 = BinaryTree(9)
b9.set_left(b13)
b10 = BinaryTree(10)
b6 = BinaryTree(6)
b6.set_left(b9)
b6.set_right(b10)

b7 = BinaryTree(7)
b11 = BinaryTree(11)
b12 = BinaryTree(12)
b7.set_left(b11)
b7.set_right(b12)

b3 = BinaryTree(3)
b3.set_left(b6)
b3.set_right(b7)

b1 = BinaryTree(1)
b1.set_left(b2)
b1.set_right(b3)

def inordertrav(root):
	if root is None:
		return
	else:
		inordertrav(root.left)
		print(root.data,end=" ")
		inordertrav(root.right)
		
def preordertrav(root):
	if root is None:
		return
	else:
		print(root.data,end=" ")
		preordertrav(root.left)
		preordertrav(root.right)




def inordertravnonrecur(root,result):
	if root is None:
		return
	stack = Stack(None)
	node = root
	while stack.isempty() != True or node is not None:
		if node:
			stack.push(node)
			node = node.left
		else:
			node = stack.pop()
			#result.append(node.data)
			print(node.data,end= " ")
			node = node.right
		
			
def preordertravnonrecur(root,result):
	if root is None:
		return
	stack = Stack(None)
	node = root
	while stack.isempty() != True or node is not None:
		if node is not None:
			print(node.data, end = " ")
			stack.push(node)
			node = node.left
		else:
			node = stack.pop()
			node = node.right

print("Using recursion inorder")
inordertrav(b1)
print("\n******************************")

print("Not Using recursion inorder")
result = list()
inordertravnonrecur(b1,result)
print("\n******************************")

print("Using recursion preorder")
preordertrav(b1)
print("\n******************************")

print("Not Using recursion preorder")
result = list()
preordertravnonrecur(b1,result)
print("\n******************************")



#print(result)

# (base) D:\>python int27_inorder_without_recursion.py
# Using recursion
# 4 2 5 8 1 13 9 6 10 3 11 7 12
# ******************************
# Not Using recursion
# 4 2 5 8 1 13 9 6 10 3 11 7 12
# ******************************
# Using recursion preorder
# 1 2 4 5 8 3 6 9 13 10 7 11 12
# ******************************