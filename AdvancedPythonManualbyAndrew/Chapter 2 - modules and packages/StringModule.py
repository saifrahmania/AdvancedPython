import string

def print_uppercase(input_string):
    print(input_string.upper())

def print_lowercase(input_string):
    print(input_string.lower())

def print_capitalize(input_string):
    print(input_string.capitalize())

def print_title(input_string):
    print(input_string.title())


def print_swapcase(input_string):
    print(input_string.swapcase())

def print_strip(input_string):
    print(input_string.strip())

def print_lstrip(input_string):
    print(input_string.lstrip())

def print_rstrip(input_string):
    print(input_string.rstrip())

def print_replace(input_string, old, new):
    print(input_string.replace(old, new))

def print_split(input_string, separator):
    print(input_string.split(separator))

def print_splitlines(input_string):
    print(input_string.splitlines())

def print_count(input_string, sub_string):
    print(input_string.count(sub_string))

def print_find(input_string, sub_string):
    print(input_string.find(sub_string))

def print_rfind(input_string, sub_string):
    print(input_string.rfind(sub_string))

def print_index(input_string, sub_string):
    print(input_string.index(sub_string))

def print_rindex(input_string, sub_string):
    print(input_string.rindex(sub_string))

def print_startswith(input_string, prefix):
    print(input_string.startswith(prefix))

def print_endswith(input_string, suffix):
    print(input_string.endswith(suffix))

def print_isalnum(input_string):
    print(input_string.isalnum())

def print_isalpha(input_string):
    print(input_string.isalpha())

def print_isdigit(input_string):
    print(input_string.isdigit())

def print_islower(input_string):
    print(input_string.islower())

def print_isupper(input_string):
    print(input_string.isupper())

def print_isspace(input_string):
    print(input_string.isspace())

def print_istitle(input_string):
    print(input_string.istitle())

def print_isnumeric(input_string):
    print(input_string.isnumeric())

def print_isdecimal(input_string):
    print(input_string.isdecimal())

def print_isidentifier(input_string):
    print(input_string.isidentifier())

def print_isprintable(input_string):
    print(input_string.isprintable())

def print_zfill(input_string, width):
    print(input_string.zfill(width))

def print_center(input_string, width):
    print(input_string.center(width))

def print_ljust(input_string, width):
    print(input_string.ljust(width))

def print_rjust(input_string, width):
    print(input_string.rjust(width))

input_string = input('Enter a string: ')
print_uppercase(input_string)
print_lowercase(input_string)
print_capitalize(input_string)
print_title(input_string)
print_swapcase(input_string)
print_strip(input_string)
print_lstrip(input_string)
print_rstrip(input_string)
old = input('Enter the old string: ')
new = input('Enter the new string: ')
print_replace(input_string, old, new)
separator = input('Enter the separator: ')
print_split(input_string, separator)
print_splitlines(input_string)
sub_string = input('Enter the sub string: ')
print_count(input_string, sub_string)
print_find(input_string, sub_string)
print_rfind(input_string, sub_string)
print_index(input_string, sub_string)
print_rindex(input_string, sub_string)
prefix = input('Enter the prefix: ')
print_startswith(input_string, prefix) 
suffix = input('Enter the suffix: ')
print_endswith(input_string, suffix)
print_isalnum(input_string)
print_isalpha(input_string)
print_isdigit(input_string)
print_islower(input_string)
print_isupper(input_string)
print_isspace(input_string)
print_istitle(input_string)
print_isnumeric(input_string)
print_isdecimal(input_string)
print_isidentifier(input_string)
print_isprintable(input_string)