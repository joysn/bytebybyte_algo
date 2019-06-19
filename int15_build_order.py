# 15. Build Order
# Question : Given a list of packages that need to be built and the dependencies for each package, determine a valid order in which to build the packages.



def build_order(package_arr):

	debug = False
	op_list = list()
	print("Input array:",package_arr) if debug else None
	
	permMarks = list()
	tempMarks = list()
	
	#print(len(package_arr))
	for i in range(len(package_arr)):
		if i not in permMarks:
			print("not in PermMark:",i) if debug else None
			visit(i,package_arr,permMarks,tempMarks,op_list)		
	return op_list
	
	
def visit(i,package_arr,permMarks,tempMarks,op_list):
	if i in tempMarks:
		print("Contains Cycle")
		exit()
	
	if i not in permMarks:
		tempMarks.append(i)
		for j in package_arr[i]:
			visit(j,package_arr,permMarks,tempMarks,op_list)
			
		permMarks.append(i)
		tempMarks.remove(i)
		op_list.append(i)

package_arr = [[],[0],[0],[1,2],[3]]
print(build_order(package_arr))
#output: 0, 1, 2, 3, 4


package_arr = [[],[2],[0],[1,2],[3]]
print(build_order(package_arr))
# [0, 2, 1, 3, 4]


package_arr = [[],[2],[1],[1,2],[3]]
print(build_order(package_arr))
# Contains Cycle

