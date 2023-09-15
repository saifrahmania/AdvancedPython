# Description: This file contains the introduction to python programming language.
# 1. Lists
# 2. Sets
# 3. Tuples
# 4. Dictionaries

# 1. Lists
# Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.

# The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator. For example − 
mylist = [x**2 for x in range(10)]
print(mylist)

# 2. Sets
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed). However, a set itself is mutable. We can add or remove items from it.

# Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

set = { 'A', 'B', 'C', 'C', 'A'}
print(set)

# 3. Tuples
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

tuple = ( 'A', 'B', 'C', 'C', 'A')
print(tuple)

# 4. Dictionaries
# Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
print(dict['one'])
print(dict[2])
print(dict)

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

# 6. Lambda Functions
# Lambda functions are anonymous functions. They are used to create functions that are not bound to a name. They are used to create functions that are used only once. They are also called throw-away functions. They are defined using the lambda keyword. The syntax is as follows:
# lambda arguments: expression
# Example:
# Suppose we want to create a function that squares a number. We can do this using a normal function as follows:
# def square(x):
#     return x**2
# print(square(5))

# We can do the same thing using a lambda function as follows:
square = lambda x: x**2
print(square(5))

# 7. Map Function
# The map function is used to apply a function to every element of a list. The syntax is as follows:
# map(function, list)
# Example:
# Suppose we want to create a list of squares of numbers from 1 to 10. We can do this using a for loop as follows:
# squares = []
# for i in range(1, 11):
#     squares.append(i**2)
# print(squares)

# We can do the same thing using a map function as follows:
squares = list(map(lambda x: x**2, range(1, 11)))
print(squares)

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

# 10. Zip Function
# The zip function is used to combine two lists into a single list of tuples. The syntax is as follows:
# zip(list1, list2)
# Example:
# Suppose we have two lists of numbers. We can combine them into a single list of tuples using a for loop as follows:
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# combined_list = []
# for i in range(len(list1)):
#     combined_list.append((list1[i], list2[i]))
# print(combined_list)

# We can do the same thing using a zip function as follows:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
combined_list = list(zip(list1, list2))
print(combined_list)

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

# 14. Generator Functions
# Generator functions are used to create iterators. They are similar to normal functions, but instead of returning a value, they yield a series of values. The syntax is as follows:
# def generator_function():
#     yield value
# Example:
# Suppose we want to create a generator function that yields the squares of numbers from 1 to 10. We can do this using a normal function as follows:
# def squares():
#     for i in range(1, 11):
#         yield i**2
# for square in squares():
#     print(square)

# We can do the same thing using a generator function as follows:
def squares():
    for i in range(1, 11):
        yield i**2
for square in squares():
    print(square)

# 15. Generator Expressions
# Generator expressions are used to create iterators. They are similar to list comprehensions, but instead of returning a list, they return a generator. The syntax is as follows:
# (expression for item in iterable)
# Example:
# Suppose we want to create a generator expression that yields the squares of numbers from 1 to 10. We can do this using a normal list comprehension as follows:
# squares = [i**2 for i in range(1, 11)]
# for square in squares:
#     print(square)

# We can do the same thing using a generator expression as follows:
squares = (i**2 for i in range(1, 11))
for square in squares:
    print(square)

# 16. Decorators
# Decorators are used to modify the behavior of a function without changing its code. They are used to add functionality to a function. The syntax is as follows:
# @decorator
# def function():
#     pass
# Example:
# Suppose we want to create a decorator that prints the time taken by a function to execute. We can do this using a normal function as follows:
