import os
from gtts import gTTS


if __name__ == "__main__":
    pass # means there is nothing to do in it and it will not show error while running this block

'''
we are creating a string variable "mycommand " that will store the the text you want to execute. then we are making a variable called "mylanguage" which take the accent of the speak .then we are using the gTTS function to convert the string variable into a mp3 file and stroring this in an object called "myobject"

'''
mycommand = "Aryan hu mai tu kon hai be bata vrna i don't know what type of thing i'll do "
MYlanguage = "en"

myobject = gTTS(text =mycommand, lang =MYlanguage,slow=False)


myobject.save("hello.mp3")
os.system("hello.mp3")
