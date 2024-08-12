info = {
    "name": "Aapna College",
    "course": "Python",
    "year": 2021,
    "students": 1000,
    "classRepresentative" : {
        "name": "Shribastab",
        "year": 2021,
        "branch": "CSE"
    },
    "Owner" : "Hemant",
    "location": "Jaipur",
    "teachers": ["Hemant", "Shribastab", "Rahul"]
}

print(info["Owner"])
print(info["teachers"])
print(info["classRepresentative"])

info.update({"students": 2000})
print(info)

# Sets:

collection = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(collection)
print(type(collection))
print(len(collection))
collection.add(11)
print(collection)
collection.pop()
sets = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(collection)
print(collection.intersection(sets))
collection.clear()
print(len(collection))

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts and figures"]
}

print(dictionary["table"])

rooms = {"python", "java", "c++", "c", "java", "javascript", "python", "python", "java"}
print(len(rooms))

values= {("int", 9), ("float",9.0), "9"}
print(values)