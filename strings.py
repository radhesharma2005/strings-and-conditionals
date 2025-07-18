# str1="This is a python program.\nwe welcome you to vs code"
# print(str1)

# #\n is a escape sequence character used write a statement in new line
# #\t creates tab space between sentences

# #Basic operations

# #Concatenation *Adding two or more strings like
# str1="hello"+"world"
# print(str1)
# print(len(str1)) #to find length of string

# #Addition of two string
# str1="Radheshyam"
# str2="Sharma"
# final_str=str1+" "+str2  #space between the strings is also count in length
# print(final_str) 
# print(len(final_str))  #17

# #indexing the string
# str="Radheshyam Sharma"
# ch=str[4]
# print(ch)

# #slicing
# str="Radheshyam"
# print(str[2:6]) #ending index is excluded
# print(str[:6])#str[0:6]
# print(str[6:])#str[6:len(str)] last index
# print(str[6:len(str)])
# print(str[-4:-1]) #for accessing using negative index

 #Strings Function
"""1)str.endswith("er")        #Returns true if string ends with substr
2)str.capitalize()             #capitalize 1st character
3)str.replace(old,new)         #replaces all occurence of old with new
4)str.find(word)               #returns 1st index of 1st occurence 
5)str.count("am")              #counts the occurence of substr in string"""

#Examples
str="i am studying python from ApnaCollege"
print(str.endswith("ege"))
print(str.capitalize())
print(str.replace("python","javascript"))
print(str.find("h"))
print(str.count("p"))

