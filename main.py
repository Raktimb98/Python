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

#* if else
# age =int(input("Enter your age:"))
# if age >= 18:
#     print("Your are an adult")
# elif age <0:
#     print("You have to born , first!")
# else:
#     print("You are not an adult!")

#* conditional expressions
# num = 981
# print("Your have more time to explore the world"if num <100 else "You have to die")

#* Indexing
# debit_number = "5649-6546-6556-5454"
# print(debit_number)
# print(debit_number[0:4])
# print(debit_number[:4])
# print(debit_number[0:])

#* Format Specifiers
# price1 = 3.14159
# price2 = 2.355
# price3 = 21212.674
# print(f"Price1 is {price1:+.2f}")
# print(f"Price2 is {price2:+010}")
# print(f"Price3 is {price3:+,.2f}")

#* While loop
# name = input("Enter your name:")
# while name =="":
#     print("You didn't enter your name")
#     name = input("Enter your name:")
# print(f"Hello {name}")

#* Short program
# exercise = input ("Enter your favorite exercise name (Press q for quit):")
# while not exercise == "q":
#     print(f"Your favorite exercise is: {exercise}")
#     exercise = input("Enter your another favorite exercise name: (Press q for quit):")
# print ("See you again boi !")

#* Another one
# num = int(input("Enter a number between 1 to 10:"))
# while num < 1 or num > 10:
#     print(f"{num} is invalid")
#     num = int(input("Enter a number between 1 to 10:"))
# print (f"Your number is: {num}")

#* For loops
# for n in range(0,11):
#     print(n)
# print("Hello youth")

# for x in reversed(range(0,11)):
#     print(x)

# customer_id="154984-854-89498-84-56445"
# for x in customer_id:
#     print(x)

#* Nested Loop
# for x in range(3):
#     for y in range(1,10):
#         print(y,end=" ")
#     print()

#* collection, list , sets and tuples
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

#* set
# car = {"Tata","Mahindra","Toyota","Volkswagen","BMW"}
# print(dir(car))
# print(car.add("Honda"))
# print(car.remove("BMW"))
# print(car)

#* Tuples
# my_tuple = ("1","2","3","3","3","4","5")
# print(my_tuple[0])
# print(my_tuple.count("3"))
# print(my_tuple)
# for items in my_tuple:
#     print(items)

#* 2D array
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
#* for collections in favorite_things:
    # for items in collections:
        # print(items,end = " ")
    # print()

#* num pad
# num_pad = [(1,2,3),(4,5,6),(7,8,9),("*",0,"#")]
# for rows in num_pad:
#     for items in rows:
#         print(items,end = " ")
#     print()

#* Dictionaries
# student = {"Ram":"marks-95","Sham":"marks- 54","Jodu":"marks-34","yash":"marks-100"}
# print(student.get("Jodu"))
# student.update({"ayesha":"marks-99"})
# print(student.get("ayesha"))

#* Random module
# import random
# # print(help(random))
# # low = 1
# # high = 1000
# # number = random.randint(low ,high)
# options = ("Rock" , "Paper" , "Scissor")
# option = random.choice(options)
# print(option)

#* Functions
# def doIt():
#     print("do it")
#     print("Just do it")
#     print("You have to do it")
# doIt()
# def hello(name):
#     # "name" is a parameter here
#     print(f"Hello {name}")
# hello("Raktim")

#* Return statement
# def add(x,y):
#     ans = x+y
#     return ans
# print(add(5,6))

#* Function to create fullname
# def create_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
# full_name =create_name("raktim" , "biswas")
# print(full_name)

#* Default arguments
# def net_price(item_price,discount= 0,tax=0.05):
#     return item_price * (1-discount) * (1+tax)
# print(net_price(500,0.1,0))

#* Timer program using default
# import time
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
# count(10)

#* Keyword
# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")
# hello(greeting="Hello",first="Raktim",last="Biswas",title="Mr.")
# Get Phone number
# def get_phone(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"
# phone_number = get_phone(country=91,area=123,first=456,last=7890)
# print(phone_number)

#* Arbitrary
# def add(*nums):
#     total = 0
#     for arg in nums:
#         total +=arg
#     return total
# print(add(1,2,3))
# Another example
# def display_name(*args):
#     for arg in args:
#         print(arg,end=" ")
# display_name("Mr.","Raktim ","Biswas")
#* Kwargs
# def print_address(**kwargs):
#     # for value in kwargs.values():
#     # for key in kwargs.keys():
#     #     print(key)
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
# print_address(street="asdf123",city="Jaipur",state="New Delhi",pin=6541521)

