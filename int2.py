# Question : Given a matrix, find the path from top left to bottom right with the
# greatest product by moving only down and right.
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# 1 > 4 > 7 > 8 > 9
# 2016

# Only for positive numbers
def max_product(x,y):
	result = 1
	#print(x,y)
	if x == x_max and y == y_max:
		return input[x][y]
	elif cache[x][y]:
		return cache[x][y]
	elif x < x_max and y < y_max:
		prod1 = input[x][y]*max_product(x+1,y)
		prod2 = input[x][y]*max_product(x,y+1)
		if prod1 > prod2:
			result = prod1
		else:
			result = prod2
	elif x < x_max:
		result = input[x][y]*max_product(x+1,y)
	else:
		result = input[x][y]*max_product(x,y+1)
			
	cache[x][y] = result
	return result
		

input = [[1,2,3],[4,5,6],[7,8,9]]
x_max = len(input[0]) - 1
y_max = len(input) - 1
cache = [[0 for i in range(len(input[0]))] for j in range(len(input))]
print(max_product(0,0))

# (base) D:\>python int2.py
# 2016

# How to make it work for -ve numbers. It is not a dynamic programing problem
# [-1, 2, 3]
# [4, 5, -6]
# [7, 8, -9]
# -1 > 4 > 5 > -6 > 9
# 1080

def prod_matrix():
	for y in range(y_max):
		for x in range(x_max):
			if x == 0 and y == 0:
				cache[x][y].append(input[x][y])
			elif y == 0:
				cache[x][y].append(cache[x-1][y][0] * input[x][y])
			elif x == 0:
				cache[x][y].append(cache[x][y-1][0] * input[x][y])
			else:
				for e in cache[x-1][y]:
					cache[x][y].append(e * input[x][y])
				for e in cache[x][y-1]:
					cache[x][y].append(e * input[x][y])
	return 1


input = [[1,2,3],[4,5,6],[7,8,9]]
x_max = len(input[0])
y_max = len(input)
cache = [[[] for i in range(len(input[0]))] for j in range(len(input))]
prod_matrix()
print(sorted(cache[-1][-1])[-1])

input = [[-1,2,3],[4,5,-6],[7,8,9]]
x_max = len(input[0])
y_max = len(input)
cache = [[[] for i in range(len(input[0]))] for j in range(len(input))]
prod_matrix()
print(sorted(cache[-1][-1])[-1])


# (base) D:\>python int2.py
# 2016
# 1080