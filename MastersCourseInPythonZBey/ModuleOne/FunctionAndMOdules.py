def add(x, y):
    return x + y

result = add(5, 10)
print(result)

import math 
print(math.sqrt(16))


try:
    print(math.sqrt(-16))
except ValueError:
    print("Invalid Value")
else:
    print("Valid Value")

try:
    number = 5 / 0
except ZeroDivisionError:
    print("Division by Zero")
else:
    print("Division Successful")

try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("File Not Found")
finally:
    print("File Found")
    file.close()


