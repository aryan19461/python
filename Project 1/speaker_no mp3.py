import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

while True:
    text = input("What do you want to say : \n")
    if text == "bye":
        print("BYE BYE BYE")
        break
    
    speak.speak(text)