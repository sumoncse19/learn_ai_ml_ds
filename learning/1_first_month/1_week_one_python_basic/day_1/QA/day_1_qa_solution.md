Here are the answers to the questions:

### **1. Python Syntax & Variables**

1. **Explain the difference between single-line comments and multi-line comments in Python.**
   - **Single-line comments** start with `#` and are used for brief comments. Example: `# This is a single-line comment`.
   - **Multi-line comments** are enclosed in triple quotes (`"""` or `'''`). They are used for longer comments spanning multiple lines. Example:
     ```python
     """
     This is a multi-line comment
     spanning multiple lines.
     """
     ```

2. **What will the following code print?**
   ```python
   x = 10
   y = 5
   print(x + y)
   ```
   - The code will print `15`, which is the result of adding `10` and `5`.

3. **How can you convert a string `"123"` to an integer in Python?**
   - Use the `int()` function: `number = int("123")`.

### **2. Data Types**

1. **What are the main data types in Python?**
   - The main data types are:
     - `int` (integer)
     - `float` (floating-point number)
     - `str` (string)
     - `bool` (boolean)
     - `list` (list)
     - `tuple` (tuple)
     - `dict` (dictionary)
     - `set` (set)

2. **How do you check the type of a variable in Python?**
   - Use the `type()` function: `type(variable_name)`.

3. **What will be the result of the following operation?**
   ```python
   result = 5.0 + 3
   print(result)
   ```
   - The result will be `8.0`, as `5.0` (a float) and `3` (an integer) result in a float when added.

### **3. Basic Operators**

1. **Write a Python expression that uses the modulus operator to find the remainder of 17 divided by 4.**
   - The expression is `17 % 4`, which results in `1`.

2. **What is the difference between `/` and `//` in Python?**
   - `/` performs floating-point division (returns a float). Example: `10 / 3` results in `3.3333`.
   - `//` performs floor division (returns the integer part of the division). Example: `10 // 3` results in `3`.

### **4. Comparison Operators**

1. **What will the following expression evaluate to?**
   ```python
   (10 != 10) or (5 < 8)
   ```
   - The expression will evaluate to `True` because `5 < 8` is `True`.

2. **How would you use comparison operators to check if a number is within a specific range (e.g., 10 to 20)?**
   - Use `and` to combine comparisons: `10 <= number <= 20`.

### **5. Logical Operators**

1. **What will be the result of the following logical operation?**
   ```python
   not (True and False)
   ```
   - The result will be `True` because `True and False` is `False`, and `not False` is `True`.

2. **Explain the difference between `and`, `or`, and `not` operators.**
   - `and`: Returns `True` if both operands are `True`. Example: `True and False` is `False`.
   - `or`: Returns `True` if at least one operand is `True`. Example: `True or False` is `True`.
   - `not`: Returns the opposite boolean value of the operand. Example: `not True` is `False`.

### **6. Strings**

1. **How can you extract the substring `"World"` from the string `"Hello World"`?**
   - Use slicing: `"Hello World"[6:]`.

2. **What does the `strip()` method do in a string?**
   - The `strip()` method removes leading and trailing whitespace from the string.

3. **How do you check if a string ends with a specific suffix?**
   - Use the `endswith()` method: `text.endswith("suffix")`.

### **7. Lists**

1. **How would you remove the first occurrence of an item in a list?**
   - Use the `remove()` method: `my_list.remove(item)`.

2. **What will be the result of the following code?**
   ```python
   my_list = [1, 2, 3]
   my_list.append([4, 5])
   ```
   - The list will be `[1, 2, 3, [4, 5]]`, as `[4, 5]` is added as a single item.

### **8. Tuples**

1. **Explain why tuples are immutable.**
   - Tuples are immutable because their elements cannot be changed or modified after creation. This means that once a tuple is defined, its size and contents cannot be altered.

2. **How do you concatenate two tuples?**
   - Use the `+` operator: `(1, 2) + (3, 4)` results in `(1, 2, 3, 4)`.

### **9. Dictionaries**

1. **How can you add a new key-value pair to a dictionary?**
   - Use the assignment syntax: `my_dict["new_key"] = "new_value"`.

2. **What method would you use to get all the keys from a dictionary?**
   - Use the `keys()` method: `my_dict.keys()`.

### **10. Control Flow**

1. **Write a Python program that prints numbers from 1 to 10 using a `for` loop.**
   ```python
   for i in range(1, 11):
       print(i)
   ```

2. **Explain how a `while` loop works with an example.**
   - A `while` loop continues executing a block of code as long as its condition is `True`. Example:
     ```python
     count = 0
     while count < 5:
         print(count)
         count += 1
     ```

### **11. Functions**

1. **What is the purpose of the `return` statement in a function?**
   - The `return` statement is used to send the result of a function back to the caller.

2. **How do you define a function that takes variable number of arguments?**
   - Use `*args` for positional arguments and `**kwargs` for keyword arguments. Example:
     ```python
     def function_name(*args, **kwargs):
         print(args)
         print(kwargs)
     ```

### **12. File Handling**

1. **How can you read the contents of a file and print them to the console?**
   ```python
   with open('file.txt', 'r') as file:
       content = file.read()
       print(content)
   ```

2. **What will happen if you attempt to read from a file that does not exist?**
   - An `FileNotFoundError` will be raised.


### **13. Error Handling**

1. **Handling Exceptions**

In Python, exceptions are handled using `try`, `except`, `else`, and `finally` blocks. Here’s a basic structure of how to handle exceptions:

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to execute if an exception occurs
    print("Cannot divide by zero!")
else:
    # Code to execute if no exception occurs
    print("Division successful!")
finally:
    # Code that will always execute, regardless of whether an exception occurred or not
    print("This block always runs.")
```

**Explanation:**
- **`try` block**: Contains the code that might raise an exception.
- **`except` block**: Contains code that runs if an exception occurs. You can specify different types of exceptions to handle various error scenarios.
- **`else` block**: Optional. Contains code that runs if no exceptions are raised.
- **`finally` block**: Optional. Contains code that always executes, regardless of whether an exception occurred or not. It’s commonly used for cleanup actions.

2. **Purpose of the `finally` Block**

The `finally` block is used to ensure that certain code is executed no matter what happens, even if an exception occurs or if the `try` block completes successfully. This is useful for cleanup operations, such as closing files or releasing resources.

**Example:**

```python
try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # This will always execute, ensuring the file is closed
    print("File closed.")
```

**Explanation:**
- **`try` block**: Tries to open and read a file.
- **`except` block**: Catches and handles the `FileNotFoundError` if the file does not exist.
- **`finally` block**: Ensures the file is closed regardless of whether an exception was raised or not. This ensures proper resource management.

Feel free to ask if you need more details or examples!
Feel free to ask if you need further clarification on any of these answers!