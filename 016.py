# mathematical and statical operations

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.min(arr,axis = 0))
print(np.min(arr,axis = 1))
print(np.mean(arr,axis = 0))
print(np.mean(arr,axis = 1))
print(np.max(arr,axis = 0))
print(np.max(arr,axis = 1))


#sum of coluns and row

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr1)

print(np.sum(arr1,axis=0))
print(np.sum(arr1,axis=1))

##Comulative function

arr3 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

#cumsum
print(np.cumsum(arr3))

#cumprod
print(np.cumprod(arr3))

#Rounding, floor, ceil
x = np.array([1.2437, 5.673256, 6.75355])
print(np.round(x,2))
print(np.floor(x))
print(np.ceil(x))


# #Normalisation

# x = [10,20,30,40,50,60,70,80,90,100]

# = x-np.main(x)\ np.max(x-np.main(x))


#concatenate
y = np.array([
    [1, 2],
    [3, 4]
])

z = np.array([
    [5, 6],
    [7, 8]
])
 
np.concatenate((y,z),axis=0)
np.concatenate((y,z),axis=1)

# Queation 
#1. math's average number
#2. student'1 max number
#3. student'4 min number
#4. average number of per student
#5. average number of per subject


marks = np.array([
    [45, 78, 56],   # student1
    [67, 82, 90],   # student2
    [58, 65, 70],   # student3
    [34, 55, 60],   # student4
    [76, 88, 97]    # student5
])

print("Marks Array:\n", marks)

#1. math's average number

maths_avg = marks[:, 0].mean()
print("Maths Average =", maths_avg)

#2. student'1 max number

s1_max = marks[0].max()
print("S1 Maximum Marks =", s1_max)

#3. student'4 min number

s4_min = marks[3].min()
print("S4 Minimum Marks =", s4_min)

#4. average number of per student

avg_per_student = marks.mean(axis=1)
print("Average per Student =", avg_per_student)

#5. average number of per subject

avg_per_subject = marks.mean(axis=0)
print("Average per Subject (Maths, English, Hindi) =", avg_per_subject)
















