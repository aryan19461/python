from time import * # now we can use evry function in time without import writing everytime
import random as rand 

# print(time()) # counts second from the year 1970 by default

#wil maytch test1 and testinput ---> Now to make sure that our program does not stop when ecnountered an error so we are using Try and except 
def mistake(paraTest,userTest):
    error = 0
    for i in range(len(paraTest)):
        try :
            if(paraTest[i] != userTest[i]):
                error = error + 1
        except:
            error = error + 1
    return error
                
    
    

test = [
    " Tere aage to chaand lge farzi tu maane ye na maane teri marzi billi billi ankh goriya oyehoye mundeyanu patt goriye",
    "ki mai hoo hero tera ki mai hu hero tera aaahhaa aankhon ke panno pe  mene rkha tha sau dafa ",
    "Mana apna ishq adhura dil na uspe sharminda hai pura hokr khtm hua sab  jo hai jinda hai pura shyd meri zaan ka sdka maange teri zudai"
    ]

test1 = rand.choices(test)
print("             ********** Typing speed****************")
print(test1)
print() # gives one empty line
print()

#now time delay
def Speed_TIME(timeStart, timeEnd , userInput):
    time_Delay = timeEnd - timeStart
    time_roundoff = round(time_Delay,2)# round off hoga 2 digits tk
    speed = len(userInput)/time_roundoff
    return round(speed)    


time1 = time() #time starts before  asking for the input
testinput = input( "Enter test input : \n")
time2 = time() #time starts after completing the writing of string



print("speed : ",Speed_TIME(time1,time2,testinput), "  words per Seconds")
print("Error : ", mistake(test1,testinput))
