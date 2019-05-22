# Merge K Arrays
# ● Question : Given k sorted arrays, merge them into a single sorted array.
# ● Eg.
# merge({{1, 4, 7},{2, 5, 8},{3, 6, 9}}) = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def merge(l): #T (k*nlog(k*n)), S(O(k*n))
	opl = list()
	debug = False
	for i in range(len(l)):
		opl += l[i]
		
	print(opl) if debug else None
	opl = sorted(opl)
	return (opl)


print(merge([[1, 4, 7],[2, 5, 8],[3, 6, 9]]))

# (base) D:\>python int8.py
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


def merge(l): #T (k*nlog(k*n)), S(O(1))
	debug = False
	for i in range(1,len(l)):
		l[0] += l[i]
		
	print(opl) if debug else None
	l[0] = sorted(l[0])
	return (l[0])


print(merge([[1, 4, 7],[2, 5, 8],[3, 6, 9]]))

# (base) D:\>python int8.py
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


