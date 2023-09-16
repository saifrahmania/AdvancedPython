
def test_function():
    print("Test Func printing the value: ",x)

x = 10
test_function()

# loops can modify the external value 
x = 1
for i in range(10):
    x += 1
print("External values after loop: ",x)

# functions can't modify the external value
def test_function():
    x += 1
    print("Test Func printing the value: ",x)

x = 10
# test_function()
# print("External values after function: ",x)

# functions can modify the external value if it is passed as an argument
def test_function(x):
    x += 1
    print("Test Func printing the value: ",x)
    return x
    


x = 10
test_function(x)
print("External values after function: ",x)
print("Test Func printing the value after calling: ",test_function(x))
test_function_caller = test_function(x)
print("Test Func printing the value calling by variable: ",test_function_caller)

# variable created in a loop will be accessable outside the loop
for i  in (range (10)):
    for j in (range(10, 11)):
        print("printing i", i)
        print("printing j", j)
        k = i + j
        print("printing k", k)
        print()

print("printing k outside the loop", k)
print("printing i outside the loop", i)
print("printing j outside the loop", j)

