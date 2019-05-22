from heapq import heappush, heappop, heapify

# using minHeap()
# T = O(nk* log(k))
# log(k) is getting min for each heap
# we do this nk times i.e. for every element

class MinHeap(object):
	
	def __init__(self):
		self.heap = []
		
	def __str__(self):
		return ' '.join([str(ele) for ele in self.heap])
		
	def insertKey(self,key):
		heappush(self.heap,key)
		
	def removeMin(self):
		return heappop(self.heap)
		
	def getMin(self):
		return self.heap[0]
	def getSize(self):
		return len(self.heap)
		
		
def merge(l):

	debug = False
	myHeap = MinHeap()
	op = list()
	row_list = list()
	for row in range(len(l)):
		row_list.append(0)
	#print(row_list) if debug else None
	
	while True :
		for row in range(len(row_list)):
			if row_list[row] != -1:
				myHeap.insertKey((l[row][row_list[row]],row))
		print("Heap state after 3 inserts {}".format(myHeap)) if debug else None
		min_ele = myHeap.removeMin()
		print("Heap state after min delete {}".format(myHeap)) if debug else None
		
		op.append(min_ele[0])
		print("Output list {}".format(op)) if debug else None
		print(myHeap.getSize()) if debug else None
		if myHeap.getSize() == 0:
			break
		myHeap = MinHeap()
		print("Before update row_list {}".format(row_list)) if debug else None
		
		row_list[min_ele[1]] += 1
		if (row_list[min_ele[1]]+1) > len(l[min_ele[1]]):
			row_list[min_ele[1]] = -1
		
		print("After update row_list {} {} {}".format(row_list,len(l[min_ele[1]]),row_list[min_ele[1]])) if debug else None
		
	return op

print(merge([[1, 4, 7],[2, 5, 8],[3, 6, 9]]))

# (base) D:\>python int8a.py
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
		