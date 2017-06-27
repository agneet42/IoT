import csv
from iteration_utilities import flatten
import numpy as np 

room_1 = ["M047","M048","M046","T004","M045","M050","L001","M044","D004","M043","E002","T005","M042","L002"]
room_2 = ["M027","L003","M028","M029","M037","D003","M030","D005","M038","L005","M031","T003","M036","M032","M035","M033","M034","L004","M039","L006","F001","M040","D006","M041","L007","F002"]
room_3 = ["M004","M005","D002","M011","M012","M003","M006","T001","M010","M013","M009","R002","M002","M007","M014","D013","I011","I012","M008","M001","M015"]
room_4 = ["M023","M016","D012","D008","D009","D016","M022","D010","L010","M017","T002","R001","D007","D014","D015","M018","M019","M021","M026","L009","M025","M024","D001","M020","L011","D011","M051"]



s = "233.txt  275.txt  319.txt  360.txt  005.txt  050.txt  101.txt  142.txt  186.txt  234.txt  276.txt  321.txt  361.txt  006.txt  051.txt  102.txt  143.txt  187.txt  235.txt  277.txt  323.txt  362.txt  007.txt  052.txt  103.txt  144.txt  188.txt  236.txt  279.txt  324.txt  363.txt  008.txt  053.txt  104.txt  145.txt  189.txt  237.txt  280.txt  325.txt  365.txt  009.txt  054.txt  105.txt  146.txt  191.txt  238.txt  281.txt  326.txt  366.txt  010.txt  055.txt  106.txt  147.txt  192.txt  239.txt  282.txt  327.txt  367.txt  011.txt  056.txt  107.txt  149.txt  193.txt  241.txt  283.txt  328.txt  368.txt  012.txt  058.txt  108.txt  150.txt  194.txt  242.txt  285.txt  329.txt  370.txt  013.txt  059.txt  110.txt  151.txt  195.txt  243.txt  286.txt  330.txt  371.txt  014.txt  060.txt  111.txt  152.txt  196.txt  244.txt  288.txt  331.txt  372.txt  015.txt  063.txt  112.txt  153.txt  197.txt  245.txt  289.txt  332.txt  373.txt  017.txt  067.txt  113.txt  154.txt  199.txt  246.txt  290.txt  333.txt  375.txt  018.txt  069.txt  114.txt  155.txt  200.txt  247.txt  291.txt  334.txt  376.txt  020.txt  070.txt  115.txt  156.txt  201.txt  248.txt  293.txt  335.txt  377.txt  021.txt  071.txt  117.txt  157.txt  202.txt  249.txt  294.txt  336.txt  378.txt  022.txt  072.txt  118.txt  158.txt  203.txt  250.txt  295.txt  337.txt  379.txt  024.txt  073.txt  119.txt  159.txt  205.txt  251.txt  296.txt  338.txt  380.txt  025.txt  074.txt  120.txt  160.txt  206.txt  252.txt  297.txt  339.txt  381.txt  026.txt  076.txt  121.txt  161.txt  208.txt  253.txt  298.txt  340.txt  382.txt  027.txt  077.txt  122.txt  162.txt  209.txt  254.txt  299.txt  341.txt  383.txt  028.txt  078.txt  123.txt  163.txt  210.txt  255.txt  300.txt  342.txt  384.txt  029.txt  079.txt  124.txt  164.txt  211.txt  256.txt  301.txt  343.txt  385.txt  030.txt  080.txt  125.txt  165.txt  212.txt  257.txt  303.txt  344.txt  386.txt  031.txt  081.txt  126.txt  167.txt  214.txt  258.txt  304.txt  345.txt  387.txt  032.txt  082.txt  127.txt  169.txt  215.txt  259.txt  305.txt  346.txt  388.txt  033.txt  083.txt  128.txt  170.txt  216.txt  261.txt  306.txt  347.txt  389.txt  035.txt  084.txt  129.txt  171.txt  218.txt  262.txt  307.txt  348.txt  390.txt  037.txt  085.txt  130.txt  172.txt  220.txt  263.txt  308.txt  349.txt  391.txt  038.txt  087.txt  131.txt  173.txt  221.txt  264.txt  309.txt  350.txt  392.txt  039.txt  088.txt  132.txt  174.txt  222.txt  265.txt  310.txt  351.txt  393.txt  040.txt  089.txt  133.txt  175.txt  223.txt  266.txt  311.txt  352.txt  394.txt  041.txt  090.txt  134.txt  177.txt  225.txt  267.txt  312.txt  353.txt  395.txt  042.txt  091.txt  135.txt  178.txt  227.txt  268.txt  313.txt  354.txt  396.txt  043.txt  093.txt  136.txt  180.txt  228.txt  269.txt  314.txt  355.txt  397.txt  044.txt  095.txt  137.txt  181.txt  229.txt  270.txt  315.txt  356.txt  398.txt  045.txt  097.txt  138.txt  182.txt  230.txt  271.txt  316.txt  357.txt  399.txt  046.txt  098.txt  139.txt  183.txt  231.txt"
s1 = s.replace(".txt  ","")

arr = []
start = 0
end = 3
k = 0
while(k==0):
	if(end > (len(s1)-1)):
		break
	else:
		arr.append(s1[start:end])
		start = end
		end = end + 3


final_array = arr[0:(len(arr)-1)]

s2 = ["004","048","100","141","185","273","317","358","400","047","099","140","184","232","274","318","359"]

for elements in s2:
	final_array.append(elements)

arr = []

for file in final_array:
	read = csv.reader(open("%s.csv" %file,"r"))
	for rows in read:
		if(len(rows) == 4):
			if(rows[3] != ''):
				char = rows[3]
				s = None
				flag = 0
				if(len(char)==1):
					arr.append([rows[1],char])
					flag = 3
				elif(char[0] =="-" or char[0] == "."):
					flag = 4
				elif(char[1]=="." or char[1]=="-"):
					s = char[0:1]
					arr.append([rows[1],s])
					flag = 2
				elif(len(char)==2):
					if((int(float(char))>=1 and int(float(char))<=24)):
						arr.append([rows[1],char])
				elif(char[2]=="." or char[2]=="-"):
					s = char[0:2]
					if((int(float(s))>=1 and int(float(s))<=24)):
						arr.append([rows[1],s])
						flag = 1
				if(flag==0):
					pass

'''rooms = []
rooms.append(room_1)
rooms.append(room_2)
rooms.append(room_3)
rooms.append(room_4)

final_room = list(flatten(rooms))
print(final_room)'''

c1 = [0]*25
c2 = [0]*25

for sensors in room_3:
	for val in arr:
		if(val[0] == sensors):
			index = int(val[1])
			c1[index] = c1[index] + 1

for sensors in room_4:
	for val in arr:
		if(val[0] == sensors):
			index = int(val[1])
			c2[index] = c2[index] + 1

write = csv.writer(open("loc_loc.csv","a"))

count = 0
for i in range(0,len(c1)):
	if(c1[i] != 0 and c2[i] != 0):
		count = count + 1

print(c1)
print(c2)
write.writerow(["3","4",count])

