# 5. Conditional Comprehension
# Conditional Comprehension is a way to filter out the elements of a list that don't satisfy a certain condition. It is similar to the way a conditional loop works, but it is much more concise and powerful. The syntax is as follows:
# [expression for item in list if conditional]

# Example:
# Suppose we want to create a list of normal nmbers and they will have to be less than 10. We can do this using a for loop as follows:
# normal_numbers = []
# for i in range(20):
#     if i < 10:
#         normal_numbers.append(i)
# print(normal_numbers)

# We can do the same thing using a conditional comprehension as follows:
normal_numbers = [i for i in range(20) if i < 10]
print(normal_numbers)

# turnary operator
# The turnary operator is a way to write an if-else statement in a single line. The syntax is as follows:
# [on_true] if [expression] else [on_false]
# Example:
# Suppose we want to create a list of even numbers and odd numbers. We can do this using a for loop as follows:
# even_numbers = []
# odd_numbers = []
# for i in range(20):
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
# print(even_numbers)
# print(odd_numbers)

# We can do the same thing using a conditional comprehension as follows:
even_numbers = [i if i % 2 == 0 else None for i in range(20)]
odd_numbers = [i if i % 2 != 0 else None for i in range(20)]
print(even_numbers)
print(odd_numbers)