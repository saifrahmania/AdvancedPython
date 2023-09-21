# This is a code
# variable
name = "John"
age = 25
# control structure
if age > 18:
    print("You are an adult")
# function
def greet(name):
    print("Hello, " + name + "!")
# call function
name = 'Saifur'
greet(name)
# statement:
x = 1
# expression:
5 * 5 + 3
# string
s = "Hello, World!"
# list
fruits = ["apple", "banana", "cherry"]
# tuple 
fruits = ("apple", "banana", "cherry")
# Dictionary
fruits = {"apple": "green", "banana": "yellow", "cherry": "red"}
# Slicing
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
print(fruits[:4])
print(fruits[2:])
print(fruits[-4:-1])
# Formatting
name = "John"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

# conditional statement:
random_number = 10
if random_number > 0:
    print("Number is positive")
else: 
    print("Number is negative")

# loop
for fruit in fruits:
    print(fruit)

# exception handling
try:
    x = int("foo")
except ValueError:
    print("Invalid input")

# modules and packages
import math
print(math.sqrt(25))

# file handling
file = open("file.txt", "w")
file.write("Hello, World!\n")
file.write("This is our new text file\n")
file.write("and this is another line.\n")
file.close()
file = open("file.txt", "r")
content = file.read()
print(content)
file.close()
# decorator
import time 
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time: {}".format(end - start))
        return result
    return wrapper
@timer
def my_function():
    time.sleep(3)
my_function()


# data types
# int
x = 5
y = 3.14
z = 3 + 4j

# string
s = "Hello, World!"
s = 'Hello World!'

# list
numbers = [1, 2, 3, 4, 5]
names = ["John","Mike","Sarah","Kate"]

# tuple
coordinate = (10, 20)
names = ("John","Mike","Sarah","Kate") 

# dictionary
ages = {"John": 25, "Mike": 30, "Sarah": 28, "Kate": 32}
phone_numbers = {"John": "555-1234", "Mike": "555-5678", "Sarah": "555-8765", "Kate": "555-4321"}

# boolean
x = True
y = False

# None
x = None

# Sets and Bytes
# set
fruits.append("grapes")
print(fruits)
fruits.remove("apple")
print(fruits)

# bytes
data = b"Hello, World!"
print(data)
print(type(data))

data = bytearray(b"Hello, World!")
print(data)

# Basic Operators with Variables
# Assign a value to a variable

x = 5
y = 3.14
print(x)
print(y)

# Arithmetic operators
z = 3 + 4j
print(x, y, z)

# Comparison operators
if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")

# Comparison operators
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
