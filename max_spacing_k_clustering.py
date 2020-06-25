from collections import defaultdict
from itertools import combinations
import numpy as np
import sys
import copy
import itertools

def make_graph(filename):
	n = 0
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip('\n').split(' ')
			if len(line) == 1:
				n = int(line[0])
				break

		mat = np.full((n+1, n+1), 999999, dtype = 'int32')

		for line in f:
			line = line.strip('\n').split(' ')
			if len(line) == 1:
				continue
			mat[int(line[0]), int(line[1])] = int(line[2])
			mat[int(line[1]), int(line[0])] = int(line[2])

	return mat, n

def make_graph_big(filename):
	# nodes = {node number: binary to decimal representation of node string}
	nodes = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines[1:]:
			x = line.strip('\n').split(' ')
			x = ''.join(x)
			node = int(x, 2)
			nodes.append(node)
	return nodes

	# no_of_nodes, no_of_bits_label = 0, 0
	# nodes = {}
	# with open(filename, 'r') as f:
	# 	for line in f:
	# 		line = line.strip('\n').split(' ')
	# 		if len(line) == 2:
	# 			no_of_nodes, no_of_bits_label = int(line[0]), int(line[1])
	# 		else:
	# 			nodes.append(''.join(line))

	# return no_of_nodes, no_of_bits_label, nodes

#hamming1 and hamming2 from https://github.com/anmourchen/algorithms/blob/master/Greedy_Algorithms_Minimum_Spanning_Trees_and_Dynamic_Programming/Assignment2/hamming.py
def hamming1(num):
    """ return the list of numbers with 1 bit difference from num """
    masks = [1 << i for i in range(num.bit_length())]
    code = [num ^ mask for mask in masks]
    return code


def hamming2(num):
    """ return the list of numbers with 2 bit difference from num """
    masks = [(1 << i) ^ (1 << j) for (i, j) in combinations(range(num.bit_length()), 2)]
    code = [num ^ mask for mask in masks]
    return code

# def hamming_distance(node_1, node_2, no_of_bits_label):
# 	for i in range(no_of_bits_label):
# 		if node_1[i] == node_2[i]:
# 			hd += 1

# 	return hd

# def complement(pos):
# 	if pos == '1':
# 		return '0'
# 	return '1'

# def neighbors_of_node(node, distance):
# 	indices = itertools.combinations(range(len(node)), distance)
# 	neighbors = []
# 	for tup in indices:
# 		nbr = copy.deepcopy(node)
# 		for index in tup:
# 			nbr = list(nbr)
# 			nbr[index] = complement(node[index])
# 			nbr = ''.join(nbr)
# 		neighbors.append(nbr)

# 	return neighbors

def largest_k_minimum_spacing(nodes):
	parent = {node: node for node in nodes}
	union_members = {node: [node] for node in nodes}
	for node in nodes:
		print(len(union_members))
		for code in hamming1(node):
			try:
				union(parent, node, code, union_members)
			except:
				pass

		for code in hamming2(node):
			try:
				union(parent, node, code, union_members)
			except:
				pass

	return len(union_members)

def matrix_using_nodes(nodes, no_of_nodes, no_of_bits_label):
	mat = np.full((no_of_nodes + 1, no_of_nodes + 1), 999999, dtype = 'int32')
	for i in range(1, no_of_nodes):
		for j in range(i + 1, no_of_nodes):
			hd = hamming_distance(nodes[i], nodes[j], no_of_bits_label)
			mat[i, j] = hd
			mat[j, i] = hd
			print(mat)

	return mat

def parent_find(parent, node):
	return parent[node]

def union(parent, node_1, node_2, union_members):
	(old_leader, new_leader) = (parent_find(parent, node_1), parent_find(parent, node_2))
	if old_leader == new_leader:
		return
	old_group = union_members.pop(old_leader)
	for node in old_group:
		parent[node] = new_leader
	union_members[new_leader].extend(old_group)

def max_spacing_clusters(mat, n):
	parent = {i: i for i in range(1, n + 1)}
	# clusters = [i for i in range(1, n + 1)]
	union_members = {i: [i] for i in range(1, n + 1)}

	mat_ = copy.deepcopy(mat)
	# print(mat_)

	while len(union_members) > 4:

		def find_closest_nodes():
			# print(np.min(mat_[np.nonzero(mat_)]), '###')
			# print(np.argmin(mat_))
			index = np.where(mat_ == np.amin(mat_))
			# print(index)
			# min_edge = np.min(mat_[np.nonzero(mat_)])
			# index = np.where(mat_ == min_edge)[0]
			i = index[0][0]
			j = index[1][0]
			return (i, j)

		i, j = find_closest_nodes()
		# print(i, j)
		# print(mat[i, j], mat[j, i])
		# print(mat[1, 348])

		mat_[i, j] = 999999
		mat_[j, i] = 999999

		union(parent, i, j, union_members)
		# print(union_members)

		# def find_spacing():
		# 	spacing_indices = []
		# 	for p in union_members:
		# 		for p_ in union_members:
		# 			if p == p_:
		# 				continue
		# 			spacing_indices.extend([(a, b) for a in union_members[p] for b in union_members[p_] if (b, a) not in spacing_indices])
		# 	return spacing_indices

		# spacing_indices = find_spacing()
		# print(len(union_members))
		# print(mat_[1, 12], mat_[12, 1])
		# break


	# return union_members

	def find_spacing():
			spacing_indices = []
			for p in union_members:
				for p_ in union_members:
					if p == p_:
						continue
					spacing_indices.extend([(a, b) for a in union_members[p] for b in union_members[p_] if (b, a) not in spacing_indices])
			return spacing_indices

	spacing_indices = find_spacing()

	min_spacing = min([mat[index[0], index[1]] for index in spacing_indices])
	return min_spacing

def main():
	filename = sys.argv[1]
	# mat, n = make_graph(filename)
	# print(max_spacing_clusters(mat, n))
	nodes = make_graph_big(filename)
	# print(nodes)
	# mat = matrix_using_nodes(nodes, no_of_nodes, no_of_bits_label)
	# print(mat)
	print(largest_k_minimum_spacing(nodes))

if __name__ == '__main__':
	main()

