import numpy as np 
import csv
from sklearn import preprocessing

obj = csv.reader(open("TEdges.csv","r"))
write = csv.writer(open("Normal.csv","w"))



obj = csv.reader(open('FinalEdge.csv','r'))

arr = []
for rows in obj:
	if(len(rows[0]) >3 or len(rows[1])>3):
		arr.append(float(rows[2]))

num_arr = np.asarray(arr)

val = mean(num_arr))

arr = []
for row in obj:
	arr.append(int(row[2]))

data = np.asarray(arr)
scale = preprocessing.minmax_scale(data, feature_range=(val,(val+0.1)))

for values in scale:
	write.writerow([values])


