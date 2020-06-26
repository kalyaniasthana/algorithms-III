import sys
import copy
from huffman_code import read_codes as read_vertex_weights

def max_weight_idp_set(no_of_vertices, weights):
	#constructing array A
	A = [0 for i in range(no_of_vertices + 1)]
	A[1] = weights[0]
	for i in range(2, no_of_vertices + 1):
		A[i] = max(A[i - 1], A[i - 2] + weights[i - 1])

	#reconstruction by backtracking
	S = []
	i = copy.deepcopy(no_of_vertices)
	while i >= 1:
		if A[i - 1] >= A[i - 2] + weights[i - 1]:
			i -= 1
		else:
			S.append(i)
			i -= 2

	return S

def main():
	filename = sys.argv[1]
	no_of_vertices, weights = read_vertex_weights(filename)
	S = max_weight_idp_set(no_of_vertices, weights)
	find = [1, 2, 3, 4, 17, 117, 517, 997]
	output = []
	for num in find:
		if num in S:
			output.append(1)
		else:
			output.append(0)
	print(output)

if __name__ == '__main__':
	main()