# Python code to demonstrate working of 
# replace()
 
str = "nerdsfornerds is for nerds"
 
str1 = "nerds"
str2 = "geeks"
 
# using replace() to replace str2 with str1 in str
# only changes 2 occurrences 
print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2)) 