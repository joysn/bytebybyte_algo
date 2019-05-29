# 13. N Stacks
# Question: Implement N > 0 stacks using a single array to store all stack data (you may use auxiliary arrays in your stack object, but all of the objects in all of
# the stacks must be in the same array). No stack should be full unless the entire array is full.


class Stacks:
	
	def __init__(self, num, capacity):
		self.capacity = capacity
		self.num_of_stacks = num
		
		self.stackData = [None]*capacity
		
		self.nextFree = 0
		
		self.stackTops = [-1]*self.num_of_stacks
		self.stackNum = [None]*self.capacity
		self.stackPrevs = [None]*self.capacity
		
	def __str__(self):
		return ' '.join([str(e) for e in self.stackData])

	def printAuxDS(self):
	
		print("My Stack Nums are:",end=" ")
		for e in self.stackNum:
			print(e,end=" ")
		print("\n")
		
		print("My Stack Prevs are:",end=" ")
		for e in self.stackPrevs:
			print(e,end=" ")
		print("\n")
		
		print("My Stack Tops are:",end=" ")
		for e in self.stackTops:
			print(e,end=" ")
		print("\n")
		
		

	def put(self,snum, val):
	
		# snum indexed from 0
		if self.nextFree >= capacity:
			print("Stack {} is full, so cannot insert the value {}".format(snum,val))
		else:
			self.stackData[self.nextFree] = val
			self.stackNum[self.nextFree] = snum
			self.stackPrevs[self.nextFree] = self.stackTops[snum]
			self.stackTops[snum] = self.nextFree
			self.nextFree += 1
			print("Inserted into Stack {} value {}".format(snum,val))
			
			
	def pop(self, snum):
		myTop = self.stackTops[snum]
		if myTop == -1:
			print("Stack {} is empty".format(snum))
		else:
			self.stackTops[snum] = self.stackPrevs[myTop]
			self.stackNum[myTop] = None
			self.stackPrevs[myTop] = None
			ele = self.stackData[myTop]
			self.stackData[myTop] = None
			self.nextFree = myTop
			return "Popped element from Stack: "+str(snum)+" is: "+str(ele)
		
N = 3;
capacity = 15;
stacks = Stacks(N, capacity);
print(stacks)
stacks.printAuxDS()
print("********************************")
stacks.put(0, 11);
stacks.put(0, 12);
stacks.put(2, 31);
stacks.put(2, 32);
stacks.put(2, 33);
stacks.put(2, 34);
stacks.put(2, 35);
stacks.put(0, 13);
stacks.put(0, 14);
stacks.put(0, 15);
stacks.put(0, 16);
print(stacks)
stacks.printAuxDS()
print("********************************")

print(stacks.pop(2)) # 35;
print(stacks)
stacks.printAuxDS()
print("********************************")

stacks.put(0, 17);
print(stacks)
stacks.printAuxDS()
print("********************************")


print(stacks.pop(2)) # 34;
stacks.put(1, 21);
print(stacks)
stacks.printAuxDS()
print("********************************")

print(stacks.pop(0)) # 17;
print(stacks.pop(0)) # 16;
print(stacks.pop(0)) # 15;
print(stacks.pop(0)) # 14;
print(stacks.pop(0)) # 13;
print(stacks.pop(0)) # 12;
print(stacks.pop(0)) # 11;
print(stacks.pop(0)) # Error
print(stacks)
stacks.printAuxDS()
print("********************************")



# (base) D:\>python int13a.py
# None None None None None None None None None None None None None None None
# My Stack Nums are: None None None None None None None None None None None None None None None

# My Stack Prevs are: None None None None None None None None None None None None None None None

# My Stack Tops are: -1 -1 -1

# ********************************
# Inserted into Stack 0 value 11
# Inserted into Stack 0 value 12
# Inserted into Stack 2 value 31
# Inserted into Stack 2 value 32
# Inserted into Stack 2 value 33
# Inserted into Stack 2 value 34
# Inserted into Stack 2 value 35
# Inserted into Stack 0 value 13
# Inserted into Stack 0 value 14
# Inserted into Stack 0 value 15
# Inserted into Stack 0 value 16
# 11 12 31 32 33 34 35 13 14 15 16 None None None None
# My Stack Nums are: 0 0 2 2 2 2 2 0 0 0 0 None None None None

# My Stack Prevs are: -1 0 -1 2 3 4 5 1 7 8 9 None None None None

# My Stack Tops are: 10 -1 6

# ********************************
# Popped element from Stack: 2 is: 35
# 11 12 31 32 33 34 None 13 14 15 16 None None None None
# My Stack Nums are: 0 0 2 2 2 2 None 0 0 0 0 None None None None

# My Stack Prevs are: -1 0 -1 2 3 4 None 1 7 8 9 None None None None

# My Stack Tops are: 10 -1 5

# ********************************
# Inserted into Stack 0 value 17
# 11 12 31 32 33 34 17 13 14 15 16 None None None None
# My Stack Nums are: 0 0 2 2 2 2 0 0 0 0 0 None None None None

# My Stack Prevs are: -1 0 -1 2 3 4 10 1 7 8 9 None None None None

# My Stack Tops are: 6 -1 5

# ********************************
# Popped element from Stack: 2 is: 34
# Inserted into Stack 1 value 21
# 11 12 31 32 33 21 17 13 14 15 16 None None None None
# My Stack Nums are: 0 0 2 2 2 1 0 0 0 0 0 None None None None

# My Stack Prevs are: -1 0 -1 2 3 -1 10 1 7 8 9 None None None None

# My Stack Tops are: 6 5 4

# ********************************
# Popped element from Stack: 0 is: 17
# Popped element from Stack: 0 is: 16
# Popped element from Stack: 0 is: 15
# Popped element from Stack: 0 is: 14
# Popped element from Stack: 0 is: 13
# Popped element from Stack: 0 is: 12
# Popped element from Stack: 0 is: 11
# Stack 0 is empty
# None
# None None 31 32 33 21 None None None None None None None None None
# My Stack Nums are: None None 2 2 2 1 None None None None None None None None None

# My Stack Prevs are: None None -1 2 3 -1 None None None None None None None None None

# My Stack Tops are: -1 5 4

# ********************************
