# Python program to sort the array elements using bubble sort technique:


from array import *

# create an empty array

arr = array('i', [])

# store elements into array.

print('How many elements? ', end='')
n = int(input())

for i in range(n):
    print('Enter elements: ', end='')
    arr.append(int(input()))

print('Original Array: ', arr)

# Applying bubble sort:


for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print('Sorted array: ', arr)
