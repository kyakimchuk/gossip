#!/usr/bin/python3

import sys
import random

N = int(sys.argv[2])
C = int(sys.argv[4])
#improving initial algorithm by increasing X
X = 5

def generate_x_random_nodes(node):
	other_nodes = list(range(N))
	other_nodes.remove(node)
	result=[]
	for i in range(X):
		rand_node = random.choice(other_nodes)
		result.append(rand_node)
		other_nodes.remove(rand_node)
	return result

count_all_recived = 0
for j in range(C):
	nodes_states = [False for i in range(N)]
	start = random.randint(0, N-1)
	nodes_states[start] = True
	nodes = [start]
	count_cycles = 1
	while True:
		temp = []
		for node in nodes:
			x_random_nodes = generate_x_random_nodes(node)
			for i in x_random_nodes:
				if not nodes_states[i]:
					nodes_states[i] = True
					temp.append(i)
		count_cycles += 1
		nodes = temp
		if not temp or all(nodes_states):
			break

	if all(nodes_states):
		count_all_recived += 1
print('In ' + str(count_all_recived/10) + '% cases all nodes recieved the packet')
