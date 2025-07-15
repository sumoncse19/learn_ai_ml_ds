# Summary: NumPy for Numerical Computing in Python

# 1. Python Lists Recap
# - Lists can hold mixed types, and allow adding/removing/changing elements.
# - BUT: Lists do not support fast, element-wise operations.
#   Example: You cannot divide one list by another directly.

# 2. The Problem: BMI Calculation with Lists
height = [1.73, 1.68, 1.71, 1.89]
weight = [65.4, 59.2, 63.6, 88.4]

# This would cause an error:
# bmi = weight / (height ** 2)

# 3. Solution: Use NumPy Arrays
# - NumPy arrays allow efficient, vectorized operations on entire datasets.
# - You can install NumPy using pip:
#   $ pip3 install numpy

# - Import NumPy in your script
import numpy as np

# - Convert lists to NumPy arrays
np_height = np.array(height)
np_weight = np.array(weight)

# - Calculate BMI with vectorized operation (element-wise)
bmi = np_weight / np_height ** 2
print(bmi)  # Output: [21.852, 20.957, 21.757, 24.735]

# 4. Comparison: List vs NumPy Array Operations
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

print(python_list + python_list)  # Output: [1, 2, 3, 1, 2, 3]
print(numpy_array + numpy_array)  # Output: [2 4 6]

# 5. Important Notes on NumPy Arrays
# - Arrays must contain a single type (float, int, str, etc.)
mixed_array = np.array([True, 1.68, "data"])
print(mixed_array)  # Output: ['True' '1.68' 'data'] — all converted to strings

# - NumPy arrays are a new Python type with their own methods

# 6. Subsetting NumPy Arrays
# - Standard subsetting using square brackets:
print(bmi[1])  # Output: BMI of 2nd person

# - Boolean subsetting: get all BMI values > 23
high_bmi = bmi[bmi > 23]
print(high_bmi)  # Output: [24.735]

# - `bmi > 23` returns a boolean array:
#   [False, False, False, True]

# 7. Summary
# - NumPy arrays allow fast, element-wise computations
# - Be careful: behavior differs from regular Python lists
# - Powerful subsetting and filtering options
# - Essential for data science and numerical analysis

# 8. Practice Time!
# - Use exercises to reinforce NumPy basics and learn powerful array techniques.
