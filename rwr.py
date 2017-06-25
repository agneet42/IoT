import csv 
import random
import numpy as np

file = csv.reader(open("FinalEdge.csv","r"))
sensors = csv.reader(open("only_sensors.csv","r"))

sensors_list = []
for rows in sensors:
	sensors_list.append(rows[0])

relevance_list = []
for i in range(0,len(sensors_list)):
	relevance_list.append(sensors_list[i])


final_array = []
for row in file:
	temp_arr = [None] * 3
	temp_arr[0] = row[0]
	temp_arr[1] = row[1]
	temp_arr[2] = row[2]
	final_array.append(temp_arr)

# print(final_array)

restart_probability = 0.3


for values in sensors_list:
	count_relevance = [0] * len(relevance_list)
	start = values
	already_visited = []
	already_visited.append(values)
	iter_list = []
	for loop1 in range(0,999):
		already_visited = []
		already_visited.append(values)
		p = None
		total_iter = 0
		k = 999
		while(total_iter != 999):
			p = None
			for p in range(1,k+1):
				node = []
				weight = []
				sum_weight = 0
				for arr in final_array:
					if(arr[1] == start or arr[0] == start):
						iter_list.append([arr[0],arr[1],arr[2]])
				for loop in iter_list:
					node.append(loop[0])
					weight.append(float(loop[2]))
				sum_weight = sum(weight)
				normalise_weight = []
				for x in range(0,len(weight)):
					normalise_weight.append(weight[x]/sum_weight)
				numpy_thing = np.asarray(normalise_weight)
				index = np.random.choice(np.arange(0,len(numpy_thing)), p = numpy_thing)
				if(node[index] == start):
					for val in iter_list[index]:
							if(val != start):
								start = val
								break
				else:
					start = node[index]
				check = len(already_visited) - 1
				if(already_visited[check-1] != start):
					already_visited.append(start)
				total_iter = total_iter + 1
				# print(total_iter, already_visited)
				if(total_iter == 999):
					break
				prob = random.uniform(0,1)
				if(prob > restart_probability):
					pass
				else:
					already_visited = []
					already_visited.append(values)
					k = k - p
					break
		flag = 0
		iter_list = []
		node = []
		weight = []
		length = len(already_visited)
		if(already_visited[length-1]==values):
			flag = 1
		elif(len(already_visited[length-1]) > 3):
			flag = 1
		else:
			stop = already_visited[length-1]
			for arr in final_array:
				if(arr[0] == stop and len(arr[1]) > 3):
					iter_list.append([arr[0],arr[1],arr[2]])
			for loop in iter_list:
				node.append(loop[1])
				weight.append(float(loop[2]))
			sum_weight = sum(weight)
			normalise_weight = []
			for x in range(0,len(weight)):
				normalise_weight.append(weight[x]/sum_weight)
			numpy_thing = np.asarray(normalise_weight)
			index = np.random.choice(np.arange(0,len(numpy_thing)), p = numpy_thing)
			if(node[index] != values):
				already_visited.append(node[index])
		if(flag != 1):
			for i in range(0,len(relevance_list)):
				if(relevance_list[i] == already_visited[len(already_visited)-1]):
					count_relevance[i] = count_relevance[i] + 1
					break

	result = [x/1000 for x in count_relevance]
	print(values, end=" : ")
	for j in len(0,len(result)):
		print(relevance_list[j],result[j])
	
