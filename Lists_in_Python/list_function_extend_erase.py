# Python code to demonstrate the working of
# extend() and clear()
 
# initializing list 1
lis1 = [2, 1, 3, 5]
 
# initializing list 1
lis2 = [6, 4, 3]
 
# using extend() to add elements of lis2 in lis1
lis1.extend(lis2)
 
# displaying list after sorting
print ("List elements after extending are : ", end="")
for i in range(0, len(lis1)):
    print(lis1[i], end=" ")
     
print ("\r")
 
# using clear() to delete all lis1 contents
lis1.clear()
 
# displaying list after clearing
print ("List elements after clearing are : ", end="")
for i in range(0, len(lis1)):
    print(lis1[i], end=" ")