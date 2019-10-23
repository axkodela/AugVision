import cv2
import numpy as np
from Tkinter import *

myMw = Tk()
myMw.geometry("+0+0")
myCam = cv2.VideoCapture(0)
showing = True

def showMenu():
	global showing
	if showing == True:
		myMenu.grid_remove()
		showBttn.configure(text="Show")
		showing = False
	else:
		myMenu.grid()
		showBttn.configure(text="Hide")
		showing = True


def captureImage():
	global myCam
	ret_Val, img = myCam.read()
	return img

def showImage(ix, p1, p2):
	overlay = ix.copy()
	overlay=cv2.Canny(overlay,p1,p2)
	myShape = overlay.shape
	flattenShape = overlay.flatten()
	repeatedShape = flattenShape.repeat(3)
	reshapedShape = repeatedShape.reshape(myShape[0],myShape[1],3)
	
	ixnew=cv2.add(reshapedShape, ix)
	cv2.imshow('my Camera1', ixnew)

##  UI ##
myMenu = Frame(myMw)
myMenu.grid(row = 1, column=0)

showBttn = Button(myMw, text="hide", command=showMenu)
showBttn.grid(row = 0, column = 0)

c1Label = Label(myMenu, text="Min. Val.:")
c1Label.grid(row = 0, column = 0)

c1Scale = Scale(myMenu, from_ = 0, to = 200, orient = HORIZONTAL)
c1Scale.grid(row = 0, column = 1)

c2Label = Label(myMenu, text="Max. Val.:")
c2Label.grid(row = 1, column = 0)

c2Scale = Scale(myMenu, from_ = 0, to = 200, orient = HORIZONTAL)
c2Scale.grid(row = 1, column = 1)

## End of UI ##

while True:
	ixl = captureImage()
	showImage(ixl, c1Scale.get(), c2Scale.get())
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	myMw.update()

cv2.release()
cv2.destroyAllWindows()	
