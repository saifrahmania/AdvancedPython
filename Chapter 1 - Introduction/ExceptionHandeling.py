# Firs example 
my_list = ['A', 'B','C']
# print(my_list[3])

try:
    my_list[3]
except IndexError:
    print("that index is out of range")

# Second Example

my_dict = {"Aardvark": 1,"Baboon": 2, "Cougar": 3}
try:
    value = my_dict["Baboon"]
except TypeError:
    print("This index is unhashable")
except KeyError:
    print("This key is not in the directory")
except:
    print("Some other error has been occured")
finally:
    print("Let's carry on")