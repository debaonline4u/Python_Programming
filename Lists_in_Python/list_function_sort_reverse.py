# Python code to demonstrate the working of
# sort() and reverse()
 
# initializing list 
lis = [2, 1, 3, 5, 3, 8]
 
# using sort() to sort the list
lis.sort()
 
# displaying list after sorting
print ("List elements after sorting are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using reverse() to reverse the list
lis.reverse()
 
# displaying list after reversing
print ("List elements after reversing are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
