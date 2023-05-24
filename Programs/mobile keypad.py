key = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def keypress(ques, ans, lst):
    if len(ques) == 0:
        lst.append(ans)
        return
    
    ch = ques[0]
    press = key[int(ch)]
    for i in range(len(press)):
        keypress(ques[1:], ans+press[i], lst)
        
lst = []
ques = "23"
keypress(ques, "", lst)
print(lst)
'''
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

'''