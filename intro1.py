'''
print("Hello World")
print("COders")
print("Python")
print("Intro to Python")
#-->"" represents the string.  Python is a case sensitive language.


'''

'''

# Variable 
name = "Aryan"
age = 22
print(name,age)

number = 24.4
Boolean_number2 = True
char_no = 'A'
print(number,Boolean_number2,char_no)

Fname = "Tony"
Lname = "Stark"
age = 51
trait = "genious"
print(Fname,Lname,"is of ",age,"yrs old","and he is a genious",trait)

'''
'''
name = input("What is your Name? ")
print(name)
# o/p -> What is your Name? aryan --> aryan

'''


# Type Conversion

'''
old_age = input("What is your age? ")
new_age = int(old_age) + 10
print(new_age)
'''

'''Here we are converting the age to integer. inititally age was being read as a string but doing int(old_age) will convert it to integer'''
'''
  *  float() function will convert the string to float
  *  str() function will convert the string to string
  *  boolean() function will convert the string to     boolean
'''
'''
#concatination example

f = input("enter first number : ")
s = input("enter second number : ")
s = f + s # concatination is done here 

print(s)
O/P 
enter first number : 5
enter second number : 6
56

''' 
'''


# printing  sum of 2 numbers
first = input("enter first number : ")
second = input("enter second number : ")
sum = int(first) + int(second) 
print("sum of two numbers is : ",sum)


'''


'''
#STRINGS
# Here a seperate variable is initalized and changes are done on that variable not in the orignal variables

name = "Aryan Singh"
print(name.upper()) 
print(name.find('n'))
print(name.replace("Aryan","Handsome"))
print("A" in name) 
# will show whether "A" is present in the name

'''

'''
# Comparison Operators
print(3 > 2) #True
print (3 >= 2 ) #True
print (3 == 2) #False
print (3 != 2) #True
'''

'''
# Logical Operator
print(2 > 3 or 2 > 1) #True if any one is true
print(2 > 1 and 3 > 2) #True if both are true
print(not 2 > 3)     #True change to False and vice versa

# if-statememt
age= 19
if(age < 18) :
    print("you are not eligible")
else :
    print("you are eligible")
print("Thank you") # default statement


#Elif statement
marks = 56
if(marks >40 and marks <=50):
    print("D")
elif(marks > 50 and marks <=60):
    print("C")
elif(marks > 60 and marks <=70):
    print("B")
elif(marks > 70 and marks <=80):
    print("A")
elif(marks > 80 and marks <=100):
    print("OUTSTANDING")
else :
    print("Exam not given")
print("Thank you")
'''

'''
# Basic calculator
first = input("enter first number : ")
operator = input("enter operator : (+,-,*,/,%)")
second = input("enter second number : ")
if(operator == "+"):
    print(int(first) + int(second))
elif(operator == "-"):
    print(int(first) - int(second))
elif(operator == "*"):
    print(int(first) * int(second))
elif(operator == "/"):
    print(int(first) / int(second))
elif(operator == "%"):
    print(int(first) % int(second))
print("Thank you for using")


'''
'''
# Range
no = range(5) # 0,1,2,3,4 is stored
print(no)
'''
'''
#Loops

#while Loops
i = 1
while(i <= 10):
    print(i)
    i = i + 1 

i = 1
while(i <= 5):
    print(i * "*")
    i = i + 1

i= 5
while(i >= 0):
    print(i * "*")
    i=i-1


#For Loops
for item in range(5):
    print(item)

'''

'''

#LIST-collection of items to store primitive data types
marks = [85,90,50]
print(marks) # prints complete list
print(marks[2]) # prints a specific item on that index number
print(marks[-1]) # in python -sign means starting from back direction 
print(marks[-2]) # prints last item on the list

print(marks[0:2]) # prints from index 0 to index 2(does not include 2)

for score in marks :
    print(score)


marks.append(99) # add item at the end of the list
marks.insert(1,100) # add item at the specific index
print (marks)

print(99 in marks) # returns true if item is present in the list
print(len(marks)) # returns the length of the list

#using list in while loop
i=0
while(i < len(marks)):
    print(marks[i])
    i =i+1


'''


'''
student = ["Aryan","Angela","Nikhil","Tarun","Tushar"]
for students in student :
    if(students == "Nikhil"):
        continue;
print(students)

'''
'''

# tuples --> immutable can not be changed
marks =(95,98,99,99,99,99)
print(marks.count(99)) # count 99
print(marks.index(98)) # index of 98
marks[0]=99 #will show error because tuple is immutable

'''

'''
#SETS -->  use to store collection of item but unique one only

[] = list
() = tuple
{} = Sets


marks = {95,98,99,99,99}
print(marks) # since its a set 99 is only printed once
print(marks[0]) # will show error because it is randomly organized or unordered as there is no idex

'''

'''
# dictonary --> key value pair
marks = {
    "English" : 89,
    "Maths" : 90,
    "Physics" : 95
}
print(marks["Maths"]) # will print maths's key value i.e. 90
marks["Chemistry"] = 66 # will add new key value pair
print(marks) 
 
marks["Physics"] = 96 # will update key value pair as it already exist
 
 
'''

'''
Functions in Python
Function is a piece of code that performs some task. (In a tv remote, each button performs a functions, so a function is like that button in code)
There are 3 types of functions in Java : 
In-built functions
 # int() str() float() min() range() max() 
Module functions
Module is a file that contains some functions & variables which can be imported for use in other files.
Each module should contain some related tasks
Example : math, random, string

import math
print(dir(math))

import random
print(dir(random))

import string
print(dir(string))

from math import sqrt
print(sqrt(4))


User-defined functions

	def sum(a, b=4):
   print(a + b)

sum(1, 2)
sum(1)

'''
