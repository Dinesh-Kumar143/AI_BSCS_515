# Task 1: Introduction
# This Program converts Celsius to Fahrenheit or vice versa.
# It takes temp and units then convert it to other form.
# It uses the formula: Fahrenheit = (Celsius * 9/5) + 32
# It uses the formula: Celsius =  (Fahrenheit -32) * 5/9
# It prints the result to the screen

# Task 1
unit = int(input("Enter 1 for Celcius to Fahrenheit:\nEnter 2 for Fahrenheit to Celcius: ")) 
Temp = float(input("Enter Temperature: "))
if (unit == 1):
    F = (Temp * 9/5) + 32
    print("Celcius to Fahrenheit = ",F)
elif (unit == 2):
    C = (Temp -32) * 5/9
    print("Fahrenheit to Celcius = ",C)

else:
    print("Input Error!")
    
# Task 2: Terminal
# To run this program, you need to open a terminal and navigate to the folder where this file is saved
# Then, you need to type the following command: python celsius_to_fahrenheit.py
# This will execute the program and show the output


# Task 3: Python Interpreter
# Python is an interpreted language, which means that it runs the code line by line
# The Python interpreter is a program that reads and executes the Python code
# You can also use the Python interpreter interactively, by typing python in the terminal
# This will open a prompt where you can type and run Python commands

# Task 4: Variables
# Variables are names that store values in memory
# You can assign values to variables using the = operator
# You can use variables in expressions and print their values
# Variables can have different types, such as numbers, strings, booleans, lists, etc.

a = 45
b = 78
print('a/b = ',a/b)

# Task 5: Text Editor
# To write and edit Python code, you need a text editor
# A text editor is a program that allows you to create and modify text files
# There are many text editors available, such as Notepad, Sublime Text, VS Code, etc.
# You can choose any text editor that you like, as long as it can save files with the .py extension
# Like this file was also made from a txt file

# Task 6: Functions
# Functions are blocks of code that perform a specific task
# You can define your own functions using the def keyword
# You can call a function by using its name and passing arguments to it
# You can return a value from a function using the return keyword
# You can use built-in functions that are provided by Python, such as print, input, len, etc.
# Functions can be override in class.
# Functions can have no Paramter and works as defaut
# Functions can be overloaded by just changing number of parameters while having same name.

def Greeting():
    print("Good Moring.")
    return

Greeting()

# Task 7: Lists and Tuples
# Lists and tuples are data structures that store multiple values in a single variable
# Lists are mutable, which means that you can change their elements
# Tuples are immutable, which means that you cannot change their elements
# WE can create a list by using square brackets [] and a tuple by using parentheses ()
# WE can access the elements of a list or a tuple by using their index, starting from 0
# WE can use slicing to get a subsequence of a list or a tuple
# WE can use operators and methods to manipulate lists and tuples, such as +, *, append, pop, etc.

l = [1,2,3,4,5] # Suppose this is a list containing 5 elements 1,2,3,4,5
t = (1,2,3,4,5) # Suppose this is a tuple containing 5 elements 1,2,3,4,5

print(l[1:3]) # Here Slicing operator ' : ' is used  to divide a list or tuple according to our need.
print(t[2:4])


# Task 8: Conditional Statements
# Conditional statements are used to control the flow of the program based on some conditions
# The if statement executes a block of code if a condition is true
# The elif statement executes a block of code if a previous condition is false and another condition is true
# The else statement executes a block of code if all the previous conditions are false
# You can use logical operators and comparison operators to form complex conditions, such as and, or, not, ==, !=, <, >, etc.

a = 45
if (a >= 40):
    print("a is Greater than 40. ")
else :
    print("a is less than 40.")

# Task 9: The For Loop
# The for loop is used to iterate over a sequence, such as a list, a tuple, a string, or a range
# The for loop executes a block of code for each element in the sequence
# You can use the break statement to exit the loop prematurely
# You can use the continue statement to skip the current iteration and move to the next one
# You can use the else statement to execute a block of code after the loop ends normally

n = 20;
for i in range(n):
    if (i == 10):
        print("i is Skipped.")
        continue
    elif (i == 15):
        print('i reached 15 and can not go further!')
        break
    print('i= ',i)


# Task 10: User Input and the While Loop
# User input is used to get data from the user through the keyboard
# You can use the input function to prompt the user for input and return it as a string
# You can convert the input to other types, such as int, float, bool, etc.
# The while loop is used to repeat a block of code while a condition is true
# The while loop is useful when you don't know how many times you need to loop
# You can use the same statements as the for loop to control the while loop
