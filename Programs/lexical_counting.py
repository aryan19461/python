

def lexical(curr , UpperLimit, list):
    if(curr > UpperLimit):
        return
    i = 0
    if(curr == 0):
        i = 1
        
    list.append(curr)
    while(i < 9):
        lexical(curr*10+i, UpperLimit,list)
        i = i + 1
    
UL = 30
current = 0
list = []    
lexical(current, UL,list)
print(list)
  
'''
[0, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 3, 30, 4, 5, 6, 7, 8]

'''