# -------------------------------------
# Python Lists and Data Types
# -------------------------------------

# 1. Python Basic Data Types Recap
height = 1.79           # float
age = 25               # int
name = "Sumon"         # str (string)
is_student = True      # bool

# Each variable stores one single value.

# 2. Problem with Individual Variables
# Let's say we want to store the heights of 4 family members.
# Creating individual variables for each would be inconvenient.

# 3. Python List
# We can store all of them in one list using square brackets.
fam_heights = [1.73, 1.68, 1.71, 1.89]  # heights in meters
print("Family heights:", fam_heights)

# We can also assign this list to a variable, just like with numbers or strings.

# 4. Lists Can Hold Multiple Data Types
# Let's mix names with heights (not recommended for calculations but allowed in Python).
fam_mixed = ["Liz", 1.73, "Emma", 1.68, "Mom", 1.71, "Dad", 1.89]
print("Mixed family data:", fam_mixed)

# 5. Lists Can Contain Other Lists (Nested Lists)
# A better way to pair names with heights:
fam_nested = [
    ["Liz", 1.73],
    ["Emma", 1.68],
    ["Mom", 1.71],
    ["Dad", 1.89]
]
print("Nested family list:", fam_nested)
print("Height of Liz:", fam_nested[0])  # Accessing Liz's data
print("Height of Liz:", fam_nested[0][1])  # Accessing Liz's height

# 6. List Type Check
# Check the type of the list and nested list
print("Type of fam_heights:", type(fam_heights))  # <class 'list'>
print("Type of fam_nested:", type(fam_nested))    # <class 'list'>

# 7. Summary:
# - Lists let you store multiple values in one variable.
# - Lists are defined with square brackets [ ].
# - Lists can store any data type (even other lists).
# - The type of a list is <class 'list'>.
# - Lists are extremely useful in data science for storing datasets, features, etc.

# ➤ You’ll learn how to access and manipulate elements in a list in the next lessons.
