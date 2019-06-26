# 19. Sum
# ● Question: Given two integers, write a function to sum the numbers without using
# any arithmetic operators.

def sumint(a,b):
	debug = False
	print(a,b) if debug else None
	if b == 0:
		return a
	partSum = a ^ b
	print(partSum) if debug else None
	carry = (a & b) << 1
	return sumint(partSum,carry)
	
	
print("Sum of 1 & 2 is:",sumint(1,2))
print("Sum of 10 & 10 is:",sumint(10,10))