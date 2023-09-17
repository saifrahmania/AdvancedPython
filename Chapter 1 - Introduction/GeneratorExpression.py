# 15. Generator Expressions
# Generator expressions are used to create iterators. They are similar to list comprehensions, but instead of returning a list, they return a generator. The syntax is as follows:
# (expression for item in iterable)
# Example:
# Suppose we want to create a generator expression that yields the squares of numbers from 1 to 10. We can do this using a normal list comprehension as follows:
# squares = [i**2 for i in range(1, 11)]
# for square in squares:
#     print(square)

# We can do the same thing using a generator expression as follows:
squares = (i**2 for i in range(1, 11))
for square in squares:
    print(square)
