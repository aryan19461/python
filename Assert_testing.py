def sum(a,b) :
    return a+b
print(sum(2,3))

assert sum(2,3) == 5 # tesing 2,3, sum is 5

#assert sum(2,10) == 11 # tesing 2,10, sum is 11 but it will return eror- AssertionError

assert sum(-20,20) == 0
print("All function passed") #if all cases passed then it will print this print line other it will be stopped at case which is not passed




# Making cases for different operation

def multiply(a,b):
    return a*b

def test_cases():
    assert multiply(2,-3) == -6    
    assert multiply(2,3) == 6
    assert multiply(0,3) == 0
    assert multiply(0,0) == 0
    assert multiply(-2,-5) == 10
    print("All cases passed")

test_cases()