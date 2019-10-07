
## Few assumptions for the algorithms
## 1. for any source s in V, there neccesarily exists a path
##    if no path exists the shortest distance is set to 1000000
## 2. All the paths have non negative weights

NO_PATH = 10**6

import sys

filname = sys.argv[1]

fh = open(filname, "r")

# g is the actual graph
g = {}

#w is the weight of each path
w = {}

#reading all the weights and nodes from the input testcase file
for i in fh.readlines():
	k = i.split()
	#print(i)
	#print(k[0])
	g[int(k[0])] = []
	w[int(k[0])] = []
	#print(k[0])
	o = k[1:len(k)]
	#print(o)
	for j in range(0, len(o)):
		_k = o[j].split(",")
		#print(_k)
		g[int(k[0])].append(int(_k[0]))
		w[int(k[0])].append(int(_k[1]))

'''
for k,v in w.items():
	print(k,g[k],v)
'''

## we are choosing the source vertex as 1
## and will be measuring the shortest distance
## from 1 to each vertex

s = 1

## the distance of the following vertices are needed
## to pass the assignment

test = [7,37,59,82,99,115,133,165,188,197]

## you can change s and test to find the shortest distance from any
## vertex to any other vertex

number_of_vertices = 200
vertices_processed_so_far = []

## number_of_vertices + 1, to apply 1 based indexing
## smallest distace
d = [NO_PATH] * (number_of_vertices + 1)
d[s] = 0

## A utility function to find out the minimun distance
## for all the vertices which haven't been processed so far

def mindist(vertices_processed_so_far, d):
	m = sys.maxint
	mind = 0
	for j in range(1,number_of_vertices):
		if d[j] < m and j not in vertices_processed_so_far:
			m = d[j]
			mind = j
	return mind

## Main loop which follows the Dijkstra's algorithm

while vertices_processed_so_far != g.keys():
	if s not in vertices_processed_so_far:
		vertices_processed_so_far.append(s)
		#print(g[s])
		for i in range(len(g[s])):
			if g[s][i] not in vertices_processed_so_far and d[g[s][i]] > d[s] + w[s][i]:
				d[g[s][i]] = d[s] + w[s][i]
				#print(w[s][i])
		s = mindist(vertices_processed_so_far, d)
		
		if s == 0:
			#print("0 ind")
			#print(vertices_processed_so_far)
			break

_t = []
for i in test:
	_t.append(d[i])

print(",".join(map(str, _t)))
