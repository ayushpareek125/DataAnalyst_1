#CONDITIONAL OPERATOR
# 1.IF
age=19
if age >= 18:
    print("you can drive")

# 2.IF ELSE
age = 17
if age >= 18:
    print("you can drive")
else:
    print("you cannot drive")   

# 3.IF ELIF ELSE
day=int(input("enter your number betwwen 1 to 7"))
if day == 1:
    print("sunday")
elif day == 2:
    print("monday")
elif day == 3:
    print("tuesday")
elif day == 4:
    print("wednesday")
elif day == 5:
    print("thursday")
elif day == 6:
    print("friday")
elif day == 7:
    print("saturday")
else:
    print("invalid number")                 

# AND,OR,NOT in conditional operator
age = 17
name = "Harsh"
if (age >= 18 or name[0] == 'H'):
    print("yes")
else:
    print("NO")    

#QUESTIONS
#1.print months name by using if elif else
month=int(input("enter your number"))
if month == 1:
    print("january")

elif month == 2:
    print("febuary")

elif month == 3:
    print("march")
            
elif month == 4:
    print("april")
            
elif month == 5:
    print("may")
            
elif month == 6:
    print("june")
            
elif month == 7:
    print("july")
            
elif month == 8:
    print("august")
            
elif month == 9:
    print("september")
            
elif month == 10:
    print("october")
            
elif month == 11:
    print("november")
            
elif month == 12:
    print("december")

else:
    print("invalid number")    

#2.if number is 25 print winner otherwise print looser
number=int(input("enter your number"))
if(number == 25):
    print("winner")
else:
    print("looser")    

#3.if number between 0 to 24 print lesser ,if number is 25 print winner, if number between 26 to 50 print greater, otherwise invalid number    
number=int(input("enter your number between 0 to 50"))         
if number == 25:
    print("winner")
elif number >= 0 and number <= 24:
    print("lesser")
elif number >= 26 and number <= 50:
    print("greater")
else:
    print("invalid number")         

#4.if number is 25 print winner if number between 0 to 20 print lesser ,if number between 21 to 24 print near to win but lesser
# if number between 26 to 30 print near to win but greater ,if number between 31 to 50 print greatest,otherwise invalid number          
number=int(input("enter a number between 0 to 50"))
if number >= 0 and number <= 20:
    print("lesser")

elif number >= 21 and number <= 24:
    print("near to win but lesser")

elif number == 25:
    print("winner")

elif number >= 26 and number <= 30:
    print("near to win,greater")

elif number >= 31 and number <=50:
    print("greatest")

else:
    print("please enter a valid number")     