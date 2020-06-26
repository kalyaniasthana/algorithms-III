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

	return schedule

def compute_completion_times(schedule, weights, lengths, no_of_jobs):
	completion_times = [0 for i in range((no_of_jobs))]
	time = 0

	for index in schedule:
		time += lengths[index]
		completion_times[index] = time

	return completion_times

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
	schedule = schedule_jobs(w, l, no_of_jobs)s
	schedule = weighted_completion_times(schedule)
	print(schedule)


if __name__ == '__main__':
	main()