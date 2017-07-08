import csv
from collections import Counter

f = csv.reader(open('nodes_things.csv','r'))
f2 = csv.reader(open('nodes_things.csv','r'))
f1 = csv.reader(open('nodes_users.csv', 'r'))

arr_t = []
arr_u = []

for rows in f:
	value = rows[0]
	if(len(value)==3):
		arr_t.append(value)


for rows in f1:
	arr_u.append(rows[0])


final_arr = []

for i in range(0,len(arr_t)):
	value = int(arr_t[i])
	for j in range(0,len(arr_u)):
		if(value == int(arr_u[j])):
			final_arr.append(value)
			break



final_arr.sort()

# print((final_arr))

for i in range(0,len(final_arr)):
	final_arr[i] = str(final_arr[i])

# print(final_arr)


'''file1 = csv.writer(open("UNodes.csv","a"))

# for elements in final_arr:
	# file1.writerow([elements])


for obj in f2:
	print(obj)
	if(len(obj[0]) > 3):
		file1.writerow([obj[0]])'''

a = csv.reader(open('edges_things.csv','r'))
a1 = csv.reader(open('nodes_things.csv','r'))
b = csv.writer(open("TEdges.csv","w"))

final_arr1 = []

for rows in a1:
	if(len(rows[0]) > 3):
		final_arr1.append(rows[0])

# print(final_arr1)

for rows in a:
	check = 0
	value = rows[0]
	value1 = rows[1]
	for i in final_arr:
		if(value == i):
			check = check + 1
			break
	for j in final_arr1:
		if(value1 == j):
			check = check + 1
			break
	if(check == 2):
		b.writerow([value,value1,rows[2]])



