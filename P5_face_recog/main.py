# Face recognition and Cmake module 
import face_recognition_models
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0) # number inside () represent your camera number if there are two camera then 0 fill use 1st camera and 1 uses 2nd camera

#loading known faces and encoding that is providing them a number to remember them
image1_file = face_recognition_models.load_image_file("1.png")
image1_encoding = face_recognition_models.face_encoding(image1_file)[0]


image2_file = face_recognition_models.load_image_file("2.png")
image2_encoding = face_recognition_models.face_encoding(image2_file)[0]


#Storing them in a List
known_face_encodings = [image1_encoding, image2_encoding]
know_face_name = ["Aryan" ,"Connor "]

#List of expected students
know_face_name = ["Aryan" ,"Connor "] # here the face will searched

face_locations = []
face_encodings = []

#getting the time of face scanned
now =datetime.now()
current_date = now.strftime("%d/%m/%Y %H:%M:%S")

# making CSV writer
f =open(f"{current_date}.csv ", "w", newline="")
lnwriter = csv.writer(f)

while True:
    _,frame = video_capture.read() # when video captured is used there first argument is always a _ which tells whether it is captured or not then comes the frame
    small_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5) 
    rgb_small = cv2.cvtColor(small_frame,cv2.COLOR_BGR2GRAY)
    
    # recognizing faces   
    face_locations = face_recognition_models.face_locations(rgb_small)
    face_encodings = face_recognition_models.face_encodings(rgb_small, face_locations)
    
    for face_encode in face_encodings:
        matches = face_recognition_models.compare_face(known_face_encodings, face_encode)
        face_distance = face_recognition_models.distance(known_face_encodings, face_encode)
        best_match_index = np.argmin(face_distance)
        
        if(matches[best_match_index]):
            name = know_face_name[best_match_index] #will get the name whose face is matched
            
    cv2.imshow('Attendence',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):#when q is pressed we will leave while loop
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()

