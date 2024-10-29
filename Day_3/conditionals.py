"""
The if statemenet
"""

# numbers = 6
# if numbers>5:
#     print("this number", numbers, "is greater than 5")
    
"""
The if-else statement
"""

# numbers = 2
# if numbers>5:
#     print("this number", numbers, "is greater than 5")
    
# else:
#     print("the number is less than 5")
    
# numbers =[2,3,4,5,6,7,8,9]
# for number in numbers:
#     if number%2 ==0:   #This is the definition of an even number
#         print("This number", number, "is an even number")
#     else:
#         print(number, "is not an odd number")

"""
if-elif-else statement
"""
# numbers =[2,4,5,8,6,3,10,30,100]
# for number in numbers:
#     if number ==2:
#         print (f"{number} is 2")
#     elif number > 10:
#         print(f"{number} is greater than 10")
#     elif number >5:
#         print(f"{number} is greater than 5")
#     else:
#         print(f"{number}") #this will print if the above three conditions are not true (a catch all condition)
        
"""The above code could be made simplier by using a Nested if-else Statement"""
# numbers =[2,4,5,8,6,3,10,30,100]
# for number in numbers:
#     if number ==2:
#         print (f"{number} is 2")
#     if number > 5:
#         if number > 10:
#             print(f"{number} is greater than 10")
#         else:
#             print(f"{number} is greater than 5")
#     else:
#         print(f"{number} is not greater than 5")
        
"""The use of nested for loops"""
# numbers = [[1,2,3,4], [4,2,1]]
# print(numbers[1])
# for number_list in numbers:
#     print (number_list)

# numbers = [[1,2,3,4], [4,2,1]]
# for number_list in numbers:
#     for number in number_list:
#         print(number)