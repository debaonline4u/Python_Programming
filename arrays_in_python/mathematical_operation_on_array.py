# Program to perform some mathematical operations on numpy arrays.

from numpy import *

arr = array([10, 20, 30, 40, 78, 25, 12, 5])
print('Original Array: ', arr)

# Arithmetic operations on the elements of the array.

print('After adding 5: ', arr+5)
print('After subtracting 5: ', arr-5)
print('After multiplying array elements: ', prod(arr))
print('After adding array elements: ', sum(arr))
print('Smallest element in the array: ', min(arr))
print('Index of smallest element: ', argmin(arr))
print('Biggest element in the array: ', max(arr))
print('Index of biggest element of the array: ', argmax(arr))
print('Array after sorting: ')
arr = sort(arr)
# print(sort(arr))
print(arr)
