# 43. Three Sum
# ● Question: Given a list of integers, write a function that returns all sets of 3
# numbers in the list, a, b, and c, so that a + b + c == 0.
# threeSum({-1, 0, 1, 2, -1, -4})
# [-1, -1, 2]
# [-1, 0, 1]


def three_sum(sum,num_list,op_list):
	global final_op
	print("Called with",sum,num_list,op_list) if debug else None
	if sum == 0:
		if len(op_list) == 3:
			final_op += [op_list]
			return
		
	if len(num_list) == 0:
		return
		
	three_sum(sum-num_list[0],num_list[1:],op_list+[num_list[0]])
	three_sum(sum,num_list[1:],op_list)
			
	return
	
debug = False
#debug = True
global final_op
final_op = []
print("Sum of 2 for [1,0,1,-1,2]")
three_sum(2,[1,0,1,-1,2],[])
print(final_op)

final_op = []
print("Sum of 0 for [-1, 0, 1, 2, -1, -4]")
three_sum(0,[-1, 0, 1, 2, -1, -4],[])
print(final_op)
	
	
# (base) D:\tocopy>python algo43_three_sum.py
# Sum of 2 for [1,0,1,-1,2]
# [[1, 0, 1], [1, -1, 2], [1, -1, 2]]
# Sum of 0 for [-1, 0, 1, 2, -1, -4]
# [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]


def three_sum(num_list):
	
	