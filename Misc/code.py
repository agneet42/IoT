import csv

obj = csv.reader(open("TEdges.csv","r"))
obj1 = csv.reader(open("Normal.csv","r"))
f = csv.writer(open("abc.csv","w"))

for rows in obj:
	for x in obj1:
		f.writerow([rows[0],rows[1],x[0]])
		break

		


