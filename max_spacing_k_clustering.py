import numpy as np
import sys
import copy

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

def parent_find(parent, node):
	return parent[node]

def union(parent, node_1, node_2, members):
	(old_leader, new_leader) = (parent_find(parent, node_1), parent_find(parent, node_2))
	if old_leader == new_leader:
		return
	old_group = members.pop(old_leader)
	for node in old_group:
		parent[node] = new_leader
	members[new_leader].extend(old_group)

def max_spacing_clusters(mat, n):
	parent = {i: i for i in range(1, n + 1)}
	clusters = [i for i in range(1, n + 1)]
	members = {i: [i] for i in range(1, n + 1)}

	mat_ = copy.deepcopy(mat)
	# print(mat_)

	while len(members) > 4:

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

		union(parent, i, j, members)
		# print(members)

		# def find_spacing():
		# 	spacing_indices = []
		# 	for p in members:
		# 		for p_ in members:
		# 			if p == p_:
		# 				continue
		# 			spacing_indices.extend([(a, b) for a in members[p] for b in members[p_] if (b, a) not in spacing_indices])
		# 	return spacing_indices

		# spacing_indices = find_spacing()
		# print(len(members))
		# print(mat_[1, 12], mat_[12, 1])
		# break


	# return members

	def find_spacing():
			spacing_indices = []
			for p in members:
				for p_ in members:
					if p == p_:
						continue
					spacing_indices.extend([(a, b) for a in members[p] for b in members[p_] if (b, a) not in spacing_indices])
			return spacing_indices

	spacing_indices = find_spacing()

	min_spacing = min([mat[index[0], index[1]] for index in spacing_indices])
	return min_spacing


def main():
	filename = sys.argv[1]
	mat, n = make_graph(filename)
	print(max_spacing_clusters(mat, n))

if __name__ == '__main__':
	main()

