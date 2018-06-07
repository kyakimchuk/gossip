#!/usr/bin/python3

import sys
from random import choice, randint

N = int(sys.argv[2])
C = int(sys.argv[4])

def run_gossip_alg(N):
	def gossip_alg(node):
		nodes_states[node] = True
		for i in nodes_states:
			if not i: 
				break
		else:
			return
		other_nodes = nodes_names[:node]+nodes_names[node+1:]
		rand1 = choice(other_nodes)
		if not nodes_states[rand1]:
			gossip_alg(rand1)
		rand2 = choice(other_nodes)
		if not nodes_states[rand2]:
			gossip_alg(rand2)
		rand3 = choice(other_nodes)
		if not nodes_states[rand3]:
			gossip_alg(rand3)
		rand4 = choice(other_nodes)
		if not nodes_states[rand4]:
			gossip_alg(rand4)
		#improving initial algorithm by increasing X
		rand5 = choice(other_nodes)
		if not nodes_states[rand5]:
			gossip_alg(rand5)

	X = 5
	nodes_states = [False for i in range(N)]
	nodes_names = [i for i in range(N)]
	start = randint(0, N-1)
	gossip_alg(start)
	for i in nodes_states:
			if not i: 
				#not all nodes recieved packages
				return False
	else:
		#all nodes recieved packages
		return True

count = 0
for j in range(C):
	if run_gossip_alg(N):
		count += 1
print('In ' + str(count/10) + '% cases all nodes recieved the packet')
