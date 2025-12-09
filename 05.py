#REPLACE
x="Hello"
y=x.replace('o','i')
print(y)

#STRING FORMAT
fname = "Rahul"
age ="20"
x=(f"My name is {fname} and my age is {age}")
print(x)

#ESCAPE CHARACTER
x="Hello \" World"
print(x)

#PYTHON BOOLEANS
x=4
y=5
print(x>y)
print(x==y)
print(x<y)

#quetion.1 add two string by using string format
name=input("enter your name")
age=input("enter your age")
text=f"my name is {name} and my age is {age}"
print(text)

#question.2 
x=int(input("enter your number"))
y=x % 2 == 0
print(y)

#OPERATORS
#AIRTHMETIC OPERATOR
x=5
y=10

print(x+y)
print(x-y)
print(x*y)
print(x%y)
print(x/y)
print(x**y)
print(x//y)

#COMPARISON OPERATOR
x=15
y=20

print(x==y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x!=y)

#ASSIGNMENT OPERATOR
x=10
print(x)

x+=5
print(x)

x-=5
print(x)

x*=5
print(x)

x/=5
print(x)

x%=5
print(x)

x**=5
print(x)

#LOGICAL OPERATOR
x=10
y=20

print(x>y and x<y)
print(x>y or x<y)
print(not(x>y and x<y))

#identifiers
x='a'
y="alok"
print(x in y)
print(x not in y)