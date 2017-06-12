import re

import numpy as np

infile = open ('newdata.txt', 'r')
outfile = open('test.txt', 'w')
column = 1
for line in infile:
	if not re.match('#', line):     
		line = line.strip()
		sline = line.split()
		outfile.write(sline[column] + '\n')
infile.close()
outfile.close()

arr = np.zeros(400)
k=0
newfile = open('test.txt', 'r')
for line in newfile:
	arr[k] = line
	k=k+1

final_array = [int(numeric_string) for numeric_string in arr]
for i in range(0,400):
	print(i+1," : ", end=" ")
	for j in range(0,400):
		if(i!=j):
			if(final_array[i]>final_array[j]):
				print(final_array[j]/final_array[i], end=" ")
			elif(final_array[j]>final_array[i]):
				print(final_array[i]/final_array[j], end=" ")
			else:
				print(final_array[j]/final_array[i], end=" ")
	print("\n")

newfile.close()


