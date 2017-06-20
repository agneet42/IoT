import csv
from iteration_utilities import deepflatten
# from underscore import _
from collections import Counter

obj = csv.reader(open("stupid.csv", "r"))
obj1 = csv.reader(open("stupid.csv", "r"))
ans = csv.writer(open("answer.csv", "w"))

arr = []
for rows in obj:
	arr.append(rows[0])

final_arr = []

temp = "233"
arr = []
for rows in obj1:
	if(rows[0] == temp):
		arr.append(rows[2])
	else:
		arr1 = [int(numeric_string) for numeric_string in arr]
		a = sum(arr1)
		for i in range(0,len(arr1)):
			arr1[i] = arr1[i]/a
		final_arr.append(arr1)
		arr = []
		arr.append(rows[2])
		temp = rows[0]

# print(final_arr)


final_list = list(deepflatten(final_arr, depth = 1))

final_obj = csv.reader(open("stupid.csv", "r"))

j = 0
for rows in final_obj:
	ans.writerow([rows[0],rows[1],final_list[j]])
	j = j + 1

