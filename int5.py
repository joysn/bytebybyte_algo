# Consecutive Array
# ● Question: Given an unsorted array, find the length of the longest sequence of
# consecutive numbers in the array.
# ● eg.
# consecutive([4, 2, 1, 6, 5]) = 3, [4, 5, 6]
# consecutive([5, 5, 3, 1]) = 1, [1], [3], or [5]


def consecutive(my_list):
	
	largest = 0
	my_dict = dict()
	
	largest_list = list()
	
	for e in my_list: #O(N)
		if e not in my_dict.keys():
			my_dict[e] = 1
	
	for e in my_list: #O(N)
		
		len = 1
		temp = list()
		temp.append(e)
		
		
		if e-1 in my_dict.keys(): # for all elements whose e-1 is present, we are going back
			while e-1 in my_dict.keys():
				len += 1
				temp.append(e-1)
				e = e-1 
		else:
			len = 1
		
		if largest < len:
			largest = len
			largest_list = temp
			
	return largest,largest_list
	

	
print(consecutive([4, 2, 1, 6, 5])) # 3, [4, 5, 6]
print(consecutive([5, 5, 3, 1])) # 1, [1], [3], or [5]

# (base) D:\>python int5.py
# (3, [6, 5, 4])
# (1, [5])



def consecutive1(my_list):
	
	largest = 0
	my_dict = dict()
	
	largest_list = list()
	
	for e in my_list: #O(N)
		if e not in my_dict.keys():
			my_dict[e] = 1
	
	for key in my_dict.keys(): #O(N)
		
		len = 1
		temp = list()
		temp.append(key)
		
		print(key)
		if key-1 not in my_dict.keys(): #Only if e-1 is not present we are moving forward, thus we will get linear time. . So we only traverse any given element at most twice﻿
			while key+1 in my_dict.keys():
				print("-->"+str(key+1))
				len += 1
				temp.append(key+1)
				key += 1 
		
		if largest < len:
			largest = len
			largest_list = temp
			
	return largest,largest_list
	

	
print(consecutive1([4, 2, 1, 6, 5])) # 3, [4, 5, 6]
print(consecutive1([5, 5, 3, 1])) # 1, [1], [3], or [5]



# (base) D:\>python int5.py
# 4
# -->5
# -->6
# 2
# 1
# -->2
# 6
# 5
# (3, [4, 5, 6])
# 5
# 3
# 1
# (1, [5])