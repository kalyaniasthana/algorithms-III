import sys

#classes from https://runestone.academy/runestone/books/published/pythonds/Graphs/Implementation.html
class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = {}

    def add_neighbor(self, nbr, weight = 0):
        self.neighbors[nbr] = weight
 
    def __str__(self):
        return 'Node: ' + str(self.id) + ' Neighbors: ' + str([x.id for x in self.neighbors])

    def get_connections(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.neighbors[nbr]

    def is_neighbor(self, node):
    	if node in self.neighbors:
    		return True
    	return False

class Graph:
    def __init__(self):
        self.node_list = {}
        self.num_of_nodes = 0

    def add_node(self, id):
        self.num_of_nodes = self.num_of_nodes + 1
        new_node = Node(id)
        self.node_list[id] = new_node
        return new_node

    def get_node(self, n):
        if n in self.node_list:
            return self.node_list[n]
        else:
            return None

    # def __contains__(self,n):
        # return n in self.node_list

    def add_edge(self, f, t, weight = 0):
        if f not in self.node_list:
            nv = self.add_node(f)
        if t not in self.node_list:
            nv = self.add_node(t)
        self.node_list[t].add_neighbor(self.node_list[f], weight)
        self.node_list[f].add_neighbor(self.node_list[t], weight)

    def __str__(self):
    	return 'Nodes: {}'.format(self.node_list.keys())

    def get_nodes(self):
        return self.node_list.keys()

    # def __iter__(self):
        # return iter(self.node_list.values())


def make_graph(filename):
	G = Graph()
	with open(filename) as f:
		for line in f:
			line = line.strip('\n').split(' ')
			if len(line) == 2:
				no_of_nodes, no_of_edges = int(line[0]), int(line[1])
				break
		for i in range(1, no_of_nodes + 1):
			G.add_node(i)
		for line in f:
			line = line.strip('\n').split(' ')
			if line == 2:
				continue
			# print(int(line[0]), int(line[1]), int(line[2]))
			G.add_edge(int(line[0]), int(line[1]), int(line[2]))
		# sys.exit()

	return G

# U: Nodes which have been visited
# V-U: Nodes which haven't been visited yet
def prims_algorithm(G):
	cost, not_visited = 0, [G.node_list[node] for node in G.node_list]
	visited = [not_visited.pop(0)]
	T = []
	# return not_visited, visited
	while True:
		#let u, v be the lowest cost edge such that u is in visited and v is in not_visited
		MIN = float('Inf')
		for u in visited:
			for v in not_visited:
				if u.is_neighbor(v):
					weight = u.get_weight(v)
					if weight < MIN:
						MIN = weight
						low_cost_edge = v
						# print(low_cost_edge)

		# print('Node with Lowest Cost: ')
		# print(low_cost_edge)
		visited.append(low_cost_edge)
		not_visited.remove(low_cost_edge)
		cost += MIN
		
		print('Cost: ' + str(cost))
		# print('Visited: ')
		# for node in visited:
			# print(node)
		# print('Not Visited: ')
		# for node in not_visited:
			# print(node)

		if len(not_visited) == 0:
			break

	# print('Answer: ')
	return cost

def main():
	filename = 'edges.txt'
	G = make_graph(filename)
	print(prims_algorithm((G)))

if __name__ == '__main__':
	main()



