# Matrix Search
# Question : Given an n x m array where all rows and columns are in sorted order,
# write a function to determine whether the array contains an element x.

def contains(mat, x):
	
	debug = True
	cnt = 0
	for row in range(len(mat)):
		cnt += 1
		if mat[row][0] == x:
			print("Time Complexity1: {}".format(cnt)) if debug else None
			return True
		if mat[row][0] > x: # row-1 has x
			for col in range(len(mat[0])):
				cnt += 1
				if mat[row-1][col] == x:
					print("Time Complexity2: {}".format(cnt)) if debug else None
					return True
			print("Time Complexity4: {}".format(cnt)) if debug else None
			return False
	print("Time Complexity3: {}".format(cnt)) if debug else None
	return False

mat = [[1, 2, 3, 4],[5, 7, 8, 9],[9, 10, 11, 12]]
print(contains(mat,1.5))
print(contains(mat,6))
print(contains(mat,8))
print(contains(mat,5))


# (base) D:\>python int9.py
# Time Complexity4: 6
# False
# Time Complexity4: 7
# False
# Time Complexity2: 6
# True
# Time Complexity1: 2
# True