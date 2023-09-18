# 13. All Function
# The all function is used to check if all elements of an iterable are True. The syntax is as follows:
# all(iterable)
# Example:
# Suppose we have a list of numbers. We can check if all of them are even using a for loop as follows:
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     if number % 2 != 0:
#         print(False)
#         break

# We can do the same thing using an all function as follows:
numbers = [1, 2, 3, 4, 5]
print(all([True if number % 2 == 0 else False for number in numbers]))