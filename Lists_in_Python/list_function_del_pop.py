# Python code to demonstrate the working of
# del and pop()
 
# initializing list 
lis = [2, 1, 3, 5, 4, 3, 8]
 
# using del to delete elements from pos. 2 to 5
# deletes 3,5,4
del lis[2 : 5]
 
# displaying list after deleting 
print ("List elements after deleting are : ",end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using pop() to delete element at pos 2
# deletes 3
lis.pop(2)
 
# displaying list after popping  
print ("List elements after popping are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")