# Python code to demonstrate the working of
# insert() and remove()
 
# initializing list 
lis = [2, 1, 3, 5, 3, 8]
 
# using insert() to insert 4 at 3rd pos
lis.insert(3, 4)
 
# displaying list after inserting
print("List elements after inserting 4 are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using remove() to remove first occurrence of 3
# removes 3 at pos 2
lis.remove(3)
lis.remove(8) 
# displaying list after removing 
print ("List elements after removing are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
