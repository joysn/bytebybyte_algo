# Given a boolean matrix, update it so that if any cell is true, all the cells
# in that row and column are true.
# ● Eg.
# [true, false, false]     [true, true, true ]
# [false, false, false] -> [true, false, false]
# [false, false, false]    [true, false, false]


def mod_mat(inp_mat): # T(O(N*M)), S = O(N*M)
	debug = False
	print(len(inp_mat)) if debug else None
	print(len(inp_mat[0])) if debug else None
	
	
	op_mat = [[[False] for i in range(len(inp_mat[0]))] for j in range(len(inp_mat))]
	print(inp_mat) if debug else None
	print(op_mat) if debug else None
	
	for i in range(len(inp_mat)): #0-3
		for j in range(len(inp_mat[0])): #0-2
			print(inp_mat[i][j]) if debug else None
			if inp_mat[i][j][0] is True:
				print(i,j) if debug else None
				for k in range(len(op_mat[0])):
					op_mat[i][k] = True
				for k in range(len(op_mat)):
					op_mat[k][j] = True
				i += 1
					
	print(op_mat)

inp_mat = [[[True],[False], [False]],[[False],[False],[False]],[[False],[False],[False]],[[False],[False],[False]]]
mod_mat(inp_mat)


# (base) D:\>python int6.py
# [[True, True, True], [True, [False], [False]], [True, [False], [False]], [True, [False], [False]]]

## Try to use the same input matrix, use an array to store all the trues of rows and columns
def mod_mat1(inp_mat): # T(O(N*M)), S = O(N+M)
	true_col = list()
	true_row = list()
	
	print(inp_mat)
	
	for row in range(len(inp_mat)):
		for col in range(len(inp_mat[0])):
			if inp_mat[row][col][0] is True:
				true_col.append(col)
				true_row.append(row)
				row += 1

	for row in true_row:
		for col in range(len(inp_mat[0])):
			inp_mat[row][col][0] = True
			
	for col in true_col:
		for row in range(len(inp_mat)):
			inp_mat[row][col][0] = True
	
	print(inp_mat)

print("************************************")
inp_mat = [[[True],[False], [False]],[[False],[False],[False]],[[False],[False],[False]],[[False],[False],[False]]]
mod_mat1(inp_mat)

# (base) D:\>python int6.py
# [[[True], [True], [True]], [[True], [False], [False]], [[True], [False], [False]], [[True], [False], [False]]]

## Type 3

def mod_mat2(inp_mat): # T(O(N*M)), S = O(1)
	zeroRowTrue = False
	zeroColTrue = False
	
	for i in range(len(inp_mat[0])):
		if inp_mat[0][i][0] is True:
			zeroRowTrue = True
			
	for i in range(len(inp_mat)):
		if inp_mat[i][0][0] is True:
			zeroColTrue = True
			
	for i in range(1,len(inp_mat)):
		for j in range(1,len(inp_mat[0])):
			if inp_mat[i][j][0] is True:
				inp_mat[0][j] = True
				inp_mat[i][0] = True
				
	for i in range(1,len(inp_mat)):
		for j in range(1,len(inp_mat[0])):
			if inp_mat[0][j][0] is True:
				inp_mat[i][j] = True
			if inp_mat[i][0][0] is True:
				inp_mat[i][j] = True
				
	if zeroRowTrue is True:
		for i in range(len(inp_mat[0])):
			inp_mat[0][i] = True
	
	if zeroColTrue is True:
		for i in range(len(inp_mat)):
			inp_mat[i][0] = True
	
	print(inp_mat)

print("************************************")
inp_mat = [[[True],[False], [False]],[[False],[False],[False]],[[False],[False],[False]],[[False],[False],[False]]]
mod_mat2(inp_mat)


# # (base) D:\>python int6.py
# # [[[True], [True], [True]], [[True], [False], [False]], [[True], [False], [False]], [[True], [False], [False]]]