#* Using args and kwargs together
# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg,end=" ")
#     print()
#     # for value in kwargs.values():
#     #     print(value, end=" ")
#     print(f"{kwargs.get('apt')} {kwargs.get('state')}")
# shipping_label("Mr.","Raktim","Biswas" ,apt="45",state="gtx store")

#* Iterables
# numbers = [1,2,3,4,5] #this is list
# numbers = (1,2,3,4,5) #this is tuple
# for number in numbers:
#     print(number, end=" ")

# foods = {"Chicken satay","Butter nun","panner tikka masala"}
# for items in foods:
#     print(items)

# options = {"A":1,"B":2,"C":3}
# # for key in options:
# # for values in options.values():
# for key,values in options.items():
#     # print(key,values , end=" ")
#     print(f"{key} : {values}")

#* Membership operators
# students = {"Adam","Eve","Martha","Katherina"}
# student = input("Enter the student name that you want to eliminate: ")
# if student in students:
#     print(f"{student} is eliminated!")
# else:
#     print(f"{student} was not found in the list.")

#* List comprehension
# doubles = []
# for n in range(1,11):
#     doubles.append(n*2)
# print(doubles)

# doubles =[value*2 for value in range(1,11)]
# print(doubles)

#* Match-case statement (switch case)
# def day_of_week(day):
#     if day ==1:
#         return "It's sunday"
#     elif day ==2:
#         return "It's monday"
#     elif day ==3:
#         return "It's tuesday"
#     elif day ==4:
#         return "It's wednesday"
#     elif day ==5:
#         return "It's thursday"
#     elif day ==6:
#         return "It's friday"
#     elif day ==7:
#         return "It's saturday"
#     else:
#         return "Invalid day"

# print(day_of_week(1))

#* It's the actual implementation of switch case(down below)
# def day_of_week(day):
#     match day:
#         case 1:
#             return "It's sunday"
#         case 2:
#             return "It's monday"
#         case 3:
#             return "It's tuesday"
#         case 4:
#             return "It's wednesday"
#         case 5:
#             return "It's thursday"
#         case 6:
#             return "It's friday"
#         case 7:
#             return "It's saturday"
#         case _:
#             return "Invalid day"
        
# print(day_of_week(1))

#* Module
# help("modules")
# import math
# print(math.pi)
# import math as m
# print(m.pi)
# the 'pi' is from the math module
#from math import pi
#print(pi)

#* Scope resolution
#* (LEGB) Local -> Enclosed -> Global -> Built in

#* Example of Local scope
# def func1():
#     x = 1 #local
#     print(x)

# def func2():
#     x = 2 #local
#     print(x)

# func1()
# func2()
# # Example of Enclosed scope
# def outer():
#     x = 1 #enclosed
#     def inner():
#         print(x)
#     inner()

# # Example of Global scope
# x = 1 #global
# def func():
#     print(x)
# func()

#* Example of Built in scope
# from math import pi
# def func():
#     print(pi)
# func()

# if __name__ == "__main__":(This is used to run the code only when the file is run directly)

# def main():
#     print("Hello world")
# if __name__ == "__main__":
#     main()

# from __name__ import *
# print(__name__)
# # Another part of the code
# def favorite_food(food):
#     print(f"Your favorite food is {food}")

# def main():
#     print("This is main page")
#     favorite_food("Chicken Satay")

# if __name__ == "__main__":
#     main()


#* Date and time
# import datetime
# date = datetime.date(2025,8,18)
# today = datetime.date.today()
# now = datetime.datetime.now()
# now = now.strftime("%H:%M:%S %d/%m/%Y")
# print(now)
# print(today)
# print(date)

# target_datetime = datetime.datetime(2025,8,18,12,0,0)
# current_datetime = datetime.datetime.now()

# if current_datetime > target_datetime:
#     print("Target date has passed")
# elif current_datetime < target_datetime:
#     print("Target date is yet to come")
# else:
#     print("Target date is today")

#* Multithreading

# import threading
# import time

# def walk_dog(name):
#     time.sleep(8)
#     print(f"You are walking the {name}")

# def take_out_trash():
#     time.sleep(2)
#     print("You are taking out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You are getting the mail")

# chore1 = threading.Thread(target=walk_dog, args=("dog",))
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are done")

