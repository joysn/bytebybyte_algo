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
	result.append(root)
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
#print(result)
newlist = list()
for i in range(0,len(result)):
	print(result[i].data,end=" ")
	temp = result[i]
	if i < len(result)-1:
		temp.right = result[i+1]
	else:
		temp.right = result[0]
	if i == 0:
		temp.left = result[len(result) - 1]
	else:
		temp.left = result[i-1]
	newlist.append(temp)
	
print("\n")
print("*************")	

# <- 4 <-> 2 <-> 5 <-> 1 <-> 6 <-> 3 <-> 7 ->

for ele in newlist:
	print(str(ele.data)+"["+str(ele.left.data)+":"+str(ele.right.data)+"]")
		
# (base) D:\>python int21_tree_dll.py
# [4, 2, 5, 1, 6, 3, 7]
# *************
# 4:[7,2]
# 2:[4,5]
# 5:[2,1]
# 1:[5,6]
# 6:[1,3]
# 3:[6,7]
		