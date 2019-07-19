##we will create a very simple 100x100 image in pbm format.
import random
def mkArray():
	x = []
	for n in range(100):
		x.append(random.randint(0,1))
	return x

def ArrToString(arr):
	tmp = ""
	for i in arr:
		tmp += str(i) + " "
	return tmp

bigx = []

for i in range(100):
	bigx.append(mkArray())

myf = open("test1.pbm", "w")
myf.write("P1\n100 100\n")

for x in bigx:
	myf.write(ArrToString(x))

myf.close()
