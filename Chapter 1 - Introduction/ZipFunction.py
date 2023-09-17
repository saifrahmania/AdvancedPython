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

t1 = (1, 2, 3)
t2 = (4, 5, 6)
l1 = [t1, t2]
print(l1)
print(type(l1[1]))
zipped = zip(t1, t2)
print(zipped)
print(list(zipped)) 
