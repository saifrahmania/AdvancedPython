x = 5
while x < 10:
    print(x)
    x += 1

for x in range(5, 10):
    print(x)

for x in range(5, 10, 2):
    print(x)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for index , day in enumerate(days):
    print(index, day)

names = ["Zeynep", "Ahmet", "Mehmet", "Ayşe"]
ages = [25, 30, 40, 50]

for name, age in zip(names, ages):
    print(name, age)

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    if i == 5:
        print(i)
        break
    else:
        print("else")

for i in range(10):
    for j in range(10):
        print(i, j)

import itertools
for i in itertools.count(3):
    print(i)
    if i >= 11:
        break

squares = [x**2 for x in range(10)]
print(squares)

person = {"name": "Zeynep", "age": 25, "city": "İstanbul"}
for key in person:
    print(key, person[key])

print("Person's Name: ",person["name"])
print("Person's Age: ",person["age"])
print("Person's City: ",person["city"])

word = "Python"
for letter in word:
    print(letter)

with open("file.txt", "r") as file:
    for line in file:
        print("Lines: ",line)

fruits = ["Apple", "Banana", "Cherry"]
search_fruit = "orange"
for fruit in fruits:
    if fruit == search_fruit:
        print("Fruit Found")
        break
    else:
        print(search_fruit," Not Found")


for index, fruit in enumerate(fruits):
    if index % 2 == 0:
        print(fruit)


for name, age_value in zip(names, ages):
    if age > 30:
        print(name, age_value)


for index, fruit in enumerate(fruits):
    if index % 2 == 0:
        print(fruit)
    else:
        continue 
count = 0
for fruit in itertools.cycle(fruits):
    print(fruit)
    count += 1
    if count >= len(fruits):
        break

fruits1 = ["Apple", "Banana", "Cherry"]
fruits2 = ["Orange", "Watermelon", "Grape"]
for fruit in itertools.chain(fruits1, fruits2):
    print(fruit)

colors = ["Red", "Green", "Blue", "Yellow"]
sizes = ["S", "M", "L", "XL"]
for color, size in itertools.product(colors, sizes):
    print(color, size)

