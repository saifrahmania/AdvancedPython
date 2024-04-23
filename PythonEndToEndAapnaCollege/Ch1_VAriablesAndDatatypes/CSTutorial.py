from math import floor
a = 5
b = 3
sum = a+b
difference = a-b
print("Sum of A and B: ",sum)
print("Difference of A and B: ",difference)

# Expression Execution

a,b = 5,3
sum = a+b
print("expression execution: ")
difference = a-b
print("Sum of A and B: ",sum)
print("Difference of A and B: ",difference)
print("Flore value of A/B: ",floor(a/b))

Txt = "@"
print(4*Txt*7)

# Concatenation
first_name = "Saifur"
last_name = "Rahman"
full_name = first_name + " " + last_name
print(full_name)

first_var = "Saifur"
second_var = "2"
third_var = 3

print((first_var + second_var)*third_var)

# remainder 

a =  - 5
b =  3
c = a%b
print(c)

"""
comments are written here আমি এখানে কমেন্ট লিখছি
"""

# providing input 
name = input("Enter your name: ")
print("Your name is: ",name)
age = float(input("Enter your age: "))
print("Your age is: ",age)
university = input("Enter your university name: ")
print("Your university is: ",university)


# if-elif-else

if age > 18:
    print("You are eligible for voting")
elif age == 18:
    print("You are eligible for voting but you are not an adult")
else:  
    print("You are not eligible for voting")
light = input("Enter the color of the light: ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Ready")
else:
    print("Go")

# # 
# # while loop

i = 0
while i < 5:
    print("Value of i: ",i)
    i += 1

# # for loop

for i in range(5):
    print("Value of i: ",i)

# # for loop with step

for i in range(0,10,2):
    print("Value of i: ",i)

# # for loop with negative step

for i in range(10,0,-2):
    print("Value of i: ",i)

# # for loop with negative step

# problem
A = int(input("Enter the value of A: "))
G  = input("M/F : ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 10")
elif((A == 3 or A == 4) and G == "F"):
    print("fee is 200")
elif(A == 5  and G == "M"):
    print("fee is 300")
else:
    print("no fee")

# time 1:39:42

# single line conditional statement 

food  = input(" Food : ")
eat  = "Yes" if food  == "Cake" or "Cola" else "No"
print(eat)

# clevr if

age = int(input("Enter your age: "))
status = ("Adult","Child")[age < 18]
print("You are a: ",status)

# Calculate simple interest
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time: "))
si = p*r*t/100
print("Simple interest: ",si)
