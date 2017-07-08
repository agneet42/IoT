import csv
import operator
file = csv.reader(open("combinedresult.csv","r"))
file1 = csv.writer(open("top5combined.csv","w"))

d ={}
first_loop = 1

for rows in file:
	if(len(rows) == 1 and first_loop == 1):
		file1.writerow([rows[0]])
		first_loop = 0
	elif(len(rows) == 1):
		c = 0
		sorted_x = sorted(d.items(), key=operator.itemgetter(1),reverse = True)
		for keys in sorted_x:
			if(c==5):
				break
			file1.writerow([keys[0],keys[1]])
			c = c + 1
		d = {}
		file1.writerow([rows[0]])
	else:
		val = float(rows[1])
		d[rows[0]] = val
