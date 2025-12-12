#create an array of number 1 to 20 using np.arange()
# shape, size, datatype

import numpy as np

arr = np.arange(1, 21)

print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Datatype:", arr.dtype)


# 3x3 random number 10 to 50 
# maximum, minimum, mean=average
# no.random.randint(start,stop,(x,y))

import numpy as np

arr = np.random.randint(10, 51, (3, 3))

print("Array:\n", arr)

print("Maximum:", arr.max())
print("Minimum:", arr.min())
print("Mean:", arr.mean())
