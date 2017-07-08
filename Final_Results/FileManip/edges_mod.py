import csv
import numpy as np

arr_social = []
arr_spatio = []
f = csv.reader(open("result.csv","r"))
f2 = csv.reader(open("result.csv","r"))
f1 = open("result_spatio.txt","r")
for row in f:
	if(":" in row[1]):
		arr_social.append(row[0])

for row in f1:
	for index in range(0,len(row)):
		if(row[index] == 'M' or row[index] == 'T' or row[index] == 'L' or row[index] == 'D' or row[index] == 'R' or row[index] == 'I' or row[index] == 'F' or row[index] == 'E'):
			arr_spatio.append(row[index:index+4])
	break

a = np.asarray(arr_social)
b = np.asarray(arr_spatio)

arr_both = np.intersect1d(a,b)


arr_final = arr_both.tolist()
# print(arr_final)

a = csv.reader(open("result_spatio1.csv","r"))

final_val = []
for row1 in a:
	final_val.append(row1[14:])

val_spatio2 = []
val_temp = []
c = 0

for row in final_val:
	val_temp.append([arr_spatio[c]])
	c = c + 1
	for index in range(0,len(row)):
		val_temp.append([arr_spatio[index],row[index]])
	val_spatio2.append(val_temp)
	val_temp = []

val_social = []
val_temp = []

first_loop = True
for rows in f2:
	if(first_loop == True):
		val_temp.append([rows[0]])
		first_loop = False
	elif(":" in rows[1]):
		val_social.append(val_temp)
		val_temp = []
		val_temp.append([rows[0]])
	else:
		val_temp.append([rows[0],rows[1]])

val_temp = []
val_social1 = []
for arr in val_social:
	val = arr[0]
	for sensors in arr_final:
		if(val[0]==sensors):
			val_social1.append(arr)


val_social2 = []
for arr in val_social1:
	first_loop = True
	for each in arr:
		check = each[0]
		for sensors in arr_final:
			if(check == sensors and first_loop == False):
				val_temp.append([check,each[1]])
				break
			if(check == sensors and first_loop ==True):
				val_temp.append([check])
				first_loop = False
				break
	val_social2.append(val_temp)
	val_temp = []

arr = []

# social gets 2/3 and spatio gets 1/3

result1 = csv.writer(open("social_results1.csv","w"))
result2 = csv.writer(open("spatio_results1.csv","w"))

for val in val_social2:
	first_arr = val[0]
	result1.writerow([first_arr[0]])
	for index in range(0,len(val)):
		if(val[index][0] != first_arr[0]):
			result1.writerow([val[index][0],(val[index][1])])

for val in val_spatio2:
	first_arr = val[0]
	result2.writerow([first_arr[0]])
	for index in range(0,len(val)):
		if(val[index][0] != first_arr[0]):
			result2.writerow([val[index][0],(val[index][1])])

result = csv.writer(open("combinedresult.csv","w"))

for i in range(0,len(val_spatio2)):
	arr = val_spatio2[i]
	first_val = arr[0]
	for j in range(0,len(val_social2)):
		arr1 = val_social2[j]
		first_val1 = arr1[0]
		if(first_val[0] == first_val1[0]):
			result.writerow([first_val[0]])
			for val in arr:
				for val1 in arr1:
					if(len(val) == 1 or len(val1) == 1):
						pass
					if(val[0] == first_val[0] or val1[0] == first_val1[0]):
						pass
					elif(val[0] == val1[0]):
						result.writerow([val1[0],float(val[1])*1/3 + float(val1[1])*2/3])
			



