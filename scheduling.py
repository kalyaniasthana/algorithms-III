import sys
# sys.path.insert(1, '../algorithms-II')
# from min_heap import read_list
import copy

def read_jobs(filename):
	weights = []
	lengths = []

	with open(filename) as f:
		for line in f:
			line = line.strip('\n').split(' ')
			weights.append(int(line[0]))
			lengths.append(int(line[1]))

	return weights, lengths

# def objective_function(weights, lengths, no_of_jobs):
	# of = []
	# for i in range(no_of_jobs):
		# of.append(float(weights[i] - lengths[i]))
# 
	# return of

# jobs are scheduled with decreasing value of objective function
# find maximum
# find all matches of this maximum value
# sort these jobs with same maximum values according to weight and add to schedule

def schedule_jobs(weights, lengths, no_of_jobs):
	schedule = []
	for i in range(no_of_jobs):
		# schedule.append([weights[i], lengths[i], float(weights[i]) - float(lengths[i])])
		schedule.append([weights[i], lengths[i], float(weights[i])/float(lengths[i])])
	schedule.sort(key = lambda x: x[2])
	schedule = schedule[:: -1]

	# print(of)
	# of_ = copy.deepcopy(of)i
	# print(of_, 'objective function')

	# while len(schedule) != no_of_jobs:
		# m = max(of)
		# find all indices of max value m
		# max_value_indices = [i for i, j in enumerate(of) if j == m]
		# print(max_value_indices)
		# print(of, schedule, m, max_value_indices)
		# mvi = []
		# for index in max_value_indices:
			# item = of[index]
			# indices = [i for i, x in enumerate(of_) if x == item]
			# mvi += indices
		# mvi = list(set(mvi))

		# if len(max_value_indices) > 1:
			# weights_max_values = [weights[i] for i in mvi]
			# print(mvi, max_value_indices, weights_max_values)
			# print(mvi, weights_max_values, 'mvi, wmv')
			# sort x based on y Z = [x for _,x in sorted(zip(Y,X))]
			# sort max_value_indices based on weights_max_value in reverse
			# mvi = [i for j, i in sorted(zip(weights_max_values, mvi), reverse = True)]
			# print(mvi, max_value_indices, of)

		# mvi = list(set(mvi))
		# print(mvi)
		# remove indices of max value indices from of
		# of = [i for j, i in enumerate(of) if j not in max_value_indices]
		
		# schedule += mvi

		
			# print(x)
		# print(mvi, max_value_indices, of)

	return schedule

def compute_completion_times(schedule, weights, lengths, no_of_jobs):
	completion_times = [0 for i in range((no_of_jobs))]
	time = 0

	for index in schedule:
		time += lengths[index]
		completion_times[index] = time

	return completion_times

# def sort_schedule(schedule, no_of_jobs):

# 	for i in range(no_of_jobs):
# 		current_weight = schedule[i][2]
# 		till_index = i
# 		for j in range(i, no_of_jobs):
# 			if schedule[j][2] == current_weight:
# 				till_index = j
# 			else:
# 				break
# 		if i != till_index:
# 			print(i, till_index)
# 			# print(schedule)
# 			for k in range(i, till_index + 1):
# 				for l in range(till_index):
# 					if schedule[l][0] < schedule[l + 1][0]:
# 						schedule[l], schedule[l + 1]  = schedule[l + 1], schedule[l]
# 			break

# 	return schedule


def weighted_completion_times(schedule):
	# weighted_completion_times = []
	ctime = 0
	sum_ctimes = 0
	for job in schedule:
		ctime += job[1]
		job.append(ctime)
		sum_ctimes += ctime*job[0]
		job.append(ctime*job[0])

	return sum_ctimes

def main():
	# filename = 'scheduling_test_case.txt'
	filename = 'jobs.txt'
	no_of_jobs = 10000
	w, l = read_jobs(filename)
	# of = objective_function(w, l, no_of_jobs)
	# print(w, 'weights')
	# print(l, 'lengths')
	schedule = schedule_jobs(w, l, no_of_jobs)
	# schedule = sort_schedule(schedule, no_of_jobs)
	# print(schedule)
	# sys.exit()
	# completion_times = compute_completion_times(schedule, w, l, no_of_jobs)
	schedule = weighted_completion_times(schedule)
	print(schedule)

if __name__ == '__main__':
	main()