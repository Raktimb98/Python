# import pyjokes
# jokes = pyjokes.get_joke()
# print(jokes)
# print("hello world")
# first_name = "Raktim"
# print(f"Hello {first_name}")
# student = False
# if student:
#     print("You are a student")
# else:
#     print("You are NOT a student")
# name = "Rob stark"
# age = 1000
# weight = 9.7
# warrior = True
# print(type(age))
# age = float(age)
# print(age)
# name = input("What is your name: ")
# age =int(input("What is your age: "))
# age +=1
# print(f"Happy Birthday {name}")
# print(f"Your turned {age} Today!")
#Rectangle calculation of an area
# length =float( input("Enter the length: "))
# width =float( input("Enter the width: "))
# area = length * width
# print(f"Your area is: {area}cm²")
#Shopping cart
# item = input("Which item do your want to buy ? :")
# quantity =int( input("How many do you want ? :"))
# price = float(input("What is the price ? : "))
# total = price * quantity
# print(f"You have to pay : {total} rupees")
#arithmetic
# import math
# radius = float(input("Enter your radius:"))
# circumference = 2*math.pi * radius
# print(f"circumference is :{circumference}")
#area of a circle
# import math
# r = float(input("Enter the radius of the circle:"))
# area = math.pi * r
# print(f"Your answer is:{area}")
#if else
# age =int(input("Enter your age:"))
# if age >= 18:
#     print("Your are an adult")
# elif age <0:
#     print("You have to born , first!")
# else:
#     print("You are not an adult!")
#Python calculator
# operator = input("Enter the operator(+,-,*,/):")
# num1 = float(input("Enter your first number:"))
# num2 = float(input("Enter your second number:"))
# if operator == '+':
#     answer = num1 + num2
#     print(f"Your ans is:{num1} + {num2}={answer}")
# elif operator == '-':
#     answer = num1 - num2
#     print(f"Your ans is:{num1} - {num2}={answer}")
# elif operator == '*':
#     answer = num1 * num2
#     print(f"Your ans is:{num1} * {num2}={answer}")
# elif operator == '/':
#     answer = num1 / num2
#     print(f"Your ans is:{num1} / {num2}={answer}")
# else:
#     print("Something went wrong!")
#conditional expressions
# num = 981
# print("Your have more time to explore the world"if num <100 else "You have to die")
# validate user input
# username = input("Enter your username:")
# length =len(username)
# has_digit = any(char.isdigit() for char in username)
# has_space = ' ' in username
# if length < 12 and has_digit and not has_space:
#     print("username is valid!")
# else:
#     if length > 12:
#         print("Username must not be longer than 12 characters!")
#     if not has_digit:
#         print("Username must contain at least one number!")
#     if has_space:
#         print("Username must not contain spaces!")
#Indexing
# debit_number = "5649-6546-6556-5454"
# print(debit_number)
# print(debit_number[0:4])
# print(debit_number[:4])
# print(debit_number[0:])

# Format Specifiers
# price1 = 3.14159
# price2 = 2.355
# price3 = 21212.674
# print(f"Price1 is {price1:+.2f}")
# print(f"Price2 is {price2:+010}")
# print(f"Price3 is {price3:+,.2f}")

# While loop
name = input("Enter your name:")
while name =="":
    print("You didn't enter your name")
    name = input("Enter your name:")
print(f"Hello {name}")
