#the input function is used to ask for the users input
# the input function always returms a string
#example write a program to calculate your pay

# rate = 10.0 
# hours = 10.0
# pay = rate * hours
# print("Pay:" , pay) # this is hard coding

# rate = input("Please enter your rate")
# print("Rate:  ",rate)
# hours = input("Please enter your hours")
# print(": ", hours)
# pay = rate * hours # the print function will always return a string
# print("Pay:" , pay) # so you need to convert to be able to multiple

#Type Conversion
"""
If you want to carry out any numerical operations with the input function
then you have to convert it because you cannot multiply two strings"""
#two ways to convert
# rate = input("Please enter your rate: ")
# rate = float(rate)
# print (type(rate))
# print("Rate: ", rate)  #preferable  with ease to understand

# #or 
# rate = float(input("Please enter your rate: "))
# print(type(rate))
# print("Rate:  ",rate) #not very clear to understand

# rate = input("Please enter your rate: ")
# rate = float(rate)
# print (type(rate))
# print("Rate: ", rate) 

# hours = input("Please enter your rate: ")
# hours = float(hours)
# print (type(hours))
# print("Rate: ", hours) 

# pay = hours * rate
# print ("Pay, Rate X Hours =: ", pay)

"""
Write a python code that takes the user's name , age and height as 
input and displays the information back to the user

"""
# name = input("Please provide your name:  ")
# print("My name is: ", name)

# age = input("Please enter your age: ")
# age = int(age)
# print("My age is: ", age)

# height = input("Please provide your height: ")
# height = float(height)
# print (" My height is: ", height, "feet")

"""Error Handling
There are three main types of errors in Python
-Synthax Errors
-Runtime errors
-Logical Errors"""
 #try and except example
 
try:
    name = input("Please provide your name:  ")
    print("My name is: ", name)

    age = input("Please enter your age: ")
    age = int(age)
    print("My age is: ", age)

    height = input("Please provide your height: ")
    height = float(height)
    print (" My height is: ", height, "feet")
except ValueError: 
    print("You enter an invalid value")
    print ("Try again")