# 12. Any Function
# The any function is used to check if any element of an iterable is True. The syntax is as follows:
# any(iterable)
# Example:
# Suppose we have a list of numbers. We can check if any of them are even using a for loop as follows:
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     if number % 2 == 0:
#         print(True)
#         break

# We can do the same thing using an any function as follows:
numbers = [1, 2, 3, 4, 5]
print(any([True if number % 2 == 0 else False for number in numbers]))