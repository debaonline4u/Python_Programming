# Python code to demonstrate the working of
# "+" and "*"
# initializing list 1
lis = [1, 2, 3]
 
# initializing list 2
lis1 = [4, 5, 6]
 
# using "+" to concatenate lists
lis2= lis + lis1
 
# priting concatenated lists
print ("list after concatenation is : ", end="")
for i in range(0,len(lis2)):
         print (lis2[i], end=" ")
          
print ("\r")
 
#using '*' to combine lists 
lis3 = lis * 3
 
# priting combined lists
print ("list after combining is : ", end="")
for i in range(0,len(lis3)):
         print (lis3[i], end=" ")