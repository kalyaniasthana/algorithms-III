import sys
sys.path.insert(0, '../algorithms-II')

class Node:
	def __init__(self, label, left_child = None, right_child = None, parent = None):
		self.label = label
		# self.parent = parent
		self.left_child = left_child
		self.right_child = right_child
		self.parent = parent
		# self.left_edge = None
		# self.right_edge = None

	def add_child(self, child):
		if self.left_child is None:
			self.left_child = child
		elif self.right_child is None:
			self.right_child = child
		else:
			return

	def add_parent(self, parent):
		self.parent = parent

	def __str__(self):
		return 'Node: {}, Left Child: {}, Right Child: {}'.format(self.label, self.right_child.label, self.left_child.label)

#finding height of a tree/subtree starting at Node = node using recursion
def max_depth(node):
	if node is None:
		return 0
	left_subtree_height = max_depth(node.left_child)
	right_subtree_height = max_depth(node.right_child)

	if left_subtree_height > right_subtree_height:
		return left_subtree_height + 1
	else:
		return right_subtree_height + 1

def dfs_paths(nodes):
	leaf_nodes = find_leaf_nodes(nodes)
	all_path_lengths = []
	for node in leaf_nodes:
		current_node = node
		path = [current_node.label]
		while True:
			if current_node.parent is None:
				break
			path.append(current_node.parent)
			current_node = current_node.parent

		all_path_lengths.append(len(path))

	return list(set(all_path_lengths))

def read_codes(filename):
	no_of_symbols = 0
	weights = []
	with open(filename) as f:
		lines = f.readlines()
		no_of_symbols = int(lines[0].strip('\n'))
		for line in lines[1:]:
			weights.append(int(line.strip('\n')))

	return no_of_symbols, weights

# 1. Build a huffman tree from the input characters
# 2. Assign binary codes to characters by traversing the huffman tree

def build_subtree(no_of_nodes, nodes):
	nodes.sort()
	smallest_1, smallest_2 = Node(nodes[0]), Node(nodes[1])
	new_node = Node(nodes[0] + nodes[1], smallest_1, smallest_2)
	return new_node, nodes

def build_entire_tree(no_of_nodes, nodes):
	nodes_ = []
	for node in nodes:
		nodes_.append(Node(node))

	_nodes = []

	while True:
		nodes_ = sorted(nodes_, key = lambda x: x.label)
		smallest_1  = nodes_.pop(0)
		smallest_2 = nodes_.pop(0)
		new_node = Node(smallest_1.label + smallest_2.label, smallest_1, smallest_2)
		smallest_1.add_parent(new_node)
		smallest_2.add_parent(new_node)
		nodes_.append(new_node)
		_nodes.append(smallest_1)
		_nodes.append(smallest_2)
		if len(nodes_) == 1:
			new_node = nodes_[0]
			smallest_1.add_parent(new_node)
			smallest_2.add_parent(new_node)
			_nodes.append(new_node)
			break
		# print([node.label for node in nodes_], 'nodes_ popping')
		# print([node.label for node in _nodes], '_nodes appending')

	max_length = max_depth(find_root(_nodes)) - 1 #length of path is no. of nodes in path - 1
	min_length = min(dfs_paths(_nodes)) - 1
	return max_length, min_length

def find_root(nodes):
	for node in nodes:
		if node.parent is None:
			return node

def find_leaf_nodes(nodes):
	leaf_nodes = []
	for node in nodes:
		if node.left_child is None and node.right_child is None:
			leaf_nodes.append(node)
	return leaf_nodes

def main():
	filename = sys.argv[1]
	no_of_nodes, nodes = read_codes(filename)
	print(build_entire_tree(no_of_nodes, nodes))

if __name__ == '__main__':
	main()