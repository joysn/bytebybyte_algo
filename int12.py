# 12. Permutations
# Question : Write a function that returns all permutations of a given list.

def permutations(a):

	debug = False
	print("In permuations {}".format(a)) if debug else None
	if len(a) == 0:
		return []
	if len(a) == 1:
		return [a]
	else:
		op = list()
		for i in range(len(a)):
			if i == 0:
				b = a[1:]
			elif i == len(a) - 1:
				b = a[:-1]
			else:
				b = a[:i]+a[i+1:]
			print("My a {} i is {} new b is {} + {} = {}".format(a,i,a[:i],a[i+1:], b))  if debug else None
			sub_op = permutations(b)
			for e in sub_op:
				op_temp = list()
				op_temp.append(a[i])
				op_temp += e
				
				op.append(op_temp)
			
		return op


print(permutations([1, 2, 3]))
print(permutations([1, 2]))
print(permutations([1]))
print(permutations([2,1]))
print(permutations([1,2,3,4]))


# (base) D:\>python int12.py
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# [[1, 2], [2, 1]]
# [[1]]
# [[2, 1], [1, 2]]
# [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]