def greet(name):
    print("Hello, " + name + "!")

name = 'Saifur'
greet(name)

def add(x, y):
    return x + y

result = add(5, 10)
print(result)

result = add( x= 5, y= 10)
print(result)

result = add(3, y= 10)
print(result)

def add(x):
    return x + 5

result = add(5)
print(result)

def print_args(*args):
    for arg in args:
        print(arg)

print_args(1,2,3,4,5)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_kwargs(name="John", age=25)

def print_args_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

print_args_kwargs(1,2,3,4,5, name="John", age=25)
