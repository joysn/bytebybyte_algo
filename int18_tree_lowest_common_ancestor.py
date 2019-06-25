# Lowest Common Ancestor
# Question: Given two nodes in a binary tree, write a function to find the lowest common ancestor.
# Eg.
# lcs(4, 3) = 1
# lcs(6, 7) = 3


class BinaryTree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data # Root
		self.parent = list()
		
	def insertLeft(self, node):
		if self.left is None:
			self.left = node
			node.parent += self.parent
			node.parent.append(self)
		else:
			node.left = self.left
			node.left.parent.append(node)
			self.left = node
			self.left.parent.append(self)
			
	def insertRight(self, node):
		if self.right is None:
			node.parent += self.parent
			node.parent.append(self)
			self.right = node
		else:
			node.right = self.right
			node.right.parent.append(self)
			self.right = node
			self.right.parent.append(self)

	
	
def inOrderTraversal(root):
	if not root:
		return
	if root.parent is not None:
		print(root.data,end=':-')
		for e in root.parent:
			print(e.data,end='->')
		print()
	else:
		print(root.data,'( NULL )',end='->')
	inOrderTraversal(root.left)
	inOrderTraversal(root.right)
		
	
def inOrderSearch(root, n):
	debug = False
	op = list()
	if root is None:
		return op,0
	if root.data == n.data:
		op.append(root.data)
		return op,1
	else:
		op.append(root.data)
		print("Calling inOrderSearch with ",root.left.data ,"and",n.data ) if debug else None
		op_temp,found = inOrderSearch(root.left,n)
		if found == 1:
			op += op_temp
			return op,1
		else:
			op_temp,found = inOrderSearch(root.right,n)
			if found == 1:
				op += op_temp
				return op,1
			else:
				op.pop()
				return op,0
	return op,0

def find_lcm(p1,p2):
	len1 = len(p1)
	len2 = len(p2)
	
	op = list()
	
	if len1 > len2:
		blen = len1
	else:
		blen = len2
		
	for i in range(blen):
		if p1[i] == p2[i]:
			op.append(p1[i])
		else:
			break
	return op

root1 = BinaryTree(2)
root1.insertLeft(BinaryTree(4))
root1.insertRight(BinaryTree(5))
#inOrderTraversal(root1)
#print("***********")

root2 = BinaryTree(3)
root2.insertLeft(BinaryTree(6))
root2.insertRight(BinaryTree(7))
#inOrderTraversal(root2)
#print("***********")

root = BinaryTree(1)
root.insertLeft(root1)
root.insertRight(root2)
print("The Tree is ")
inOrderTraversal(root)
print("***********")

    # # 1
   # # / \
  # # 2   3
 # # / \ / \
# # 4  56   7

path1, found1 = inOrderSearch(root,BinaryTree(6)) # O(n)
path2, found2 = inOrderSearch(root,BinaryTree(7))
# print(path1)
# print(path2)
print("The LCM of 6 & 7 is", end=":")
print(find_lcm(path1,path2)[-1]) #O(logn)


path1, found1 = inOrderSearch(root,BinaryTree(3))
path2, found2 = inOrderSearch(root,BinaryTree(4))
# print(path1)
# print(path2)
print("The LCM of 3 & 4 is", end=":")
print(find_lcm(path1,path2)[-1])


# (base) D:\>python int18.py
# The Tree is
# 1:-
# 2:-1->
# 4:-2->
# 5:-2->
# 3:-1->
# 6:-3->
# 7:-3->
# ***********
# The LCM of 6 & 7 is:3
# The LCM of 3 & 4 is:1