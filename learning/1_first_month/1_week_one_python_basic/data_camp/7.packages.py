# Summary: Python Packages

# Python functions and methods let you reuse powerful, tested code.
# But including *everything* in Python by default would be messy and inefficient.

# 1. What Are Packages?
# - Packages = directories of Python modules (scripts).
# - Modules contain functions, methods, and new types for specific tasks.
# - Examples:
#   - NumPy → efficient arrays
#   - Matplotlib → data visualization
#   - scikit-learn → machine learning
# - These are not built-in and need to be installed.

# 2. Installing Packages
# - Use `pip` to install external packages:
# - On your terminal:
#   $ python3 get-pip.py       # Installs pip (if not already installed)
#   $ pip3 install numpy       # Installs NumPy for Python 3

# 3. Importing Packages
# - After installation, you must **import** the package into your script.

# a. Import the entire package:
import numpy
print(numpy.array([1, 2, 3]))  # Output: [1 2 3]

# b. Use an alias (shorter name) with `as`:
import numpy as np
print(np.array([4, 5, 6]))  # Output: [4 5 6]

# c. Import a specific function directly:
from numpy import array
print(array([7, 8, 9]))  # Output: [7 8 9]

# 4. Pros and Cons
# - `import numpy` keeps context clear → `numpy.array()`
# - `from numpy import array` is shorter, but context is lost in long scripts
#   (reader may not realize `array()` is from NumPy)

# 5. Best Practices
# - Use `import numpy as np` — it's readable and concise.
# - Avoid `from ... import ...` unless you're sure it's clear and limited.

# Let’s move to exercises to practice installing and importing packages!
