# 11. Zero Sum Subarray
# Question: Given an array, write a function to find any subarray that sums to zero, if one exists.

#zeroSum({1, 2, -5, 1, 2, -1}) = [2, -5, 1, 2]


def zeroSum(a,sum):	
	cache =[[0 for i in range(len(a)+1)] for j in range(len(a)+1)]
	
	# print(len(a))
	# print(len(cache))
	# print(len(cache[0]))
	cache[0][0] = 0
	
	for col in range(1,len(cache[0])):
		cache[0][col] = a[col-1]
		cache[col][0] = a[col-1]
		
	for row in range(1,len(cache)-1):
		cache[row][row+1] = cache[0][row+1] + cache[row][0]
		op = list()
		op.append(cache[row][0])
		op.append(cache[0][row+1])
		if cache[row][row+1] == 0:
			return op
		for col in range(row+2,len(cache)):
			cache[row][col] = cache[0][col] + cache[row][col-1]
			op.append(cache[0][col])
			if cache[row][col] == 0:
				return op
		
	# for row in range(len(cache)):
		# for col in range(len(cache[0])):
			# print(cache[row][col], end="|")
		# print("\n")
	return []
	

print("1,2,-3 Should be same {}".format(zeroSum([1, 2, -3],0)))
print("[1] Should be None {}".format(zeroSum([1],0)))
print("[1,-1] Should be same {}".format(zeroSum([1,-1],0)))
print("[1,-2] Should be None {}".format(zeroSum([1,-2],0)))
print(zeroSum([1, 2, -5, 1, 2, -1],0))
print(zeroSum([1, 2, -5, 1, 2, -6],0))

# (base) D:\>python int11.py
# 1,2,-3 Should be same [1, 2, -3]
# [1] Should be None []
# [1,-1] Should be same [1, -1]
# [1,-2] Should be None []
# [1, 2, -5, 1, 2, -1]
# [2, -5, 1, 2]