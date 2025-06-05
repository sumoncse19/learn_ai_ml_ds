# Summary: Python Functions

# This video introduces functions in Python, which are reusable blocks of code designed to perform specific tasks.

# 1. What is a Function?
# - A function is a block of code you can call to execute a task without rewriting the logic.
# - Example: `type()` returns the type of a value. You've already used built-in functions like this.

# 2. Example - max()
# - You can use max(fam) to get the tallest value in a list called fam.
# - It acts like a black box: you input data and get output without needing to know the internal logic.

fam = [1.73, 1.68, 1.71, 1.89]
tallest = max(fam)
print(tallest)  # Output: 1.89

# 3. Example - round()
# - round() takes a number and optionally the number of decimal places.
# - With two arguments: it rounds to that many decimal places.
# - With one argument: it rounds to the nearest integer.

print(round(1.68, 1))  # Output: 1.7
print(round(1.68))     # Output: 2

# 4. Arguments and Optional Arguments
# - Arguments are inputs to a function. In round(), number and ndigits are arguments.
# - ndigits is optional — if you skip it, Python assumes you want to round to the nearest whole number.

# 5. Discovering Functions
# - To find out if a function exists for a task, check Python docs, Google, or use learning platforms like DataCamp.

# 6. Practice Time
# - The video encourages you to start using functions in exercises right away.
