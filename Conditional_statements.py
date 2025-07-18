#Conditional Statement syntax
#if-elif-else

"""if(condition):
    statement
elif(condition):
    statement2
else:
    statementN """       

#example
# light=input("Enter the signal colors:-")

# if(light=="red"):
#     print("stop")
# elif(light=="Green"):
#     print("go")
# elif(light=="yellow"):
#     print("look") 

#example 2
score=int(input("Enter your 12th percentage:-"))
if(score>=90):
     grade="A"    #spaces here below if is called as indentation in python
elif(90>score>=80):
    grade="B"
elif(80>score>=70):
    grade="C"
elif(70>score>=60):
    grade="D"
elif(60>score>=50):
    grade="E"
else:
    grade="F"    

print("THe grade of student is:-",grade)              

#example3
# num=int(input("Enter the number"))
# if(num>2):
#     print("Greater than 2")     #checks for only (if) if true
# elif(num>3):
#     print("Greater than 3")    #otherwise goes to elif if if is false

#Nesting in python
age=int(input("Enter the age:-"))
if(age>=18):
    if(age>=80):
        print("Cannot drive")
else:
    print("Cannot drive")
