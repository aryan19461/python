
'''
# Randomly generates size of teh image 

import cv2 

# Load the image
src = cv2.imread("connor.png", cv2.IMREAD_UNCHANGED)

# Display the image
#cv2.imshow("Image", src)

# Wait for a key press
cv2.waitKey(0)

This code will load the image "connor.png" and display it in a window titled "Image". The 
cv2.waitKey(0)
function will wait for a key press before closing the window.
 
 
 
# percentage by which the image will be scaled
scale_percent = 50

#calculate the scale factor of orignal dimension

new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# dsize = random varaible to store new heignt and width
dsize = (new_width , new_height)

#resized image
output = cv2.resize(src, dsize)

cv2.imwrite("resized_image.png", output)
cv2.waitKey(0)



'''

import cv2
import matplotlib.pyplot as plt
import win32com.client as wincom


image = cv2.imread("connor.png")
cv2.imshow("Image", image)

#halve the image
half_img = cv2.resize(image, (0,0), fx=0.5, fy=0.5)

#twice the image
twice_img = cv2.resize(image, (0,0), fx=2, fy=2)

#biggggg
big_img = cv2.resize(image, (1900,1440))

# Now we storing all the four images with their tiles name in a  list so that we can access them all in on go
# title are generally the imahge name while images is the name of the window
titles = ["orignal","half_img","twice_img","big_img"]
images = [image, half_img, twice_img, big_img]
count = 4 # denotes the number of elements in the list
for img in range(count):
    plt.subplot(2,2,img+1)#This code creates a subplot grid with 2 rows and 2 columns, and selects the (img+1)th subplot to be the current subplot. The variable "img" is likely an integer representing the index of the current image being plotted.
    plt.title(titles[img])
    plt.imshow(images[img])

text = "Resizing is completed"
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(text)
plt.show()
