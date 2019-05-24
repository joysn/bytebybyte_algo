# Merge Arrays
# Question : Given 2 sorted arrays, A and B, where A is long enough to hold the
# contents of A and B, write a function to copy the contents of B into A without
# using any buffer or additional memory.
	

def mergeArrays(a,b):
	
	print("Input {} and {}".format(a,b))
	aidx = len(a) - len(b) - 1
	bidx = len(b) - 1
	midx = len(a) - 1
	
	while aidx >= 0 and bidx >= 0:
		if a[aidx] > b[bidx]:
			a[midx] = a[aidx]
			aidx -= 1
		else:
			a[midx] = b[bidx]
			bidx -= 1
		midx -= 1
	
	while bidx >= 0:
		a[midx] = b[bidx]
		bidx -= 1
		midx -= 1
	return a
	
# A = [1,4,5,0,0,0]
# B = [2,3,6]
A = [1,3,5,0,0,0]
B = [2,4,6]
print("Output {}".format(mergeArrays(A, B)))
# A = {1,2,3,4,5,6}


A = [1,4,5,0,0,0]
B = [2,3,6]
print("Output {}".format(mergeArrays(A, B)))
# A = {1,2,3,4,5,6}


A = [1,2,3,0,0,0]
B = [4,5,6]
print("Output {}".format(mergeArrays(A, B)))
# A = {1,2,3,4,5,6}


A = [4,5,6,0,0,0]
B = [1,2,3]
print("Output {}".format(mergeArrays(A, B)))
# A = {1,2,3,4,5,6}


# (base) D:\>python int10.py
# Input [1, 3, 5, 0, 0, 0] and [2, 4, 6]
# Output [1, 2, 3, 4, 5, 6]
# Input [1, 4, 5, 0, 0, 0] and [2, 3, 6]
# Output [1, 2, 3, 4, 5, 6]
# Input [1, 2, 3, 0, 0, 0] and [4, 5, 6]
# Output [1, 2, 3, 4, 5, 6]
# Input [4, 5, 6, 0, 0, 0] and [1, 2, 3]
# Output [1, 2, 3, 4, 5, 6]

