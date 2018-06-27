#Program to demonstrate list in python --> list declaring and printing
L=[1,"Narendra"," Modi","21st June",12+45]
print(L)

# Adding more items to List. 
L.append(6)
print(L)

# Remove an item through POP
L.pop()

print(L)

#Printing any particular item. 
print("My First Name is: {} and Last Name: {}".format(str(L[1]),str(L[2])))