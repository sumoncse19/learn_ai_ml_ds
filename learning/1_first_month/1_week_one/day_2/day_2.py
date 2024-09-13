"""
<--- # 6. Lists --->
"""
# Creating a list
my_list = [1, 2, 3, "hello"]

# Accessing elements
first_element = my_list[0]  # --> 1
last_element = my_list[-1]  # --> 'hello'

# Common List Operations: --->

# Adding elements
my_list.append("new item")  # Adds 'new item' to the end of the list

# Removing elements
my_list.remove("new item")  # Removes the first occurrence of 'new item'

# Accessing and modifying elements
item = my_list.pop()  # Removes and returns the last element
item = my_list.pop(1)  # Removes and returns the element at index 1

# Extending lists
my_list.extend([4, 5, 6])  # Adds elements from another iterable to the end of the list

# Inserting elements
my_list.insert(2, "new item")  # Inserts 'new item' at index 2

# Sorting lists
my_list.sort()  # Sorts the list in ascending order
my_list.sort(reverse=True)  # Sorts the list in descending order
my_list.sort(key=len)  # Sorts the list based on the length of elements

# Example: 
# List of numbers
numbers = [3, 1, 4, 1, 5, 9]
numbers.append(2)  # Add 2 to the end
numbers.sort()  # Sorts the list to [1, 1, 2, 3, 4, 5, 9]

# List of strings
words = ["banana", "apple", "cherry"]
words.insert(1, "blueberry")  # Insert 'blueberry' at index 1
# words = ["banana", "blueberry", "apple", "cherry"]


"""
<--- # 7. Tuples --->
"""
# Creating a tuple
my_tuple = (1, 2, 3, "hello")

# Accessing elements
first_element = my_tuple[0]  # --> 1
slice = my_tuple[1:3]  # --> (2, 3)

# Common Tuple Operations:
# Concatenation
new_tuple = my_tuple + (4, 5)  # --> (1, 2, 3, 'hello', 4, 5)

# Repetition
repeated_tuple = my_tuple * 2  # --> (1, 2, 3, 'hello', 1, 2, 3, 'hello')

# Converting other data types to tuple
tuple_from_list = tuple([1, 2, 3])  # --> (1, 2, 3)

tuple_from_string = tuple("hello")  # --> ('h', 'e', 'l', 'l', 'o')
tuple_from_set = tuple({1, 2, 3})  # --> (1, 2, 3)
tuple_from_dict = tuple({"name": "Alice", "age": 30})  # --> ('name', 'age')

# Example:
# Tuple of mixed data types
mixed_tuple = (1, "apple", 3.14)
# Accessing an element
element = mixed_tuple[1]  # --> "apple"

"""
<--- # 8. Dictionaries --->
"""
# Creating a dictionary
my_dict = {"name": "Alice", "age": 30}

# Accessing values
name = my_dict["name"]  # --> Alice

# Modifying values
my_dict["age"] = 31

# Adding key-value pairs
my_dict["location"] = "Wonderland"

# Removing key-value pairs
my_dict.pop("age")

# Clearing all elements
my_dict.clear()

# Updating or merging dictionaries
my_dict.update({"name": "Bob", "age": 25})

# Setting a default value for a key
my_dict.setdefault("name", "Charlie")

# Getting a value with a default
my_dict.get("city", "Unknown")

# Getting keys, values, and items
my_dict.keys()  # --> dict_keys(['name', 'age', 'city'])
my_dict.values()  # --> dict_values(['Bob', 25, 'New York'])
my_dict.items()  # --> dict_items([('name', 'Bob'), ('age', 25), ('city', 'New York')])

# Example: 
# Dictionary of student grades
grades = {"Alice": 90, "Bob": 85}
grades["Charlie"] = 92  # Add new student
grades["Alice"] = 95  # Update Alice's grade
# Removing a student
grades.pop("Bob")

"""
<--- # 9. Control Flow --->
"""
# Conditional Statements
if age > 18:
    print("Adult")
else:
    print("Minor")

# Loops
for i in range(5):
    print(i)    # --> 0, 1, 2, 3, 4

count = 0
while count < 5:
    print(count)    # --> 0, 1, 2, 3, 4
    count += 1

# Functions
def two_sum(param1, param2):
    return param1 + param2

summation = two_sum(5, 3)  # --> 8

def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # --> Hello, Alice!

# File Handling && Error Handling
try:    
    with open('file.txt', 'r') as file:
        content = file.read()

    with open('file.txt', 'w') as file:
        file.write("Hello, World!")
except:
    print(f"Error, something went wrong, while try to read or write file!")

# Example:
# Checking for even and odd numbers
for num in range(10):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Great! Let’s start with the basics of Python, breaking down key topics to get you started. Here’s a comprehensive overview for your second day of learning Python.