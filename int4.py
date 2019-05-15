# Find Duplicates
# ● Question : Given an array of integers where each value 1 <= x <= len(array), write
# a function that finds all the duplicates in the array.
# ● Eg.
# dups([1, 2, 3]) = []
# dups([1, 2, 2]) = [2]
# dups([3, 3, 3]) = [3]
# dups([2, 1, 2, 1]) = [1, 2]


def find_dup(dups): # Time = O(N), Space = O(N)
	#print(dups)
	my_dict = dict()
	
	op = list()
	for e in dups:
		if e in my_dict.keys():
			if e not in op:
				op.append(e)
		else:
			my_dict[e] = 1
	return op


print(find_dup([1,2,3]))
print(find_dup([1,2,2]))
print(find_dup([3,3,3]))
print(find_dup([2,1,2,1]))


def find_dup1(dups): # Time = O(N), Space = O(1)
	op = list()
	for e in dups:
		#print(e)
		idx = abs(e)-1
		if dups[idx] < 0:
			if abs(e) not in op:
				op.append(abs(e))
		else:
			dups[idx] = -1 * dups[idx]
	return op
	
print(find_dup1([1,2,3]))
print(find_dup1([1,2,2]))
print(find_dup1([3,3,3]))
print(find_dup1([2,1,2,1]))
