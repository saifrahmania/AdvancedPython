# 8. Filter Function
# The filter function is used to filter out elements of a list that don't satisfy a certain condition. The syntax is as follows:
# filter(function, list)
# Example:
# Suppose we want to create a list of even numbers from 1 to 10. We can do this using a for loop as follows:
# even_numbers = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         even_numbers.append(i)
# print(even_numbers)

# We can do the same thing using a filter function as follows:
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(even_numbers)