#* How to connect to an API

# import requests
# base_url = "https://pokeapi.co/api/v2"

# def get_pokemon_info(pokemon_name):
#     url = f"{base_url}/pokemon/{pokemon_name.lower()}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         name = data['name']
#         height = data['height']
#         weight = data['weight']
#         types = [type_info['type']['name'] for type_info in data['types']]
        
#         print(f"Name: {name.capitalize()}")
#         print(f"Height: {height}")
#         print(f"Weight: {weight}")
#         print(f"Types: {', '.join(types).capitalize()}")
#     elif response.status_code == 404:
#         print(f"Pokemon '{pokemon_name}' not found.")
#     elif response.status_code == 500:
#         print("Server error. Please try again later.")
#     else:
#         print(f"Failed to retrieve data for {pokemon_name}. Status code: {response.status_code}")
#         return

# pokemon_name = input("Enter the name of the Pokemon: ")
# get_pokemon_info(pokemon_name)

#* PyQt5 introduction
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
# from PyQt5.QtGui import QIcon ,QFont , QPixmap
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Python GUI")
#         # self.setGeometry(x,y,width,height)
#         self.setGeometry(500, 250, 500, 300)
#         self.setWindowIcon(QIcon("E:\Programming\Python\image.jpg"))

#         # label = QLabel("Hello, from PyQt5!",self)
#         # label.setFont(QFont("Arial", 20))
#         # label.setStyleSheet("color: blue;" "background-color: yellow;")
#         # label.setGeometry(50, 50, 400, 50)
#         # label.setAlignment(Qt.AlignCenter)
#         # label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

#         # Adding an image
#         label = QLabel(self)
#         label.setGeometry(0, 0, 500, 300)
#         pixmap = QPixmap("E:\Programming\Python\image.jpg")
#         label.setPixmap(pixmap)
#         label.setScaledContents(True)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()

#* PyQt5 layouts
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout,QGridLayout

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500, 250, 500, 300)
#         self.initUI()

#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         label1 = QLabel("Label 1", self)
#         label2 = QLabel("Label 2", self)
#         label3 = QLabel("Label 3", self)
#         label4 = QLabel("Label 4", self)
#         label5 = QLabel("Label 5", self)

#         label1.setStyleSheet("background-color: red;")
#         label2.setStyleSheet("background-color: green;")
#         label3.setStyleSheet("background-color: blue;")
#         label4.setStyleSheet("background-color: yellow;")
#         label5.setStyleSheet("background-color: orange;")

#         # vbox = QVBoxLayout()
#         # vbox.addWidget(label1)
#         # vbox.addWidget(label2)
#         # vbox.addWidget(label3)
#         # vbox.addWidget(label4)
#         # vbox.addWidget(label5)
#         # central_widget.setLayout(vbox)

#         # hbox = QHBoxLayout()
#         # hbox.addWidget(label1)
#         # hbox.addWidget(label2)
#         # hbox.addWidget(label3)
#         # hbox.addWidget(label4)
#         # hbox.addWidget(label5)
#         # central_widget.setLayout(hbox)

#         grid = QGridLayout()
#         grid.addWidget(label1, 0, 0)
#         grid.addWidget(label2, 0, 1)
#         grid.addWidget(label3, 1, 0)
#         grid.addWidget(label4, 1, 1)
#         grid.addWidget(label5, 2, 0, 1, 2)
#         central_widget.setLayout(grid)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.setWindowTitle("Python GUI")
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()

#* PyQt5 Buttons
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500, 250, 500, 300)
#         self.button = QPushButton("Click Me", self)
#         self.InitUI()

#     def InitUI(self):
#         self.button.setGeometry(50, 50, 100, 30)
#         self.button.setStyleSheet("background-color: green; color: white; font-size: 16px;")
#         self.button.clicked.connect(self.on_click)

#     def on_click(self):
#         print   ("Button clicked")
#         self.button.setText("Clicked")
#         self.button.setDisabled(True)
# if __name__ == "__main__":
#     app = QApplication(sys.argv) 
#     window = MainWindow()
#     window.setWindowTitle("Python GUI")
#     window.show()
#     sys.exit(app.exec_())

#* PyQt5 Checkbox
# import sys
# from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500, 250,500,300)
#         self.checkbox = QCheckBox("Check me",self)
#         self.initUI()

