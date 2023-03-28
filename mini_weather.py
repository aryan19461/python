weather = input("What is the weather today?")
if(weather == "Rain" or weather == "rain"):
    print("It will rain")
elif(weather == "Sunny" or weather == "sunny"):
    print("It will be sunny")
elif(weather == "Cloudy" or weather == "cloudy"):
    print("It will be Cloudy")
elif(weather == "thunder" or weather == "thunder"):
    print("It will be Thunderstorm - dangerous weather")
else:
    print("Wrong input  ")   
    

# Above same Program using function 
def climate(weather : str) :
    '''
    weather : str --> means we are telling the compiler that weather is a string thus making it easier for the pther uses to understand
    '''
    if(weather == "Rain" or weather == "rain"):
        print("It will rain")
    elif(weather == "Sunny" or weather == "sunny"):
        print("It will be sunny")   
    elif(weather == "Cloudy" or weather == "cloudy"):
        print("It will be Cloudy")
    elif(weather == "thunder" or weather == "thunder"):
        print("It will be Thunderstorm - dangerous weather")
    else:
        print("Wrong input  ")   

climate("Rain")