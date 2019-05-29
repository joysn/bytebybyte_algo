# 13. N Stacks
# ● Question: Implement N > 0 stacks using a single array to store all stack data
# (you may use auxiliary arrays in your stack object, but all of the objects in all of
# the stacks must be in the same array). No stack should be full unless the entire
# array is full.


class Stacks:
	
	def __init__(self, num, capacity):
		self.capacity = capacity
		self.num_of_stacks = num
		self.myList = [None]*capacity*num
		self.myTopList = [0]*num
		
	def __str__(self):
		return ' '.join([str(e) for e in self.myList])

	def printTopList(self):
		print("My Stack Tops are:",end=" ")
		for e in stacks.myTopList:
			print(e,end=" ")
		print("\n")

	def put(self,snum, val):
		# snum indexed from 0
		myTop = self.myTopList[snum]
		if myTop >= capacity:
			print("Stack {} is full, so cannot insert the value {}".format(snum,val))
		else:
			self.myList[snum*self.capacity+myTop] = val
			self.myTopList[snum] += 1
			print("Inserted into Stack {} value {}".format(snum,val))
			#pass
			
	def pop(self, snum):
		myTop = self.myTopList[snum]
		if myTop == 0:
			print("Stack {} is empty".format(snum))
		else:
			self.myTopList[snum] -= 1
			ele = self.myList[snum*self.capacity+myTop-1]
			self.myList[snum*self.capacity+myTop-1] = None
			return "Popped element from Stack: "+str(snum)+" is: "+str(ele)
		
N = 3;
capacity = 5;
stacks = Stacks(N, capacity);
print(stacks)
stacks.printTopList()
stacks.put(0, 11);
stacks.put(0, 12);
stacks.put(0, 13);
stacks.put(0, 14);
stacks.put(0, 15);
stacks.put(0, 16);
stacks.put(2, 31);
stacks.put(2, 32);
stacks.put(2, 33);
stacks.put(2, 34);
stacks.put(2, 35);
stacks.put(2, 36);
print(stacks)
stacks.printTopList()

print(stacks.pop(0)) # 15;
print(stacks.pop(2)) # 35;
print(stacks)
stacks.printTopList()


print(stacks.pop(0)) # 14;
print(stacks.pop(0)) # 13;
print(stacks.pop(0)) # 12;
print(stacks.pop(0)) # 11;
print(stacks.pop(0)) # Error;
print(stacks)
stacks.printTopList()
