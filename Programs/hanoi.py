
def TOH(src,dest,help,n):
    if(n == 0):
        return
    TOH(src,help,dest,n-1)
    print("Move  ", src, " to ", dest, "  With the help of helper")
    TOH(help,dest,src,n-1)
    
print(TOH("A","B","C",3))
'''
Move   A  to  B   With the help of helper
Move   A  to  C   With the help of helper
Move   B  to  C   With the help of helper
Move   A  to  B   With the help of helper
Move   C  to  A   With the help of helper
Move   C  to  B   With the help of helper
Move   A  to  B   With the help of helper

'''