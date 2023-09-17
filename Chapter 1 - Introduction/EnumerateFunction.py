# 11. Enumerate Function
# The enumerate function is used to add a counter to an iterable. The syntax is as follows:
# enumerate(iterable, start=0)
# Example:
# Suppose we have a list of numbers. We can add a counter to it using a for loop as follows:    
# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     print(i, numbers[i])

# We can do the same thing using an enumerate function as follows:
numbers = [1, 2, 3, 4, 5]
for i, number in enumerate(numbers):
    print(i, number)