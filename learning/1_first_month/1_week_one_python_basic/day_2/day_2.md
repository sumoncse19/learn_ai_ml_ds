### Day 2 Learning: Lists, Tuples, Dictionaries, and Control Flow

#### **6. Lists**

Lists are mutable sequences in Python that can hold items of different data types. Lists are defined using square brackets `[]`.

**Creating and Accessing Lists:**

```python
# Creating a list
my_list = [1, 2, 3, "hello"]

# Accessing elements
first_element = my_list[0]  # --> 1
last_element = my_list[-1]  # --> 'hello'
```

**Common List Operations:**

```python
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
```

**Example:**

```python
# List of numbers
numbers = [3, 1, 4, 1, 5, 9]
numbers.append(2)  # Add 2 to the end
numbers.sort()  # Sorts the list to [1, 1, 2, 3, 4, 5, 9]

# List of strings
words = ["banana", "apple", "cherry"]
words.insert(1, "blueberry")  # Insert 'blueberry' at index 1
# words = ["banana", "blueberry", "apple", "cherry"]
```

#### **7. Tuples**

Tuples are immutable sequences in Python, defined using parentheses `()`. Unlike lists, tuples cannot be changed after they are created.

**Creating and Accessing Tuples:**

```python
# Creating a tuple
my_tuple = (1, 2, 3, "hello")

# Accessing elements
first_element = my_tuple[0]  # --> 1
slice = my_tuple[1:3]  # --> (2, 3)
```

**Common Tuple Operations:**

```python
# Concatenation
new_tuple = my_tuple + (4, 5)  # --> (1, 2, 3, 'hello', 4, 5)

# Repetition
repeated_tuple = my_tuple * 2  # --> (1, 2, 3, 'hello', 1, 2, 3, 'hello')

# Converting other data types to tuple
tuple_from_list = tuple([1, 2, 3])  # --> (1, 2, 3)
```

**Example:**

```python
# Tuple of mixed data types
mixed_tuple = (1, "apple", 3.14)
# Accessing an element
element = mixed_tuple[1]  # --> "apple"
```

#### **8. Dictionaries**

Dictionaries are mutable mappings in Python that store key-value pairs. They are defined using curly braces `{}`.

**Creating and Accessing Dictionaries:**

```python
# Creating a dictionary
my_dict = {"name": "Alice", "age": 30}

# Accessing values
name = my_dict["name"]  # --> Alice
age = my_dict.get("age")  # --> 30
```

**Common Dictionary Operations:**

```python
# Adding and updating elements
my_dict["location"] = "Wonderland"  # Adds a new key-value pair

# Removing elements
my_dict.pop("age")  # Removes the key 'age' and its value

# Clearing dictionary
my_dict.clear()  # Removes all key-value pairs

# Dictionary methods
keys = my_dict.keys()  # Returns dict_keys(['name', 'location'])
values = my_dict.values()  # Returns dict_values(['Alice', 'Wonderland'])
items = my_dict.items()  # Returns dict_items([('name', 'Alice'), ('location', 'Wonderland')])
```

**Example:**

```python
# Dictionary of student grades
grades = {"Alice": 90, "Bob": 85}
grades["Charlie"] = 92  # Add new student
grades["Alice"] = 95  # Update Alice's grade
# Removing a student
grades.pop("Bob")
```

#### **9. Control Flow**

Control flow statements manage the execution flow of a program.

**Conditional Statements:**

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

**Loops:**

```python
# For loop
for i in range(5):
    print(i)  # Outputs 0, 1, 2, 3, 4

# While loop
count = 0
while count < 5:
    print(count)  # Outputs 0, 1, 2, 3, 4
    count += 1
```

**Example:**

```python
# Checking for even and odd numbers
for num in range(10):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```

Feel free to reach out if you need further explanations or more examples!