# -------------------------------------
# Variables and Data Types in Python
# -------------------------------------

# 1. Using Python as a Calculator
# Python can perform complex calculations easily.

# 2. Creating Variables
# Variables are used to store values for reuse in your code.
# Variable names are case-sensitive.

height = 1.79  # height in meters
weight = 68.7  # weight in kilograms

# Printing a variable will show its value
print("Height:", height)
print("Weight:", weight)

# 3. Calculating BMI
# BMI = weight / (height^2)
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

# 4. Reproducibility
# If you change the weight, BMI will update accordingly
weight = 75.0  # New weight
bmi = weight / (height ** 2)
print("New BMI:", bmi)

# 5. Python Data Types
# Use type() to check the data type of a variable
print("Type of bmi:", type(bmi))  # float

# Integer example
age = 25
print("Type of age:", type(age))  # int

# String example
name = "Sumon"
print("Type of name:", type(name))  # str

# Boolean example
is_student = True
print("Type of is_student:", type(is_student))  # bool

# 6. Operator Behavior Based on Type
# Adding integers
sum_numbers = 3 + 4
print("Sum of integers:", sum_numbers)  # 7

# Adding strings (concatenation)
sum_strings = "Hello" + " " + "World"
print("Sum of strings:", sum_strings)  # "Hello World"

# 7. Summary
# - Variables help store and reuse values.
# - Python supports multiple data types: int, float, str, bool.
# - Operator behavior depends on the data type.
# - Reproducible code allows easy updates and reusability.

# Practice creating variables and using different data types below!

