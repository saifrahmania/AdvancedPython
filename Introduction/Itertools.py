# 19. Itertools
# Itertools is a module that provides various functions that work on iterators to produce complex iterators. It is used to create iterators for efficient looping. The syntax is as follows:
# import itertools
# Example:
# Suppose we want to create an iterator that yields the squares of numbers from 1 to 10. We can do this using a normal function as follows:
# import itertools
# def squares():
#     for i in itertools.count(1):
#         yield i**2
# for square in squares():
#     print(square)
#     if square == 100:
#         break

# We can do the same thing using itertools as follows:
import itertools
def squares():
    for i in itertools.count(1):
        yield i**2
for square in squares():
    print(square)
    if square == 100:
        break