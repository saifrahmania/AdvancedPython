# 14. Generator Functions
# Generator functions are used to create iterators. They are similar to normal functions, but instead of returning a value, they yield a series of values. The syntax is as follows:
# def generator_function():
#     yield value
# Example:
# Suppose we want to create a generator function that yields the squares of numbers from 1 to 10. We can do this using a normal function as follows:
# def squares():
#     for i in range(1, 11):
#         yield i**2
# for square in squares():
#     print(square)

# We can do the same thing using a generator function as follows:
def squares():
    for i in range(1, 11):
        yield i**2
for square in squares():
    print(square)