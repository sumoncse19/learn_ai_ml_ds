# -------------------------------------
# Subsetting and Slicing Python Lists
# -------------------------------------

# Let's reuse the mixed family list and nested list for this lesson
fam = ["Liz", 1.73, "Emma", 1.68, "Mom", 1.71, "Dad", 1.89]

# 1. Subsetting with Positive Index
# List indexes start at 0 in Python
# Example: To get Emma's height (4th item, index 3)
emma_height = fam[3]
print("Emma's height:", emma_height)

# To get the string "Dad" (7th element, index 6)
dad_label = fam[6]
print("Label:", dad_label)

# 2. Subsetting with Negative Index
# You can count from the end using negative indexes
# Example: -1 is the last element in the list (Dad's height)
dad_height = fam[-1]
print("Dad's height:", dad_height)

# Confirming that positive and negative indexing give the same result
print("Same value from two directions:", fam[7], "==", fam[-1])

# 3. List Slicing (Creating a sub-list)
# Syntax: list[start:end] -> includes start index, excludes end index

# Example: Get 4th, 5th, and 6th elements → index 3 to 5 (5 not included)
sub_list_1 = fam[3:5]
print("Sliced elements (index 3 to 5):", sub_list_1)

# Example: Get 2nd to 4th elements → index 1 to 4
sub_list_2 = fam[1:4]
print("Sliced elements (index 1 to 4):", sub_list_2)

# 4. Omitting start or end index in slicing

# Example: Slice from beginning to index 4 (4 not included)
start_slice = fam[:4]
print("Slice from beginning to index 4:", start_slice)

# Example: Slice from index 4 to end
end_slice = fam[4:]
print("Slice from index 4 to end:", end_slice)

# Summary:
# - Indexing lets you access single elements (e.g., fam[3])
# - Negative indexing starts from the end (e.g., fam[-1])
# - Slicing (e.g., fam[2:5]) creates a new list with a range of elements
# - The start index is included; the end index is excluded in slicing
# - Omitting start (`[:end]`) or end (`[start:]`) allows flexible slicing

# ➤ You’ll learn next how to manipulate lists (add/remove/change items).
