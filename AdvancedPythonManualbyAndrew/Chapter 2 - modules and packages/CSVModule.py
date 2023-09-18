path = "C:\\Users\\Admin\\Documents\\GitHub\\AdvancedPython\\Chapter 2 - modules and packages\\csvtest.csv"
file = open(path, "w")
file.write("item, color, size\n")
file.write("ball, red, small\n")
file.write("ball, red, medium\n")
file.write("ball, red, large\n")
file.write("ball, blue, small\n")
file.write("ball, blue, medium\n")
file.write("ball, blue, large\n")
file.write("ball, green, small\n")
file.write("ball, green, medium\n")
file.write("bat, green, large\n")
file.write("bat, red, small\n")
file.write("bat, red, medium\n")
file.write("bat, red, large\n")
file.close()

# Path: Chapter%202%20-%20modules%20and%20packages/CSVModule.py
import csv
path = "C:\\Users\\Admin\\Documents\\GitHub\\AdvancedPython\\Chapter 2 - modules and packages\\csvtest.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader) # The first line is the header
data = [row for row in reader] # Read the remaining data
print(header)
print(data)

