# 44. Tree Level Order
# Question: Given a tree, write a function that prints out the nodes of the tree in
# level order.
# ● Eg
# traverse(tree) = 1 2 3 4 5 6 7


class BinaryTree:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None
		
	def setData(self,data):
		self.data = data
		
	def getData(self):
		return self.data
		
	def setLeft(self,left):
		self.left = left
		
	def getLeft(self):
		return self.left
		
	def setRight(self,right):
		self.right = right
		
	def getRight(self):
		return self.right
		
		
	def insertLeft(self,node):
		if self.left is None:
			self.left = node
		else:
			temp = self.left
			self.left = node
			node.left = temp
			
	def insertRight(self,node):
		if self.right is None:
			self.right = node
		else:
			temp = self.right
			self.right = node
			node.right = temp
			
def inorderTrav(root,result):
	if root is None:
		return
	inorderTrav(root.left,result)
	result.append(root.data)
	inorderTrav(root.right,result)
		
def levelOrder(root):
	if root is None:
		return
		
	op = list()
	queue = list()
	queue.append(root)
	while len(queue) > 0:
		curr = queue.pop(0)
		op.append(curr.data)
		if curr.left is not None:
			queue.append(curr.left)
		if curr.right is not None:
			queue.append(curr.right)
	return op
	
		
	
		
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
inorderTrav(b,result)
print("Inorder:- ", result)
print("Level Order:- ",levelOrder(b))
