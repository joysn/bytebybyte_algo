# 16. Shortest Path
# Question: Given a directed graph, find the shortest path between two nodes if
# one exists.
# shortestPath(2, 3) = 2 -> 5 -> 4 -> 3

class Node:
	
	def __init__(self, data=None, children= None):
		self.data = data
		self.children = list()
		
	def set_data(self, data):
		self.data = data
		
	def add_children(self, n):
		if n.data is not None:
			self.children.append(n)
		
		
		
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.add_children(n2)
n1.add_children(n3)
n2.add_children(n5)
n5.add_children(n4)
n4.add_children(n1)
n4.add_children(n3)

def findShortestPath(nsrc,ndest):

	debug = False
	toVisit = list()
	path = list()
	parentList = dict()
	
	if nsrc is None or ndest is None:
		print("No path")
		return
		
	if nsrc.data == ndest.data:
		print("No path")
		return path
		
	parentList[nsrc] = Node(-1)
	toVisit.append(nsrc)
	while len(toVisit) != 0:
		curr = toVisit.pop(0)
		if curr.data == ndest.data:
			break
			
		if curr.children == None:
			continue
			
		for ch in curr.children:
			if ch not in parentList.keys():
				parentList[ch] = curr
				#parentList.append([ch,curr])
				toVisit.append(ch)

	for k in parentList.keys():
		print(k.data,parentList[k].data) if debug else None

	if parentList[k] == None:
		print("No path")
		return path
		
	n = ndest
	while(n.data != -1):
		print(n.data,end='->') if debug else None
		path.append(n.data)
		n = parentList[n]
		
	path.reverse()
	print(path)
	
findShortestPath(n2,n3)	