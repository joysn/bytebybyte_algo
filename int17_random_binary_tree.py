# 17. Random Binary Tree
# Question: Implement a binary tree with a method getRandomNode() that returns
# a random node.
# Eg.
# getRandomNode() = 5
# getRandomNode() = 8
# getRandomNode() = 1

import random

class BSTNode:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		self.children = 0
		
def insertNode(root, node):
	if root is None:
		root = node
	else:
		if root.data > node.data:
			if root.left == None:
				root.left = node
				root.children = root.children + 1
			else:
				root.children = root.children + 1
				insertNode(root.left, node)
		else:
			if root.right == None:
				root.right = node
				root.children = root.children + 1
			else:
				root.children = root.children + 1
				insertNode(root.right, node)					
	
def inOrderTraversal(root):
	if not root:
		return
	print(root.data,'(',root.children,')',end='->')
	inOrderTraversal(root.left)
	inOrderTraversal(root.right)
		
	
def getchildren(n):
	if n is None:
		return 0
	return n.children+1
	
def getRandomNode(root):
	if root is None:
		return -1
	count = random.randint(1,root.children)
	#count = 6
	print("Count is",count)
	print("Node is", getRandomNode1(root, count))
	
    # 5
   # / \
  # 2   7
 # / \ / \
# 1  36   8

def getRandomNode1(curr, count):
	debug = False
	print("Data",curr.data,"Count",count,"Children:",getchildren(curr),"Left Children:",getchildren(curr.left)) if debug else None
	if count == getchildren(curr.left):
		return curr.data
	if count < getchildren(curr.left):
		return getRandomNode1(curr.left, count)
	if curr.right is not None:
		return getRandomNode1(curr.right, count - getchildren(curr.left) - 1)
	return curr.right.data
		
	
root = BSTNode(3)
insertNode(root, BSTNode(7))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(5))
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(9))
    # 3
   # / \
  # 1   7
 # / \ / \
   # 2 5 9
inOrderTraversal(root)
print()
# 2->1->2->7->5->9
# (base) D:\>python int18.py
# 3->1->2->7->5->9->
# 3 ( 5 )->1 ( 1 )->2 ( 0 )->7 ( 2 )->5 ( 0 )->9 ( 0 )->


root = BSTNode(5)
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(7))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(3))
insertNode(root, BSTNode(6))
insertNode(root, BSTNode(8))
    # 5
   # / \
  # 2   7
 # / \ / \
# 1  36   8
inOrderTraversal(root)
print()
# 5->2->1->3->7->6->8->
# 5 ( 6 )->2 ( 2 )->1 ( 0 )->3 ( 0 )->7 ( 2 )->6 ( 0 )->8 ( 0 )->


getRandomNode(root)
# getRandomNode() = 8
# getRandomNode() = 1