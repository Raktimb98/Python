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

#if else
# age =int(input("Enter your age:"))
# if age >= 18:
#     print("Your are an adult")
# elif age <0:
#     print("You have to born , first!")
# else:
#     print("You are not an adult!")

#conditional expressions
# num = 981
# print("Your have more time to explore the world"if num <100 else "You have to die")

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

#collection, list , sets and tuples
# fruit = "Mango"
# fruit_list = ["Apple","Banana","Cherry"]
# print(fruit)
# print(fruit_list[2])
# fruit_list[0] ='mango'
# fruit_list.append('Mango')
# fruit_list.remove('Banana')
# fruit_list.insert(1,'Litchi')
# fruit_list.sort
# for fruits in fruit_list:
#     print(fruits)

#set
# car = {"Tata","Mahindra","Toyota","Volkswagen","BMW"}
# print(dir(car))
# print(car.add("Honda"))
# print(car.remove("BMW"))
# print(car)

#Tuples
# my_tuple = ("1","2","3","3","3","4","5")
# print(my_tuple[0])
# print(my_tuple.count("3"))
# print(my_tuple)
# for items in my_tuple:
#     print(items)