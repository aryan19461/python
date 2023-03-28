# (Arrays) List is a list of objects also called Arrays
numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
print(numbers[0]) # prints 0th index element
print(numbers) # prints complete array or list

# The first element is always the first element in the list
# The last element is always the last element in the list
# The middle element is the middle element in the list
print(numbers[-1]) # negative means start from the last element then it become -1 is 5the element and -2 is 4th element and so on




# (Slices) Lists are a sequence of objects that are a part of a larger list helps to cut the array or list to the part where you want to slice it down
# NOTE--> fist no is the inclusive but last number is exclusive. like 0:3 means the first 3 elements of the list excluding 3rd element
print(numbers[0:3]) # prints the first 3 elements of the list
print(numbers[3:4]) # prints the first 4 elements of the list
length = len(numbers)
print(length) # prints the length of the list

print("My name is Aryan and I love you all "[0:9]) # prints the first 9 elements of the list

print(numbers[0:6:2]) # prints the first 6 elements of the list but will skip 2 elements after every element


#  Dictionary -> key value pairs
# [] = list
# () = tuple
# {} = Sets
persons = {
    "name": "Aryan",
    "shirt":"White"
}
print(persons["name"]) # name is key which is unique and will call its pair which is Aryan


Laptop = {
    "OS": "Windows",
    "Ram": 8
}
print(Laptop["Ram"]) # Ram is key which is unique and will call its pair which is 8
 
# Making functions that uses dictionary keys

def net_worth():
    return person["assets"] - person["debt"]



def introduce():
    person ={
        "Name": "Aryan",
        "Age": 20,
        "Roll no" : 1901010022,
        "Gender"   : "Male",
        "assets": 100,
        "debt" : 50,
        "net_worth": lambda :  person["assets"] - person["debt"], # created an inline function for already created one 
        "fruits" : [" Apple", "Banana", "Mango"]
    }
    print(f"My Name is", {person["Name"]} , "\n And my Age is ", {person["Age"]} , "\n and my roll call is --> ",{person["Roll no"]} , " \n I am ", {person["Gender"]}," \n my net worth is -->",{person["net_worth"]()},"\n My favourite fruit is" )  # here we are calling networth fucntion so we are writing () after bracekts 
    print(person.values()) # prints the values of the dictionary
    print(person.keys()) # prints the keys of the dictionary


introduce()


