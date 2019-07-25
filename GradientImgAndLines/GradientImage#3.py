def mkArray():
	x = []
	tmp=0
	for n in range(0, 300):
		tmp += 1
		if tmp % 2 == 0:
			x.append(tmp)
		else:
			x.append(0)
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
	myf = open("test7.pgm","w")
	myf.write("P2\n300 300\n255\n")
	for n in biga:
		myf.write(ArrayToString(n))
	myf.close()

mkFile()
