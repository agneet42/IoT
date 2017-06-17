import csv

f = csv.reader(open("edges.csv","r"))

writable = csv.writer(open("nodes.csv","w"))

arr = ["ssup"]


for rows in f:
	a = rows[0]
	b = rows[1]
	flaga = 0
	flagb = 0
	for i in range(0,len(arr)):
		if(a == i):
			flaga = 1
		if(b == i):
			flagb = 1
	if(flaga == 0):
		writable.writerows([rows[0]])
		arr.append(rows[0])
	if(flagb == 0):
		writable.writerows([rows[1]])
		arr.append(rows[1])