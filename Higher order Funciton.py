'''
Higher order function -> 
* Map -> it is a function that takes two arguments and returns a new object.

* filter ->

'''

def double_number(number):
    return number * 2

print(list(map(double_number,[1,2,3,3])))

# Filter -> use to filter the data from the list
number = [1,2,3,4,5,6,7,8,9,10,11,12]
print(list(filter(lambda i : i%2==0, number))) # filter automatically loops every time

# list comprehension
print([i * 2 for i in number ]) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

# to get odd numbers
number_list = [1,2,3,4,5,6,7,8,9,10,11,12]
print([i for i in number_list if i%2 !=0 ]) #[1, 3, 5, 7, 9, 11]

# give all odd numbers cubed
number_list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
print([i**3 for i in number_list2 if i%2 !=0 ]) #[1, 27, 125, 343, 729, 1331]


