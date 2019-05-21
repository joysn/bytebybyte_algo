# Question: Given a 2D array of 1s and 0s, find the largest square subarray of all
# 1s.
def find_larg_square(mat):

	debug = False
	print("Original Matrix {}".format(mat) )
	
	print(len(mat)) if debug else None
	print(len(mat[0])) if debug else None
	
	largest = 0
	for i in range(1,len(mat)): # rows
		for j in range(1,len(mat[0])): # cols
			if mat[i][j] == 1:
				mat[i][j] += min(mat[i-1][j-1], mat[i-1][j],mat[i][j-1])
				if largest < mat[i][j]:
					largest = mat[i][j]
				
	print("Modified Matrix {}".format(mat) )
	print("Size of largest Squeare Matrix {}".format(largest))
			


mat = \
[[0, 0, 0, 0],
 [0, 1, 1, 1],
 [0, 1, 1, 1],
 [0, 0, 1, 1]
]

find_larg_square(mat)

mat = \
[[0, 0, 0, 0],
 [0, 1, 1, 1],
 [0, 1, 1, 1],
 [0, 1, 1, 1]
]
find_larg_square(mat)


mat = \
[[1, 1, 1, 0],
 [1, 1, 1, 1],
 [1, 1, 1, 1],
 [0, 1, 1, 1]
]
find_larg_square(mat)


# (base) D:\>python int7.py
# Original Matrix [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1]]
# Modified Matrix [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 0, 1, 2]]
# Size of largest Squeare Matrix 2
# Original Matrix [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
# Modified Matrix [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3]]
# Size of largest Squeare Matrix 3
# Original Matrix [[1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
# Modified Matrix [[1, 1, 1, 0], [1, 2, 2, 1], [1, 2, 3, 2], [0, 1, 2, 3]]
# Size of largest Squeare Matrix 3

