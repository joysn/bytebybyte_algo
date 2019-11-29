# 32. Two Missing Numbers
# ● Question : Given an array containing all the numbers from 1 to n except two, find
# the two missing numbers.
# ● Eg.
# missing([4, 2, 3]) = 1, 5


def missing(arr,n):
	missList = set()
	wholeList = set()
	giveList = set()
	for i in range(1,n+1):
		wholeList.add(i)
	giveList = set(arr)
	missList = wholeList - giveList
	return missList
	
	
arr = [4,1,3]
print(missing(arr,5))


def missing2(arr,n):
	missList = list()
	wholeArray = list()
	
	for i in range(1,n+1):
		missList.append(i)
		
	for i in range(len(arr)):
		missList.remove(arr[i])
		
	return missList
	
arr = [4,1,3]
print(missing2(arr,5))



def missing3(arr,n):
	totalSum = n*(n+1)/2
	arrSum = 0
	
	for ele in arr:
		arrSum += ele
		
	print(totalSum,arrSum) if debug else None
	pivot = int((totalSum - arrSum)/2)
	print("Pivot is:",pivot) if debug else None
	
	totalXorLeft = 0
	totalXorRight = 0
	for i in range(1,pivot+1):
		totalXorLeft ^= i
		
	for i in range(pivot+1,n+1):
		totalXorRight ^= i
	print(totalXorLeft,totalXorRight) if debug else None
	
	arrXorLeft = 0
	arrXorRight = 0
	for ele in arr:
		if ele <= pivot:
			arrXorLeft ^= ele
		else:
			arrXorRight ^= ele
	print(arrXorLeft,arrXorRight) if debug else None
	
	return([totalXorLeft ^ arrXorLeft, totalXorRight ^ arrXorRight])
	
debug = False
arr = [4,1,3]
print(missing3(arr,5))
