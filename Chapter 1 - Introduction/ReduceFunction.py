# 9. Reduce Function
# The reduce function is used to reduce a list to a single value. The syntax is as follows:
# reduce(function, list)
# Example:
# Suppose we want to find the sum of all the numbers from 1 to 10. We can do this using a for loop as follows:
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum)

# We can do the same thing using a reduce function as follows:
from functools import reduce
sum = reduce(lambda x, y: x + y, range(1, 11))
print(sum)