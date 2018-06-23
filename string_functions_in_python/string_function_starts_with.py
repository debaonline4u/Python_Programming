# Python code to demonstrate working of 
# startswith() and endswith()
str = "geeksforgeeks"
str1 = "geek"
str2="gee3"
 
# using startswith() to find if str starts with str1
if    str.startswith(str1):
        print ("str begins with str1")
else :  print ("str does not begin with str1")
 
# using endswith() to find if str ends with str1
if str.startswith(str2):
       print ("str ends with str1")
else : print ("str does not end with str2")