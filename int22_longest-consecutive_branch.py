# 22. Longest Consecutive Branch
# ● Question: Given a tree, write a function to find the length of the longest branch of
# nodes in increasing consecutive order.
# ● Eg.


class BinaryTree:

	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.size = 1
		
	def set_data(self,data):
		self.data = data
		
	def get_data(self):
		return self.data
		
	def set_left(self,left):
		self.left = right
	
	def set_right(self,right):
		self.right = right
		
	def get_left(self):
		return self.left
		
	def get_right(self):
		return self.right
		
	def insertLeft(self,node):
		if self.left == None:
			self.left = node
		else:
			temp = self.left
			self.left = node
			node.left = temp
			
	def insertRight(self,node):
		if self.right == None:
			self.right = node
		else:
			temp = self.right
			self.right = node
			node.right = temp
			
	
def inorderTrav(root,result):
	global maxSize
	if root == None:
		return
	else:
		#print(root.data, root.size)

		if root.left is not None:
			if root.left.data == root.data + 1:
				root.left.size = root.size + 1
				if root.left.size > maxSize:
					maxSize = root.left.size
			elif root.right.data == root.data + 1:
				root.right.size = root.size + 1
				if root.right.size > maxSize:
					maxSize = root.right.size
		
		inorderTrav(root.left, result)
		result.append(root)
		inorderTrav(root.right, result)
		
		
b1 = BinaryTree(1)
b1.insertLeft(BinaryTree(1))
b1.insertRight(BinaryTree(2))

b2 = BinaryTree(2)
b2.insertLeft(BinaryTree(1))
b2.insertRight(BinaryTree(3))

b = BinaryTree(0)
b.insertLeft(b1)
b.insertRight(b2)

global maxSize
maxSize = 1
result = list()
inorderTrav(b,result)
# [4, 2, 5, 1, 6, 3, 7]
#        1
#     2      3
#   4   5  6   7
for ele in result:
	print(str(ele.data)+"["+str(ele.size)+"]")
print("*************")	
print(maxSize)


# (base) >python int22_longest-consecutive_branch.py
# 1[1]
# 1[2]
# 2[3]
# 0[1]
# 1[1]
# 2[1]
# 3[2]
# *************
# 3



			