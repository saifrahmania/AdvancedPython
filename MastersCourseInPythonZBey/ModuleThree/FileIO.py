with open("example.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("joy bangla!\n")
with open("example.txt", "a") as f:
    f.write("Hello, Saifur!")
with open("example.txt", "r") as f:
    print(f.read())
f.close()

import csv
with open("example.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Saifur", 23])
    writer.writerow(["Rahman", 24]) 


with open("example.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

