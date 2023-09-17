# 16. Decorators
# Decorators are used to modify the behavior of a function without changing its code. They are used to add functionality to a function. The syntax is as follows:
# @decorator
# def function():
#     pass
# Example:
# Suppose we want to create a decorator that prints the time taken by a function to execute. We can do this using a normal function as follows:
# import time
# def time_taken(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end - start)
#     return wrapper
# @time_taken
# def function():
#     for i in range(1000000):
#         pass
# function()

# We can do the same thing using a decorator as follows:
import time
def time_taken(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper
@time_taken
def function():
    for i in range(1000000):
        pass
function()