# Median of Arrays
# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]
# median(arr1, arr2) = 3.5

# final array 1,2,3,4,5,6 - take the middle one and since it is even in number, we find the average

debug = False
def cal_median(a1,a2):
	final_a = a1+ a2
	print(final_a) if debug else None
	final_a = sorted(final_a) #O((a+b)log(a+b))
	print(final_a) if debug else None
	l = len(final_a)
	if len(final_a)%2 != 0:
		return final_a[int((l+1)/2)-1]
	else:
		m = int((l+1)/2)
		return (final_a[m-1]+final_a[m])/2
	
	
print(cal_median([1,3,5],[2,4,6])) #O((a+b)log(a+b))
print(cal_median([1,3,5],[2,4,6,7]))
print(cal_median([1,3,5],[]))
print(cal_median([1,3],[]))
print("***********************")
# (base) D:\>python int1.py
# 3.5
# 4
# 3
# 2.0

## ***********
## Enhancement
## ***********

debug = False
def cal_median(a1,a2):
	
	j = 0
	k = 0
	final_a = []
	l1 = len(a1)
	l2 = len(a2)
	print(l1,l2) if debug else None
	for i in range(0,l1+l2): #O(n+m)
		print(i,j,k) if debug else None
		if j < l1 and k < l2:
			if a1[j] < a2[k]:
				final_a.append(a1[j])
				j += 1
			else:
				final_a.append(a2[k])
				k += 1
	print(j,k,l1,l2) if debug else None
	while j < l1:
		final_a.append(a1[j])
		j += 1
	while k < l2:
		final_a.append(a2[k])
		k += 1
		
	#final_a = a1+ a2
	print(final_a) if debug else None
	l = l1+l2
	if len(final_a)%2 != 0:
		return final_a[int((l+1)/2)-1]
	else:
		m = int((l+1)/2)
		return (final_a[m-1]+final_a[m])/2
	
	
print(cal_median([1,3,5],[2,4,6])) #O(n+m)
print(cal_median([1,3,5],[2,4,6,7]))
print(cal_median([1,3,5],[]))
print(cal_median([1,3],[]))
print("***********************")

# O(log(min(n, m))), where n and m are the sizes of given sorted array


# Python code for median with   
# case of returning double 
# value when even number  
# of elements are present 
# in both array combinely 
median = 0
i = 0 
j = 0
   
# def to find max 
def maximum(a, b) : 
    return a if a > b else b 
   
# def to find minimum 
def minimum(a, b) : 
    return a if a < b else b 
   
# def to find median 
# of two sorted arrays 
def findMedianSortedArrays(a, n, b, m) : 
  
    global median, i, j 
    min_index = 0 
    max_index = n  
       
    while (min_index <= max_index) : 
      
        i = int((min_index + max_index) / 2) 
        j = int(((n + m + 1) / 2) - i) 
       
        # if i = n, it means that Elements from a[] in the 
        # second half is an empty set. and if j = 0, it  
        # means that Elements from  b[] in the first half is  
        # an empty set. so it is  necessary to check that,  
        # because we compare elements  from these two groups. Searching on right 
        if (i < n and j > 0 and b[j - 1] > a[i]) : 
            min_index = i + 1
                   
        # if i = 0, it means that Elements from a[] in the 
        # first half is an empty set and if j = m, it means 
        # that Elements from b[] in  the second half is an empty  
        # set. so it is necessary to check that, because we compare  
        # elements from these two groups. searching on left 
        elif (i > 0 and j < m and b[j] < a[i - 1]) : 
            max_index = i - 1
           
        # we have found the desired halves. 
        else : 
          
            # this condition happens when we don't have any elements  
            # in the first half from a[]  so we returning the last 
            # element in b[] from the  first half. 
            if (i == 0) : 
                median = b[j - 1] 
                   
            # and this condition happens when we don't have any  
            # elements in the first half from b[] so we returning the  
            # last element in a[] from the first half. 
            elif (j == 0) : 
                median = a[i - 1]          
            else : 
                median = maximum(a[i - 1], b[j - 1])  
            break
          
      
       
    # calculating the median. If number of elements  is odd there is  one middle element.   
    if ((n + m) % 2 == 1) : 
        return median 
   
    # Elements from a[] in the  second half is an empty set.  
    if (i == n) : 
        return ((median + b[j]) / 2.0) 
   
    # Elements from b[] in the  second half is an empty set. 
    if (j == m) : 
        return ((median + a[i]) / 2.0) 
       
    return ((median + minimum(a[i], b[j])) / 2.0) 
  
   
print(findMedianSortedArrays([1,3,5],3,[2,4,6],3)) #O(log(min(n,m)))
print(findMedianSortedArrays([1,3,5],3,[2,4,6,7],4))
print(findMedianSortedArrays([],0,[1,3,5],3))
print(findMedianSortedArrays([],0,[1,3],2))
print("***********************")