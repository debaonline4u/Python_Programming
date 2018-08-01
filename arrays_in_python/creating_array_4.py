# creating array from another array


from array import *

arr1 = array('d', [1.3, 2.3, -6.8, 9.809, 3.4554])

arr2 = array(arr1.typecode, (a for a in arr1))  # arr1 content is copied to arr2
print('array elements from new array is: ')

n = len(arr2)
# for i in range(n):
#     print(arr2[i], ' ')

i = 0
while i < n:            # accessing array element using while loop
    print(arr2[i])
    i += 1
