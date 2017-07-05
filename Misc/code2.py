import csv

arr = []
arr1 = []

obj = csv.reader(open("FinalNode.csv","r"))
obj1 = csv.reader(open("FinalNode.csv","r"))


for i in obj:
	if(len(i[0]) <= 3):
		arr.append(i[0])

for j in obj1:
	if(len(j[0]) > 3):
		arr1.append(j[0])	


# print(arr,arr1)

obj2 = csv.writer(open("TEdges.csv","w"))

obj3 = csv.reader(open("edges_things.csv","r"))


for row in obj3:
	check = 0
	value = row[0]
	value1 = row[1]
	value2 = int(row[0])
	for a in arr:
		if(int(a) == value2):
			check = check + 1
			break
	for b in arr1:
		if(b == value1):
			check = check + 1
			break
	if(check == 2):
		obj2.writerow([value2,value1,row[2]])