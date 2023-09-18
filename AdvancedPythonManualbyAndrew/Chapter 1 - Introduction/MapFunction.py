# 7. Map Function
# The map function is used to apply a function to every element of a list. The syntax is as follows:
# map(function, list)
# Example:
# Suppose we want to create a list of squares of numbers from 1 to 10. We can do this using a for loop as follows:
# squares = []
# for i in range(1, 11):
#     squares.append(i**2)
# print(squares)

# We can do the same thing using a map function as follows:
numbers = range(5,11)
squares = list(map(lambda x: x**2, numbers))
print(squares)