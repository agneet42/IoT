import re
import sys

from scipy import spatial

infile = open('newdata1.txt','r').readlines()
final_list = []
iter_list = []
for values in infile:
	iter_list = values.split()
	final_list.append(iter_list[0:9])

array1 = []
for array in final_list:
	if(array[1] != '?'):
		array1.append(array[0:9])

temp = []
final_array = []
for lst in array1:
	# print(lst)
	temp = [int(numeric_string) for numeric_string in lst]
	final_array.append(temp)

for lst in final_array:
	index = lst[0]
	print(index,end=" : ")
	for lst1 in final_array:
		if(index != lst1[0]):
			result = 1 - spatial.distance.cosine(lst[1:9], lst1[1:9])
			print(result,end=" ")
	print("\n")

infile.close()
	