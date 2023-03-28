# defining the function by using keyword def

# No argumnets
def hello():
    print("Hello function is called" )

hello()



print("-----------------------------Funciton with Parameters-------------------------------")



# functions with parameters --> making this function dynamic so that we change only the name which is the parameter instead of going through the function
def intro(name):
    print(name)


intro("Aryan")

def intro2(name2):
    print(f'Hey intro2 is called by { name2 }')
intro2("Aryan")

print("----------------Multiple Arguments--------------------------------------------")


# Multiple Arguments
def greeting(name,greet):
    print(f'Hello greeting is called by {name} and {greet}') # here f'--' is called to print the greeting and the name in a manner that we don't always do the typecasting
greeting("Sing","Welcme the tribal cheif")


print("----------Default Arguments--------------------------------------------------")

# Default Arguments --> greet will take default greeting if not provided by the user
def greeting2(name,greet="Default greeting"):
    print(f'Hello greeting is called by {name} and {greet}') # here f'--' is called to print the greeting and the name in a manner that we don't always do the typecasting
greeting2("Sing")

print("------------------Named arguments------------------------------------------")

# named arguments --> postion of name and greet doesn't matter that is greet is called first or not
greeting(greet="Named Argument is called", name="Roman")
 
print("------------------------------------------------------------")
# Example of function with multiple arguments

def sum(a,b):
    return a+b
print(sum(2,3)) # return functions neeed print function

# Example 1
def Big_ONE(a : int,b : int):
    if(a > b) :
        print(f'{a} is greater than {b}')
    elif(a < b) :
        print(f'{b} is greater than {a}')
    else:
        print(f'{a} and {b} are equal')
Big_ONE(2132,32133)

print("------------------------------------------------------------")



# LAMBDA is a special function in python which is used to create an anonymous function

#example 1
def sum(a,b):
    return a+b
    # OR
sum2 = lambda a,b : a+b # implicit return , in Lambda  there can only be one expression
print(sum2(5,20))


# lamda arg1,arg2 ...: <expressions>
greet = lambda greet,name : f"{greet} {name}"
print(greet("Ni hao mao","Aryan"))


