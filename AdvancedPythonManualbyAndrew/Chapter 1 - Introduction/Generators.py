# 18. Generators
# Generators are used to create iterators. They are used to create iterators without having to write a class. The syntax is as follows:
# def generator():
#     yield value
# Example:
# Suppose we want to create a generator that yields the squares of numbers from 1 to 10. We can do this using a normal function as follows:
# def squares():
#     for i in range(1, 11):
#         yield i**2
# for square in squares():
#     print(square)

# We can do the same thing using a generator as follows:
def squares():
    for i in range(1, 11):
        yield i**2
for square in squares():
    print(square)