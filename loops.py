import array
# for loop
fruits_shop ={"Apple", "Banana", "Kiwo", "Orange", "Pomogranate"}

for fruit in fruits_shop:
    print("My favorite fruit is ",fruit)

'''

for fruit in fruits_shop:
    print("My favorite fruit is ",fruit)
    if(fruit == "Kiwo"):
        exit() --> when kiwo is encountered then exit() will exit the loop
        
Here enumerate() will return a tuple of index and value

for fruit in enumerate(fruits_shop):
    print("My favorite fruit is ",fruit)
    if(fruit == "Kiwo"):
        exit()



for index,fruit in enumerate(fruits_shop):
    print("My favorite fruit is ",fruit ,"at index ->",index)


'''
print("\n \n \n \n \n \n \n \n \n \n")

# Adding more things in array
# using range we can tell the loop to run this many time from 0 to 9 as 10 is not included but 0 is included
'''
for i in range(0,10):
    print("hhaha")
'''
for _  in range(0,10):
    print(fruits_shop)
    fruits_shop.add("Apple")
    

# while loop
