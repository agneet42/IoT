import csv

lookup = dict()
for row1 in csv.reader(open("cosine.csv","r")):
    lookup[(row1[0], row1[1])] = row1[2]
with open("final1.csv", "w") as w:
    w1 = csv.writer(w)
    for row in csv.reader(open("division.csv","r")):
        if (row[0], row[1]) in lookup:
            store = (0.5*float(row[2])+0.5*float(lookup[(row[0], row[1])]))
            w1.writerow([row[0],row[1],store])