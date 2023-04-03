from tkinter import * # importing button and canvas -->use to make graphic 
import speedtest as speed



def speedCheck():
    # Checking wifi speed
    wifi = speed.Speedtest()
    wifi.get_servers()
    download = round(wifi.download()/10**6, 3)
    upload = round(wifi.upload()/10**6, 3)
    print( "Download speed --> ", download, " Mbps") #10**6 --> 10 ki power 6
    print( "Speed --> ", upload, " Mbps")
    label_down.config(text=download)
    label_up.config(text=upload)    





# this will create a blank window
background = Tk()
background.title("Internet Speed Test") # will change window title
background.geometry("700x700" ) # will change window size
#designing the label
background.configure(background="orange") # will change background color
label =Label(background,text="Internet Speed Test",font=("Times New Roman",20,"bold"),bg ="green",fg="white") 
label.place(x =50 , y = 60) # will change label position



#downloading speed label
label_down =Label(background,text="Downloading Speed Test",font=("Times New Roman",20,"bold"),bg ="pink",fg="white")
label_down.place(x =50 , y = 120)

label_down =Label(background,text="00",font=("Times New Roman",20,"bold"),bg ="pink",fg="white") # will change this 00 to actual download speed .
label_down.place( x = 450 ,y = 120)


#uploading speed
label_up =Label(background,text="Uploading Speed Test",font=("Times New Roman",20,"bold"),bg ="blue",fg="white")
label_up.place(x =50 , y = 220)


label_up =Label(background,text="00",font=("Times New Roman",20,"bold"),bg ="blue",fg="white")
label_up.place( x = 450 ,y = 220)

# Making a button
button = Button(background,text = "CHECK", font =("Cursive", 24,"bold"), relief=RAISED, bg ="green", fg="white", command = speedCheck()) # RAISED will be used to make it look like it is pressed

button.place(x = 150 , y = 420)
#will show the creaeted window
background.mainloop()


# setting the parameters --> the function we have made to get download speed and upload speed we have to shpw the speed test result in 00 above 
'''
In this script, the 
Button
 widget is created using the 
Button()
 of the 
tkinter
 module. The 
command
 parameter of the 
Button()
 method is used to specify the function that should be called when the button is clicked.

In this case, the 
command
 parameter is set to 
speedCheck()
, which is a function defined earlier in the script. When the user clicks the "CHECK" button, the 
speedCheck()
 function is called, which tests the internet speed and updates the labels with the new download and upload speeds.

So, the 
command
 parameter of the 
Button()
 method is used to bind a function to the button, which is executed when the button is clicked
'''