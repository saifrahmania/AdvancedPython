import re
pattern = "^[a-z]+$"
strings = ["abc", "123", "ABC", "abc123", "abcABC", "ABCabc", "abcABC123", "ABCabc123", "abcABC123xyz"]
for string in strings:
    if re.match(pattern, string):
        print(string, "matches")
    else:
        print(string, "does not match")

pattern2 = "\d{3}-\d{3}-\d{4}"
strings2 = "My SSN is 123-45-6789"

match  = re.search(pattern2, strings2)
if match:
    print("SSN found:", match.group())
else:
    print("SSN not found")

pattern3 = "\d+"
strings3 = "There are 1000 apples for 123 persons."
new_string = re.sub(pattern3, "N", strings3)
print(new_string)