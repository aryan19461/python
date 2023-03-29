
# Here we are telling that try and except block is used to handle the error
try:
    a = int(input("Enter a number: "))
    print(a + 3)

except :
    print("You have entered a String ")   
'''

except Exception as e:
    print("You have entered a String ",e)  
 This Exception is used to handle the error plus showing why that error has occurred
 
'''

