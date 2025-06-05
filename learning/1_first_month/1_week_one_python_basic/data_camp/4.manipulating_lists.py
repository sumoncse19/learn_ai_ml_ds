# -------------------------------------
# Manipulating Python Lists
# -------------------------------------

# Let's start with a sample list
fam = ["Liz", 1.73, "Emma", 1.68, "Mom", 1.71, "Dad", 1.89]
print("Original list:", fam)

# 1. Changing List Elements
# Suppose Dad's height was updated from 1.89 to 1.86
fam[7] = 1.86
print("Updated Dad's height:", fam)

# You can also change multiple elements using slicing
# Let's update Liz's name and height
fam[0:2] = ["Elizabeth", 1.75]
print("Updated Liz's name and height:", fam)

# 2. Adding Elements to a List
# Use + operator to combine lists
new_member = ["You", 1.80]
fam_ext = fam + new_member
print("Extended family list:", fam_ext)

# Note: The original fam list is not changed
print("Original fam list still unchanged:", fam)

# 3. Removing Elements from a List
# Use del keyword with index
del fam[2]  # Removes "Emma"
print("After deleting Emma:", fam)

del fam[2]  # Removes Emma's height (1.68)
print("After deleting Emma's height:", fam)

# 4. Behind the Scenes - List References
# What happens when you assign a list to a new variable?
x = [1, 2, 3]
y = x           # y points to the same list in memory as x
y[1] = 100      # Modify second element in y
print("x after changing y:", x)  # x is also changed

# Why? Because x and y both point to the same list object

# 5. Copying Lists Properly
# To create an actual copy (not just a reference), use list() or slicing
x = [1, 2, 3]
y = list(x)     # This creates a new list with the same values
y[1] = 999
print("x after copying with list():", x)
print("y after modification:", y)

# Alternatively, use slicing to copy
z = x[:]
z[0] = 555
print("x after slicing copy:", x)
print("z after modification:", z)

# Summary:
# - Change elements: list[index] = new_value
# - Change slices: list[start:end] = new_values_list
# - Add elements: list1 + list2
# - Remove elements: del list[index]
# - Assigning a list to another variable creates a reference, not a copy
# - Use list() or slicing to copy a list without linking their memory
# - For copying lists: either direct assignment (y = x) or using list() or slicing (y = list(x) or y = x[:])
# - If we copy a list using assignment, both variables point to the same memory location and changes in one will affect the other. Otherwise, they are independent.

# ➤ Next, you'll learn how to use list functions and methods to work smarter!
