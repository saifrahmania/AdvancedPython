def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result = add_numbers(num1, num2)
difference_result = subtract_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
division_result = divide_numbers(num1, num2)

# Print the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Division:", division_result)

def calculate_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Calculate the sum of numbers from 1 to 15
sum_result = calculate_sum(1, 15)
print("Sum:", sum_result)

# Calculate the factorial of the sum
factorial_result = calculate_factorial(sum_result)
print("Factorial:", factorial_result)

# time stamp: 06:23:21