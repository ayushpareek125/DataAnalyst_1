# FUNCTION
num_1 = int(input("enter your number"))
num_2 = int(input("enter your number"))
def add (a,b):
    print(a+b)

add(num_1,num_2)    

# return
def add (a,b):
    return a+b
result = add(10,20)
print(result)

#default parameters
def details(name="ravi",age=0):
    print(name)
    print(age)
details()    
details("alok",1)
details("alok")

#lambda function
add = lambda a,b : a+b
result = add(10,6)
print(result)

'''Question.def test(a,b)
       return a if a>b else b
       print(test(test(2,5),test(10,3)))'''

def test(a,b):
    if a>b:
        return a
    else:
        return b    
test_1= test(2,5)
print(test_1)

test_2 = test(10,3)
print(test_2)

test_3 = test(test_1,test_2)
print(test_3)