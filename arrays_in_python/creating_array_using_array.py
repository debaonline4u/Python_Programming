# Python program to create a string type array using numpy array() method.


from numpy import *

arr = array(['Delhi', 'Mumbai', 'Hyderabad', 'Bengaluru', 'Bhubneswar', 'Baroda'])

# Creating an array from another array.

arr2 = array(arr)
arr3 = arr

# display the arrays:

print('arr = ', arr)
print('arr2 = ', arr2)
print('arr3 = ', arr3)

