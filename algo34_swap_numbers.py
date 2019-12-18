# 34. Swap Variables
# ● Question : Given two integers, write a function that swaps them without using
# any temporary variables.


def swap(n1, n2):
	print("before Swap:",n1,n2)
	n1 = n1 + n2
	print(n1) if debug else None
	n2 = n1 - n2
	print(n2) if debug else None
	n1 = n1 - n2
	print("After Swap:",n1,n2)
	
debug = False
swap(3,2)
swap(1,2)
swap(10,1)
swap(3.1,2.1)
swap(-3.1,-2.1)

# (base) D:\>python algo34_swap_numbers.py
# before Swap: 3 2
# After Swap: 2 3
# before Swap: 1 2
# After Swap: 2 1
# before Swap: 10 1
# After Swap: 1 10
# before Swap: 3.1 2.1
# After Swap: 2.1 3.1
# before Swap: -3.1 -2.1
# After Swap: -2.1 -3.1
	
	

