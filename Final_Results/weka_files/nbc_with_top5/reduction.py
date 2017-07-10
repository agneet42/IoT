import csv
import operator
import collections

file = csv.reader(open("weka2.csv","r"))
file1 = csv.reader(open("weka2.csv","r"))

arr_duration = []
arr_label = []
for i in file1:
	arr_duration.append(i[0])
	arr_label.append(i[len(i)-1])

arr_duration = arr_duration[1:]
arr_label = arr_label[1:]

arr_sensors = []
arr_values = []

for row in file:
	for index in range(1,len(row)-1):
		arr_sensors.append(row[index])
	break

for row in file:
	arr_tmp = []
	for index in range(1,len(row)-1):
		arr_tmp.append(row[index])
	arr_values.append(arr_tmp)	

arr_top5 = []
arr_tmp = []

file1 = csv.reader(open("top5combined.csv","r"))
first_loop = True
for val in file1:
	if(len(val)==1 and first_loop==True):
		first_loop=False
		arr_tmp.append(val[0])
	elif(len(val)==1):
		arr_top5.append(arr_tmp)
		arr_tmp = []
		arr_tmp.append(val[0])
	else:
		arr_tmp.append(val[0])

ans = csv.writer(open("reduced.csv","w"))
count = 0

for arr in arr_values:
	d = {}
	d1 = collections.OrderedDict()
	c = 0
	for index in range(0,len(arr)):
		d[arr_sensors[index]] = arr[index]
	for index1 in range(0,len(arr)):
		d1[arr_sensors[index1]] = arr[index1]
	sorted_x = sorted(d.items(), key=operator.itemgetter(1),reverse = True)
	for keys in sorted_x:
		if(c==5):
			break
		sensor = keys[0]
		for arr1 in arr_top5:
			if(sensor == arr1[0]):
				to_be_replaced = arr1[1:]
				for val in to_be_replaced:
					for key in d:
						if(key==val):
							d[key] =0
							break
				break
		c = c + 1
		to_write = []
	for key in d:
		print(key,end=",")
		to_write.append(d[key])
	a = arr_duration[count]
	b = arr_label[count]
	final = [a] + to_write + [b]
	ans.writerow(final)
	count = count + 1	
	
	