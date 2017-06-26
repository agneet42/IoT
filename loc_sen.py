import csv

'''room_1 = ["M047","M048","M046","T004","M045","M050","L001","M044","D004","M043","E002","T005","M042","L002"]
room_2 = ["M027","L003","M028","M029","M037","D003","M030","D005","M038","L005","M031","T003","M036","M032","M035","M033","M034","L004","M039","L006","F001","M040","D006","M041","L007","F002"]
room_3 = ["M004","M005","D002","M011","M012","M003","M006","T001","M010","M013","M009","R002","M002","M007","M014","D013","I011","I012","M008","M001","M015"]
room_4 = ["M023","M016","D012","D008","D009","D016","M022","D010","L010","M017","T002","R001","D007","D014","D015","M018","M019","M021","M026","L009","M025","M024","D001","M020","L011","D011","M051"]



obj = csv.reader(open("only_sensors.csv","r"))
obj1 = csv.reader(open("only_sensors.csv","r"))
obj2 = csv.reader(open("only_sensors.csv","r"))
obj3 = csv.reader(open("only_sensors.csv","r"))

writ = csv.writer(open("loc_sen.csv","a"))

check = []
for row in obj:
	check.append(row[0])


for val in room_4:
	f=0
	for val1 in check:
		if(val == val1):       
			f=1	
			break		
	if(f==0):				
	#	print(val)  uncomment to print anomalies


for val in room_4:
	writ.writerow(["4",val])'''


x = csv.reader(open("loc_sen.csv","r"))

weight = csv.writer(open("loc_sen_weights.csv","w"))

for rows in x:
	weight.writerow([rows[0],rows[1],"1"])
