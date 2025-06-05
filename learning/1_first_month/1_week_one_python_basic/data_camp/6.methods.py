# Summary: Python Methods

# This video explains methods in Python — functions that belong to objects.

# 1. Built-in Functions vs Methods
# - Built-in functions: like max(), len(), type(), round()
# - Some operations (like finding an element's index or reversing a list) are not available as built-in functions but as **methods**.

# 2. Objects and Types
# - Everything in Python is an object: strings, floats, lists, etc.
# - Each object has a type (e.g., str, float, list) and comes with built-in methods specific to that type.

# 3. List Methods Example
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71]

# Get index of "mom"
print(fam.index("mom"))  # Output: 4

# Count how many times 1.73 appears
print(fam.count(1.73))   # Output: 1

# 4. String Methods Example
sister = "liz"

# Capitalize first letter
print(sister.capitalize())  # Output: Liz

# Replace a character
print(sister.replace("z", "sa"))  # Output: lisa

# 5. Object Types Define Method Availability
# - Only certain methods are available on specific types.
# - For example, strings have `replace`, but lists do not.

# This would raise an error:
# fam.replace("liz", "lisa")  # AttributeError: 'list' object has no attribute 'replace'

# 6. Same Method Name on Different Types
# - Methods like `index()` exist on both strings and lists, but behave differently based on object type.

print("hello".index("e"))  # Output: 1
print(fam.index("emma"))   # Output: 2

# 7. Methods That Modify Objects
# - Some methods change the object they are called on.
# - Example: append() modifies the list in-place.

fam.append("me")
print(fam)  # Output: ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'me']

fam.append(1.75)
print(fam)  # Output: [..., 'me', 1.75]

# 8. Summary
# - Functions like max() and type() are general-purpose.
# - Methods are object-specific functions, called with dot notation.
# - Different types have different available methods, and behavior can vary.
# - Some methods modify the original object (like append), while others return a new one (like replace).
