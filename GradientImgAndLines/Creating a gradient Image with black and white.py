def mkArray():
	x = []
	tmp=0
	for n in range(0, 300):
		x.append(tmp)
		tmp += 1
		if tmp > 255:
			tmp = 255
	return x
biga = []

for n in range(0, 300):
	biga.append(mkArray())

def ArrayToString(arr):
	tmp = ""
	for i in arr:
		tmp += str(i) + " "
	return tmp

def mkFile():
	myf = open("test4.pgm","w")
	myf.write("P2\n300 300\n255\n")
	for n in biga:
		myf.write(ArrayToString(n))
	myf.close()

mkFile()