#     def initUI(self):
#         self.checkbox.setStyleSheet("font-size: 20px;" "font-family: Poppins;")
#         self.checkbox.setGeometry(50,50,200,30)
#         # self.checkbox.setChecked(True) # Check the checkbox by default
#         self.checkbox.stateChanged.connect(self.checkbox_changed)
#     def checkbox_changed(self,state):
#         if state == Qt.Checked:
#             print("Checkbox is checked")
#         else:
#             print("Checkbox is unchecked")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.setWindowTitle("Python GUI")
#     window.show()
#     sys.exit(app.exec_())

#* PyQt5 Radio button
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QLabel

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500, 250, 500, 300)
#         self.setWindowTitle("Python GUI")

#         self.radio1 = QRadioButton("Rupay", self)
#         self.radio2 = QRadioButton("Visa", self)
#         self.radio3 = QRadioButton("Mastercard", self)
#         self.radio4 = QRadioButton("Cash", self)
#         self.radio5 = QRadioButton("Cheque", self)

#         self.button_group_1 = QButtonGroup(self)
#         self.button_group_2 = QButtonGroup(self)

#         self.label = QLabel("", self)
#         self.label.setGeometry(50, 200, 400, 40)

#         self.initUI()

#     def initUI(self):
#         self.radio1.setGeometry(50, 50, 150, 30)
#         self.radio2.setGeometry(50, 80, 150, 30)
#         self.radio3.setGeometry(50, 110, 150, 30)
#         self.radio4.setGeometry(50, 140, 150, 30)
#         self.radio5.setGeometry(50, 170, 150, 30)

#         self.setStyleSheet("font-size: 20px; font-family: Poppins;")

#         self.button_group_1.addButton(self.radio1)
#         self.button_group_1.addButton(self.radio2)
#         self.button_group_1.addButton(self.radio3)

#         self.button_group_2.addButton(self.radio4)
#         self.button_group_2.addButton(self.radio5)

#         # Connect radio buttons to the handler
#         for btn in self.button_group_1.buttons():
#             btn.toggled.connect(self.radio_changed)
#         for btn in self.button_group_2.buttons():
#             btn.toggled.connect(self.radio_changed)

#     def radio_changed(self):
#         selected_1 = next((btn.text() for btn in self.button_group_1.buttons() if btn.isChecked()), None)
#         selected_2 = next((btn.text() for btn in self.button_group_2.buttons() if btn.isChecked()), None)
#         self.label.setText(f"Group 1: {selected_1 or 'None'} | Group 2: {selected_2 or 'None'}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

#* PyQt5 Line edit
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit ,QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500, 250, 500, 300)
#         self.line_edit = QLineEdit(self)
#         self.button = QPushButton("Submit", self)
#         self.initUI()

#     def initUI(self):
#         self.line_edit.setGeometry(50, 50, 200, 30)
#         self.button.setGeometry(50, 100, 100, 30)
#         self.line_edit.setPlaceholderText("Enter your name")
#         self.line_edit.setStyleSheet("font-size: 20px; font-family: Poppins;")
#         self.button.setStyleSheet("font-size: 20px; font-family: Poppins;")
#         self.line_edit.setMaxLength(10)
#         self.button.clicked.connect(self.submit)

#     def submit(self):
#         text = self.line_edit.text()
#         print(f"Submitted text: {text}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.setWindowTitle("Python GUI")
#     window.show()
#     sys.exit(app.exec_())

#* PyQt5 CSS Styles
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class ColorfulButtonsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Three Colorful Buttons with Hover Effects")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Red Button
        self.red_button = QPushButton("Red")
        self.red_button.setStyleSheet("""
            QPushButton {
                background-color: #E53935;
                color: white;
                border-radius: 10px;
                font: bold 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF6659;
                color: #212121;
            }
        """)

        # Yellow Button
        self.yellow_button = QPushButton("Yellow")
        self.yellow_button.setStyleSheet("""
            QPushButton {
                background-color: #FFEB3B;
                color: #212121;
                border-radius: 10px;
                font: bold 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FFF176;
                color: #E53935;
            }
        """)

        # Green Button
        self.green_button = QPushButton("Green")
        self.green_button.setStyleSheet("""
            QPushButton {
                background-color: #43A047;
                color: white;
                border-radius: 10px;
                font: bold 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #66BB6A;
                color: #212121;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.red_button)
        layout.addWidget(self.yellow_button)
        layout.addWidget(self.green_button)
        central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorfulButtonsApp()
    window.show()
    sys.exit(app.exec_())
