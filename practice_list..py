# Create a function that doubles the list passed in.
def double(numbers : list) :
    result =[] # creating an empty array to store answer
    for number in numbers :
        print(number)
        result.append(number *2 ) # adding list element to result array
    print("result array : ",result)

double([1,2,3,4,5])

print("-------------------------------------------------")
'''
split(',') --> means it removes , from the string representation and return teh string. 

len functions by default seperates the string word when it encounters a space --> len(phrase)
'''
# Count the number of words in string --> do not count spaces
def count_words(phrase : str) :
    print("String is : ",phrase)
    print("Number of words : ",len(phrase.split()))

count_words("Aryan is best")      
    
    
    


print("-------------------------------------------------")

print("-------------------------------------------------")

# create a functions that takes list and return its sum of elements
def sum_List(num : list) -> int:
    print("List is : ",num)
    
    sum = 0
    for i in num:
        sum = sum + i # taking each element using i 
    print("Sum is : ",sum)
    
sum_List([1,2,3,4,5])
 

print("-------------------------------------------------")

print("-------------------------------------------------")

# Find the max elemnent in list

def maxxy(number : list):
    print("List is : ",number)
    current_MAX = number[0]
    for i in number:
        if(i >= current_MAX):
            current_MAX = i
        else:
            print(current_MAX)

    print("Max element is : ",current_MAX)

maxxy([1,2,3,4,5,])





print("-------------------------------------------------")

print("-------------------------------------------------")

print("-------------------------------------------------")
print("\n \n \n \n \n")


# create a  function to find word frequency of all repeated words --> should return a dictionary 


def word_frequency(phrase ):
    result = {}
    words = phrase.split() # splitting the phrase after every space encountered -> ['I', 'love', 'Batman', 'because', 'I', 'am', 'Batman']
   # Now we are storing everything in empty dictionary but since its an empty dictionary only the unique words are stored and when it runs the next time and the same words are encounted then it will increment the key value
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] = result[word] + 1
    return result
    
         
print(word_frequency("I love Batman because I am Batman"))
#dynamic input
#print(word_frequency(input("Please enter the phrase : ")))


print("-------------------------------------------------")

print("-------------------------------------------------")

print("-------------------------------------------------")
print("\n \n \n \n \n")

