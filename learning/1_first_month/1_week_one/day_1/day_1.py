# 1. Python Syntax
# This is a single comment
""" 
This is multiline comment
line 1
line 2
... ... ...
 """
print("Hello, World!")  # This prints a message to the console

# 2. Variables
# variable_name = value
x = 5
name = "Alice"

# 3. Data Types
age = 30    # Integer (`int`):** Whole numbers
height = 5.9    # Float (`float`):** Numbers with decimal points.
greeting = "Hello, World!"    # String (`str`):** Textual data enclosed in quotes.
is_active = True    # Boolean (`bool`):** Represents `True` or `False

# Convert between types using functions like `int()`, `float()`, `str()`
number = int("10")  # Converts string to integer (Type Conversion)

# 4. Basic Operators
# Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), Modulus (`%`), Exponentiation (`**`), Floor Division (`//`)
sum = 5 + 3  # Addition --> 8
subs = 5 - 3 # Substraction --> 2
product = 4 * 7  # Multiplication --> 28
division = 10 / 2  # Division --> 5.0 (float)
modulus = 10 % 3  # Modulus --> 1
exponent = 2 ** 3  # Exponentiation --> 8
floor_division = 10 // 3  # Floor Division --> 3

# Comparison Operators: Equal to (`==`), Not equal to (`!=`), Greater than (`>`), Less than (`<`), Greater than or equal to (`>=`), Less than or equal to (`<=`)
is_equal = (5 == 5)  # Equal to --> True
is_not_equal = (5 != 5)  # Not equal to --> False
is_greater = (10 > 5)  # Greater than --> True

# Logical Operators: `and`, `or`, `not`
result = (5 > 3) and (2 < 4)  # Logical AND --> True
result = (5 > 3) or (2 > 4)  # Logical OR --> True
result = not (5 > 3)  # Logical NOT --> False

# 5. Strings
text = "Python"
text2 = 'is fun!'
combined = text + " is fun!"  # Concatenation --> "Python is fun!"
repeated = text * 2  # Repetition --> "PythonPython"

first_char = text[0]  # Indexing --> 'P'
last_char = text[-1]  # Indexing --> 'n'

text = "HeLlo World"
slice1 = text[0:5]  # Slicing --> "HeLlo"
slice2 = text[6:]   # Slicing --> "World"
slice3 = text[:5]   # Slicing --> "HeLlo"
lower_text = text.lower()  # --> "hello world"
upper_text = text.upper()  # --> "HELLO WORLD"
title_text = text.title()  # --> "Hello World"
capitalized_text = text.capitalize()  # --> "Hello world"
replaced_text = text.replace("World", "Python")  # --> "HeLlo Python"
replaced_text = text.replace("HeLlo", "Hello")  # --> "HeLlo World"
split_text = text.split(" ")  # --> ["Hello", "World"]
index = text.find("World")  # --> 6
starts = text.startswith("Hello")  # --> True
ends = text.endswith("World")  # --> True
is_alpha = text.isalpha()  # --> True

words = ["Hello", "World"]
joined_text = " ".join(words)  # --> "Hello World"

text = "Hello World World"
index = text.rfind("World")  # --> 12

text = "   Hello World   "
stripped_text = text.strip()  # --> "Hello World"
text = "   Hello World"
left_stripped_text = text.lstrip()  # --> "Hello World"
text = "Hello World   "
right_stripped_text = text.rstrip()  # --> "Hello World"
text = "   "
is_space = text.isspace()  # --> True

text = "12345"
is_digit = text.isdigit()  # --> True

text = "42"
padded_text = text.zfill(5)  # --> "00042"

# 6. Lists
my_list = [1, 2, 3, "hello"]
my_list.append("new item")  # --> [1, 2, 3, 'hello', 'new item']
item = my_list[1]   # --> 2
my_list.remove("new item")  # --> [1, 2, 3, 'hello']
item = my_list.pop()  # --> 'hello'
item = my_list.pop(1)  # --> 2
my_list.extend([4, 5, 6])  # --> [1, 3, 'hello', 4, 5, 6]
my_list.insert(2, "new item")  # --> [1, 3, 'new item', 'hello', 4, 5, 6]
my_list.clear()  # --> []
my_list.reverse()  # --> [6, 5, 4, 'hello', 3, 1]
my_list.sort()  # --> [1, 3, 4, 5, 6, 'hello']
my_list.sort(reverse=True)  # --> ['hello', 6, 5, 4, 3, 1]
my_list.sort(key=len)  # --> ['hello', 1, 3, 4, 5, 6]
my_list.sort(key=lambda x: x.lower())  # --> ['hello', 1, 3, 4, 5, 6]
my_list.sort(key=lambda x: x.lower(), reverse=True)  # --> ['hello', 6, 5, 4, 3, 1]

# 7. Tuples
my_tuple = (1, 2, 3, "hello")
element = my_tuple[0] # --> 1
slice = my_tuple[1:3]  # --> (2, 3)
new_tuple = my_tuple + (4, 5)  # --> (1, 2, 3, 'hello', 4, 5)
new_tuple = my_tuple * 2  # --> (1, 2, 3, 'hello', 1, 2, 3, 'hello')
new_tuple = tuple(range(5))  # --> (0, 1, 2, 3, 4)
new_tuple = tuple("hello")  # --> ('h', 'e', 'l', 'l', 'o')
new_tuple = tuple([1, 2, 3])  # --> (1, 2, 3)
new_tuple = tuple((1, 2, 3))  # --> (1, 2, 3)
new_tuple = tuple({1, 2, 3})  # --> (1, 2, 3)
new_tuple = tuple({"name": "Alice", "age": 30})  # --> ('name', 'age')
new_tuple = tuple(my_list)  # --> (1, 2, 3, 'hello')

# 8. Dictionaries
my_dict = {"name": "Alice", "age": 30}
name = my_dict["name"]  # --> Alice
my_dict["location"] = "Wonderland"  # --> {"name": "Alice", "age": 30, "location": "Wonderland"}
my_dict.pop("age")  # --> {"name": "Alice", "location": "Wonderland"}
my_dict.clear()  # --> {}
my_dict.update({"name": "Bob", "age": 25})  # --> {"name": "Bob", "age": 25}
my_dict.setdefault("name", "Charlie")  # --> {"name": "Bob", "age": 25}
my_dict.setdefault("city", "New York")  # --> {"name": "Bob", "age": 25, "city": "New York"}
my_dict.get("name")  # --> "Bob"
my_dict.get("city", "Unknown")  # --> New York
my_dict.keys()  # --> dict_keys(['name', 'age', 'city'])
my_dict.values()  # --> dict_values(['Bob', 25, 'New York'])
my_dict.items()  # --> dict_items([('name', 'Bob'), ('age', 25), ('city', 'New York')])

# 9. Control Flow
if age > 18:
    print("Adult")
else:
    print("Minor")

for i in range(5):
    print(i)    # --> 0, 1, 2, 3, 4

count = 0
while count < 5:
    print(count)    # --> 0, 1, 2, 3, 4
    count += 1

# 10. Functions
def two_sum(param1, param2):
    return param1 + param2

summation = two_sum(5, 3)  # --> 8

def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # --> Hello, Alice!

# 11. File Handling
try:    
    with open('file.txt', 'r') as file:
        content = file.read()

    with open('file.txt', 'w') as file:
        file.write("Hello, World!")
except:
    print(f"Error, something went wrong, while try to read or write file!")

# 12. Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Great! Let’s start with the basics of Python, breaking down key topics to get you started. Here’s a comprehensive overview for your first day of learning Python:
