import cv2
def show_myImage():
	camera = cv2.VideoCapture(0)
	ret_err, img = camera.read()
	cv2.imshow('my image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


show_myImage()
