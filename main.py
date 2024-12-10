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

# 2D array
# car_list = ["BMW","Audi","Toyota","Tata","Volkswagen"]
# food_list = ["Egg roll","Paneer tikka","Egg chicken roll","Chicken satay","Chicken 65"]
# computer_specification = ["H410M","i3 10105f","16GB","1TB","GT 710 ddr3"]
# favorite_things = [car_list,food_list,computer_specification]
# favorite_things = [["BMW","Audi","Toyota","Tata","Volkswagen"],
                #    ["Egg roll","Paneer tikka","Egg chicken roll","Chicken satay","Chicken 65"],
# ["H410M","i3 10105f","16GB","1TB","GT 710 ddr3"]]
# print(favorite_things[0][0])
# for collection in favorite_things :
#     print (collection)
# for collections in favorite_things:
    # for items in collections:
        # print(items,end = " ")
    # print()

#num pad
# num_pad = [(1,2,3),(4,5,6),(7,8,9),("*",0,"#")]
# for rows in num_pad:
#     for items in rows:
#         print(items,end = " ")
#     print()

#Dictionaries
# student = {"Ram":"marks-95","Sham":"marks- 54","Jodu":"marks-34","yash":"marks-100"}
# print(student.get("Jodu"))
# student.update({"ayesha":"marks-99"})
# print(student.get("ayesha"))

#Random module
# import random
# # print(help(random))
# # low = 1
# # high = 1000
# # number = random.randint(low ,high)
# options = ("Rock" , "Paper" , "Scissor")
# option = random.choice(options)
# print(option)

# Functions
# def doIt():
#     print("do it")
#     print("Just do it")
#     print("You have to do it")
# doIt()
# def hello(name):
#     # "name" is a parameter here
#     print(f"Hello {name}")
# hello("Raktim")

# Return statement
# def add(x,y):
#     ans = x+y
#     return ans
# print(add(5,6))

# Function to create fullname
# def create_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
# full_name =create_name("raktim" , "biswas")
# print(full_name)

# Default arguments
# def net_price(item_price,discount= 0,tax=0.05):
#     return item_price * (1-discount) * (1+tax)
# print(net_price(500,0.1,0))

# Timer program using default
# import time
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
# count(10)

# Keyword
def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")
hello(greeting="Hello",first="Raktim",last="Biswas",title="Mr.")