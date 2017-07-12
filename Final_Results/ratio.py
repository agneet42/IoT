import csv

file1 = csv.reader(open("reduced.csv"))
file2 = csv.reader(open("weka2.csv"))

for row in file1:
	break
for row1 in file2:
	break

count1 = 0
count2 = 0

for row in file1:
	if(row[0] != '0:00:00'):
		for index in range(1,len(row)):
			if(row[index] != '0'):
				count1 = count1 + 1

print(count1)

for row1 in file2:
	if(row1[0] != '0:00:00'):
		for index in range(1,len(row1)):
			if(row1[index] != '0'):
				count2 = count2 + 1

print(count2)

ans = count2 - count1
print(ans/100)