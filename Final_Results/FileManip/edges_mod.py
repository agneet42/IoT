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

print(val_spatio2)
print("********************")
print(val_social2)