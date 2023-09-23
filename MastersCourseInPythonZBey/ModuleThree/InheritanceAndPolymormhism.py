class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
    def drive(self):
        print("Driving")

class Car(Vehicle):
    def __init__(self, wheels, doors):
        self.doors = doors
        super().__init__(wheels)

    def honk(self):
        print("Beep! Beep!")

class Bike(Vehicle):
    def __init__(self, wheels, gears):
        self.gears = gears
        super().__init__(wheels)

    def honk(self):
        print("Ring! Ring!")

class Animals:
    def __init__(self):
        pass

    def speak(self):
        pass

class Dog(Animals):
    def speak(self):
        return "Woof!"
    
class Cat(Animals):
    def speak(self):
        return "Meow!"
    
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

def divide(numerator, denominator):
    assert denominator != 0, "Denominator cannot be zero"
    return numerator / denominator

print(divide(10, 2))
print(divide(10, 0))

import logging

# Create a "mylog.log" file in the current working directory
with open("mylog.log", "w") as log_file:
    pass  # This creates an empty file

# Create a logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create a file handler and set the log level
file_handler = logging.FileHandler("mylog.log")
file_handler.setLevel(logging.DEBUG)

# Create a stream handler to display log messages in the terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# Create a formatter for both handlers
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

try:
    value = int("abc")
except ValueError as e:
    # Log the error message
    logger.error("Invalid value, please give an integer")

# Additional code for testing
try:
    value = int("123")  # Replace "123" with any valid integer or "abc" to test different scenarios
except ValueError as e:
    # Log the error message
    logger.error("Invalid value, please give an integer")
