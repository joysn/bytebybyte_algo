# 21. Tree to Doubly Linked List
# ● Question : Given a tree, write a function to convert it into a circular doubly linked
# list from left to right by only modifying the existing pointers.
# ● Eg.

class BinaryTree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		
		
	def set_data(self, data):
		self.data = data
		
	def get_data(self):
		return self.data
		
	def set_left(self,left):
		self.left = left
		
	def set_right(self, right):
		self.right = right
		
	def get_left(self):
		return self.left
		
	def get_right(self):
		return self.right
		
	def insertLeft(self,node):
		if self.left is None:
			self.left = node
		else:
			temp = node
			temp.left = self.left
			self.left = temp
			
			
	def insertRight(self,node):
		if self.right is None:
			self.right = node
		else:
			temp = node
			temp.right = self.right
			self.right = temp
			
			
def inordertrav(root,result):
	if root is None:
		return
	inordertrav(root.left,result)
	result.append(root.data)
	inordertrav(root.right,result)
	
	
b1 = BinaryTree(2)
b1.insertLeft(BinaryTree(4))
b1.insertRight(BinaryTree(5))

b2 = BinaryTree(3)
b2.insertLeft(BinaryTree(6))
b2.insertRight(BinaryTree(7))

b = BinaryTree(1)
b.insertLeft(b1)
b.insertRight(b2)

result = list()
inordertrav(b,result)
# [4, 2, 5, 1, 6, 3, 7]
#        1
#     2      3
#   4   5  6   7
print(result)
print("*************")	

# <- 4 <-> 2 <-> 5 <-> 1 <-> 6 <-> 3 <-> 7 ->

def concatenate(a, b):
	if a is None:
		return b
	if b is None:
		return a
		
	aEnd = a.left
	bEnd = b.left
	
	a.left = bEnd
	bEnd.right = a
	aEnd.right = b
	b.left = aEnd
	
	return a
	
def treeToList(n):
	if n is None:
		return n
	
	leftList = treeToList(n.left)
	rightList = treeToList(n.right)
	n.left = n
	n.right = n
	
	n = concatenate(leftList,n)
	n = concatenate(n,rightList)
	return n
	

n = treeToList(b)
	
def inorderdlltrav(begin):
	root = begin
	while root.right.data != begin.data:
		print(root.data,end=":")
		print('[',end="")
		if root.left is not None:
			print(root.left.data,end=",")
		else:
			print('Null',end=",")
		if root.right is not None:
			print(root.right.data,end="")
		else:
			print('Null',end="")
		print(']')
		root = root.right
	

inorderdlltrav(n)
		
# (base) D:\>python int21_tree_dll.py
# [4, 2, 5, 1, 6, 3, 7]
# *************
# 4:[7,2]
# 2:[4,5]
# 5:[2,1]
# 1:[5,6]
# 6:[1,3]
# 3:[6,7]
		