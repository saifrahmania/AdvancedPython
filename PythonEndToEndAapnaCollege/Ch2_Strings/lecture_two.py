# str1 = "This is a string"
# str2 = 'This is also a string'
# str3 = """This is a multiline string"""
# str4 = '''This is also a multiline string'''
# print(str1)
# print(str2)
# print(str3)
# print(str4)

# # Concatenation
# str5 = "hello"
# str6 = "world"
# str7 = str5 + " " + str6
# print(str7)

# length of string

# print(len(str7))
# print(str7[0])
# print(str7[1])
# print(str7[2])
# print(str7[3])
# print(str7[4])

# # Slicing
# print(str7[0:5])
# print(str7[:5])
# print(str7[6:len(str7)])
# print(str7[:])
# print(str7[0:5:2])
# print(str7[-1:-5:-1])
# print(str7.endswith("World"))
# print(str7.capitalize())
# print(str7.replace("hello", "Hellou"))
# print(str7.find("world"))
# print(str7.count("l"))

# # Conditional Statements
# age = 12

# if (age >= 16 and age < 18):
#     print("You are eligible for drinking but not for driving")
# elif (age >= 18):
#     print("You are eligible for driving")
# else:
#     print("You are not eligible for driving and drinking")

# marks = [90, 80, 70, 60, 50]
# for mark in marks:
#     if mark >= 90:
#         print("Grade A")
#     elif mark >= 80:
#         print("Grade B")
#     elif mark >= 70:
#         print("Grade C")
#     elif mark >= 60:
#         print("Grade D")
#     else:
#         print("Grade F")

# num  = input("Enter a number: ")
# num = int(num)
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("The greatest number is:", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("The greatest number is:", num2)
# else:
#     print("The greatest number is:", num3)

# numbers = []
# for i in range(7):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# greatest = numbers[0]
# for num in numbers:
#     if num > greatest:
#         greatest = num

# print("The greatest number is:", greatest)
num = int(input("Enter a number: "))

if num % 7 == 0:
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")