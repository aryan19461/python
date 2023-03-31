from gtts import gTTS
import speech_recognition as sr
import win32com.client as wincom



# obtain audio from the microphone
r = sr.Recognizer()
speak = wincom.Dispatch("SAPI.SpVoice")

with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:


    text = r.recognize_google(audio)
    print("You said: " + text)

    # convert text to speech
    tts = gTTS(text)
    speak.speak(text)
    #tts.save("output.mp3")
    
    # play the audio file
    #os.system("output.mp3")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
'''
In this code, we first obtain audio input from the user using the SpeechRecognition library. We then use the Google Speech Recognition API to convert the audio input into text. Once we have the text, we use the gTTS library to convert the text into an audio file. Finally, we play the audio file using the mpg321 command.

'''