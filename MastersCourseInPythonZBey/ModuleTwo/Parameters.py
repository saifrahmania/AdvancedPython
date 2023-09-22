def multitask(x, y):
    return x + y, x * y, x - y, x / y

addition, multiplication, subtraction, division = multitask(5, 10)
print(addition)
print(multiplication)
print(subtraction)
print(division)
