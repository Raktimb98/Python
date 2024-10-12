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
# name = input("Enter your name:")
# while name =="":
#     print("You didn't enter your name")
#     name = input("Enter your name:")
# print(f"Hello {name}")

# Short program
# exercise = input ("Enter your favorite exercise name (Press q for quit):")
# while not exercise == "q":
#     print(f"Your favorite exercise is: {exercise}")
#     exercise = input("Enter your another favorite exercise name: (Press q for quit):")
# print ("See you again boi !")

#Another one
# num = int(input("Enter a number between 1 to 10:"))
# while num < 1 or num > 10:
#     print(f"{num} is invalid")
#     num = int(input("Enter a number between 1 to 10:"))
# print (f"Your number is: {num}")

#Compound interest calculator
# principle = 0
# rate = 0
# time = 0
# principle = float(input("Enter the principle amount:"))
# while principle <= 0 :
#     principle = float(input("Enter the principle amount:"))
#     if principle <=0:
#         print("Principle can't be negative or zero !")

# rate = float(input("Enter the rate amount:"))
# while rate <= 0 :
#     rate = float(input("Enter the rate amount:"))
#     if rate <=0:
#         print("rate can't be negative or zero !")

# time = int(input("Enter the time in years:"))
# while time <= 0 :
#     time = int(input("Enter the time in years:"))
#     if time <=0:
#         print("time can't be negative or zero !")

# total = principle * pow((1+rate/100),time)
# print(f"Total amount after {time} years is: {total:.2f}")

#For loops
# for n in range(0,11):
#     print(n)
# print("Hello youth")

# for x in reversed(range(0,11)):
#     print(x)

# customer_id="154984-854-89498-84-56445"
# for x in customer_id:
#     print(x)

#Countdown timer
# import time
# time.sleep(3)
# print("Time's up")

# My_time = int(input("Enter you time in second:"))
# while My_time < 0:
#     print("Enter a valid time!")
#     My_time = int(input("Enter you time in second:"))
# for x in range(My_time,0,-1):
#     second = x % 60
#     minutes =int (x / 60) %60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{second:02}")
#     time.sleep(1)
# print("Time's up")

#Nested Loop
# for x in range(3):
#     for y in range(1,10):
#         print(y,end=" ")
#     print()

#Rectangle 
# symbol = input("Enter your symbol:")
# rows = int(input("How many rows do you want:"))
# while rows <= 0:
#     rows = int(input("Enter a valid positive number:"))
# column = int(input("How many columns do you want:"))
# while column <= 0:
#     column = int(input("Enter a valid positive number:"))
# for x in range(rows):
#     for y in range(column):
    #     print(symbol,end=" ")
    # print()

#collection, list , sets and tuples
fruit = "Mango"
fruit_list = ["Apple","Banana","Cherry"]
# print(fruit)
# print(fruit_list[2])
# fruit_list[0] ='mango'
fruit_list.append('Mango')
# fruit_list.remove('Banana')
# fruit_list.insert(1,'Litchi')
fruit_list.sort
for fruits in fruit_list:
    print(fruits)