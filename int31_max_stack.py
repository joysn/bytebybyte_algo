# 31. Max Stacks
# ● Question : Implement a LIFO stack that has a push(), pop(), and max() function,
# where max() returns the maximum value in the stack. All of these functions
# should run in O(1) time.
# ● Eg.push(1)
# max() = 1
# push(2)
# max() = 2
# push(1)
# max() = 2
# pop() = 1
# max() = 2
# pop() = 2
# max() = 1


class Node:
	def __init__(self):
		self.data = None
		self.next = None
		self.prevMax = None
		
	def set_data(self,data):
		self.data = data
		
	def get_data(self):
		return self.data
		
	def set_next(self,next):
		self.next = next
		
	def set_prevMax(self,prevMax):
		self.prevMax = prevMax
		
	def get_next(self):
		return self.next
		
		
class MaxStack:
	def __init__(self):
		self.top = None
		self.maxnode = None
		
	def push(self,data):
		node = Node()
		node.set_data(data)
		if self.top is None:
			self.top = node
			self.maxnode = node
		else:
			node.set_next(self.top)
			self.top = node
			if self.maxnode.data < data:
				node.set_prevMax(self.maxnode)
				self.maxnode = node
	
	def pop(self):
		if self.top is None:
			print("Stack is empty")
		else:
			ele = self.top
			self.top = ele.next
			if self.maxnode.data == ele.data:
				self.maxnode = ele.prevMax
			return ele.data
			
	
	def max(self):
		if self.maxnode is not None:
			return self.maxnode.data
		else:
			return None
		
	def display(self):
		if self.top is None:
			print("Stack is empty")
		else:
			temp = self.top
			print("Top:",end=" ")
			while temp is not None:
				print(temp.data,end="(")
				print(temp.prevMax.data,end="") if temp.prevMax else None
				print(")",end="->")
				temp = temp.next
			print(":Bottom",end="")
			print()
			
		
ms = MaxStack()
ms.push(1)
print("Max is:",ms.max())
ms.push(2)
ms.display()
print("Max is:",ms.max())
ms.push(1)
ms.display()
print("Max is:",ms.max())

print("Pop:",ms.pop())
ms.display()
print("Max is:",ms.max())

print("Pop:",ms.pop())
ms.display()
print("Max is:",ms.max())

print("Pop:",ms.pop())
ms.display()
print("Max is:",ms.max())

ms.push(5)
ms.display()
print("Max is:",ms.max())

ms.push(1)
ms.display()
print("Max is:",ms.max())

print("Pop:",ms.pop())
ms.display()
print("Max is:",ms.max())

print("Pop:",ms.pop())
ms.display()
print("Max is:",ms.max())


# (base) D:\>python int31_max_stack.py
# Max is: 1
# Top: 2(1)->1()->:Bottom
# Max is: 2
# Top: 1()->2(1)->1()->:Bottom
# Max is: 2
# Pop: 1
# Top: 2(1)->1()->:Bottom
# Max is: 2
# Pop: 2
# Top: 1()->:Bottom
# Max is: 1
# Pop: 1
# Stack is empty
# Max is: None
# Top: 5()->:Bottom
# Max is: 5
# Top: 1()->5()->:Bottom
# Max is: 5
# Pop: 1
# Top: 5()->:Bottom
# Max is: 5
# Pop: 5
# Stack is empty
# Max is: None

