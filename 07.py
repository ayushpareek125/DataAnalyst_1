#MATCH
num = int(input("enter your number"))
match num :
    case a if 0<= a <=20:
        print("less")
    case b if b == 25:
        print("winner")
    case _:
        print("invalid")
        
#LOOP
# A.WHILE LOOP
# 01.TO PRINT COUNTING 1 TO 10
start = 1
while(start <= 10):
    print(start)
    start += 1     

# 02.TO PRINT THE ODD NUMBERS(1,,3,5,7)
start = 1
while(start <= 10):
    print(start)
    start += 2    

# 03.TO PRINT THE SUM OF 1 TO 10
start = 1
sum = 0
while(start <= 10):
    sum=sum+start
    start += 1
print(sum)        

# 04.TO PRINT THE LENGTH OF A STRING
text = ("Hello world")
start = 0
while(start<(len(text))):
    print(text[start])
    start += 1

# 05.TO PRINT THE COUNT OF A CHARCTER IN A STRING  
text = "Hello world"
count = 0
i = 0
while(i<len(text)):
    if text [i] == 'l':
        count += 1
    i += 1
print(count)          

# 06.TAKE A NAME OR CHARACTER FROM USER AND PRINT THE COUNT OF CHARACTER WHICH USER GIVES
text = input("enter your name")
char = input("enter your character")
count = 0
i = 0
while(i<len(text)):
    if text[i] == char:
        count += 1
    i += 1
print(count)        

# 07.TO PRINT THE SUM OF EVEN NUMBERS
start = 0
sum = 0
while(start <= 10):
    sum = sum + start
    start += 2
print(sum)    

# 08.PRINT EVEN NUMBERS
s = 1
while(s <= 10):
    if s % 2 == 0:
        print(s)
    s += 1    

# 09.TO PRINT THE EVEN NUMBERS AND ITS SUM
sum = 0
s = 1
while(s <= 10):
    if (s % 2 == 0):
        print(s)
        sum += s
    s += 1
print(sum)        