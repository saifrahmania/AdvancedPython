# 17. Iterators
# Iterators are used to iterate over an iterable. They are used to access the elements of an iterable one by one. The syntax is as follows:
# for item in iterable:
#     pass
# Example:
# Suppose we have a list of numbers. We can iterate over it using a for loop as follows:
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)

# We can do the same thing using an iterator as follows:
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break