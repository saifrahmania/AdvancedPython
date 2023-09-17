# 6. Lambda Functions
# Lambda functions are anonymous functions. They are used to create functions that are not bound to a name. They are used to create functions that are used only once. They are also called throw-away functions. They are defined using the lambda keyword. The syntax is as follows:
# lambda arguments: expression
# Example:
# Suppose we want to create a function that squares a number. We can do this using a normal function as follows:
# def square(x):
#     return x**2
# print(square(5))

# We can do the same thing using a lambda function as follows:
square = lambda x: x**2
print(square(5))

# printing series using lambda function

even_numbers = list(map(lambda x: x * 2 + 1, range(10)))
print(even_numbers)

odd_numbers = list(map(lambda x: x * 2 + 1, range(10)))
print(odd_numbers)