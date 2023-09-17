# 20. Collections
# Collections is a module that provides various functions that work on collections to produce complex collections. It is used to create collections for efficient data manipulation. The syntax is as follows:
# import collections
# Example:
# Suppose we want to create a list of numbers. We can do this using a normal list as follows:
# import collections
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# We can do the same thing using collections as follows:
import collections
numbers = collections.deque([1, 2, 3, 4, 5])
print(numbers)
