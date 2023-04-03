from tkinter import *

'''
def calculations ():
    print("Enter number 1 : ")
    a= int(input("\n"))
    print("Enter number 2 : ")
    b= int(input("\n"))
    operator = input("Enter operator : " ) 
    try:
        if(operator == "+"):
            print("Result is : ", a+b)
        if(operator == "-"):
            print("Result is : ", a-b)
        if(operator == "/"):
            print("Result is : ", a/b)
        if(operator == "%"):
            print("Result is : ", a%b)
        if(operator == "*"):
            print("Result is : ", a*b)
        if(operator == "^"):
            print("Result is : ", a**b)
    except:
        print("Enter a valid number")    
   
'''
print("Enter number 1 : ")
a= int(input("\n"))
print("Enter number 2 : ")
b= int(input("\n"))
operator = input("Enter operator : " ) 
try:
    if(operator == "+"):
            print("Result is : ", a+b)
    if(operator == "-"):
            print("Result is : ", a-b)
    if(operator == "/"):
            print("Result is : ", a/b)
    if(operator == "%"):
            print("Result is : ", a%b)
    if(operator == "*"):
            print("Result is : ", a*b)
    if(operator == "^"):
            print("Result is : ", a**b)
except:
        print("Enter a valid number")    
    
        
backgroudWindow = Tk()
backgroudWindow.title("Calculator")
backgroudWindow.geometry("500x600")
label = Label(backgroudWindow, text="Enter Number 1 " , font=("Arial", 20), bg="lightblue")
label.place(x=50, y=50)
label = Label(backgroudWindow, text="Enter Number 2 ", font=("Arial", 20), bg="lightblue")
label.place(x=50, y=250)

label = Label(backgroudWindow, text="Result", font=("Arial", 20), bg="lightblue")
label.place(x=50, y=350)

button = Button(backgroudWindow, text="Calculate", font=("Arial", 20), bg="lightblue",relief=RAISED,command=calculations())
button.place(x=150, y=450)

backgroudWindow.mainloop()