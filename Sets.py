# SETS -> {}
#SETS -->  use to store collection of item but unique one only
'''
[] = list
() = tuple
{} = Sets

'''
marks = {95,98,99,99,99}
print(marks) # since its a set 99 is only printed once
#print(marks[0]) # will show error because it is randomly organized or unordered as there is no idex

list =['ruby', 'python', 'Java']
list2 = ['python', 'python', 'ruby', 'c++', "SQL","Java"]
language = list + list2
print(language) # it wil concatinate both list1 and list2 then print all items but if we use SETS then it will print only unique items
language_set = set(language)
print(language_set) # it will concatinate both list and list2 but since we are telling that it has to set therefore it will only show unique items




print("-------------------------------------------")
list ={'ruby', 'python', 'Java'}
list2 = {'python', 'python', 'ruby', 'c++', "SQL","Java"}
print(list2) # it will print the items in the set only unique ones

