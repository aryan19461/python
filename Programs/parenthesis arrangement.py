def parent(si,ei,n,ans,list):
    if(si==n and ei==n):
        list.append(ans)
    
    if(si < n):
        parent(si+1,ei,n,ans + "{",list)
    if(si > ei):
        parent(si,ei+1,n,ans + "}",list)
    
list = []
parent(0,0,3," ",list)    
print(list)
'''
[' {{{}}}', ' {{}{}}', ' {{}}{}', ' {}{{}}', ' {}{}{}']

'''