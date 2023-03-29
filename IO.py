s = "Aryan is the best adn electrifying "

'''
Will create a text file having name text and string s will be stored in that text file
with open("test.txt","w") as f :
    f.write(s)
''' 
# shortcut for writing above lines of code
fp = open("test1.txt","w") # will create test1.txt file
fp.write(s) # will write the string s in test1

# to close
fp.close() # by default automatically closes the file

# Reading File -> simply change 'w' to 'r'

'''
Will create a text file having name text and string s will be stored in that text file
with open("test.txt","r") as f :
    f.readt(s)

''' 
# fp is just a variable name
# shortcut for writing above lines of code
fp = open("test1.txt","r") # will create test1.txt file
fp.read(s) # will write the string s in test1
