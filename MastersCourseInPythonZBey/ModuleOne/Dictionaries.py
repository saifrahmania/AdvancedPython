my_dict = {}
my_dict = {"name": "John", "age": 25, "city": "New York"}
print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
my_dict["email"] = "john@gmail.com"
print(my_dict)
my_dict.pop("email")
print(my_dict)
for key in my_dict:
    print(key, my_dict[key])

if "name" in my_dict:
    print(my_dict["name"])

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
for key in sorted(my_dict.keys()):
    print(key, my_dict[key])

squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers)