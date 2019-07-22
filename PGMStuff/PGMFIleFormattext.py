## will put python file here later on.

##PGM Test1

## What Is PGM?
		PGM is 


## Python Code For PGM rnadom image ##
import random

## Creating Each Singular Array inside of the outer one.
def mkarray():
	x = [] ## singular array with numbers
	for i in range(300): 
		x.append(random.randint(0,255)) ## append random numbers as each element 
	return x
## end

bigy = [] ## outer array.

for n in range(300):
	bigy.append(mkarray())


## Printing to file stuff ##
def ArrToString(arr):
	tmp1 = ""
	for i in arr:
		tmp1 += str(i) + " "
	return tmp1

zerosArray = []
for i in range(24):
	zerosArray.append(int("0"))

def toFile(arr):
	myf = open("test3.pgm","w")
	myf.write("P5\n300 300\n255\n")
	print(zerosArray)
	for i in arr:
		myf.write(ArrToString(i))
		print(i)
	myf.close()

toFile(bigy)
