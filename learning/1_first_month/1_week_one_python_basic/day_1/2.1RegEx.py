## RegEx

'''
In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings. 

`This RegEx module provides several functions for working with regular expressions, including <code>search, split, findall,</code> and <code>sub</code>.`

`Python provides a built-in module called <code>re</code>, which allows you to work with regular expressions. 
First, import the <code>re</code> module`
'''

import re
# --------> Problem 1 Start <--------
str1 = "Michael Jackson is the best"

searchText = r"Jackso"

isFound = re.search(searchText, str1)

if isFound:
    print(f"{searchText} found!")
else:
    print(f"{searchText} not found.")

# --------> Problem 1 End <--------


# --------> Problem 2 Start <--------
'''
The regular expression pattern is defined as r"\d\d\d\d\d\d\d\d\d\d", which uses the \d special sequence to match any digit character (0-9), and the \d sequence is repeated ten times to match ten consecutive digits
'''
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# --------> Problem 2 End <--------


# --------> Problem 3 Start <--------
'''
A simple example of using the \W special sequence in a regular expression pattern with Python code:

The regular expression pattern is defined as r"\W", which uses the \W special sequence to match any character that is not a word character (a-z, A-Z, 0-9, or _). The string we're searching for matches in is "Hello, world!".
'''
pattern = r"\W"  # Find any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

# --------> Problem 3 End <--------


# --------> Problem 4 Start <--------
'''The findall() function finds all occurrences of a specified pattern within a string.'''
str2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", str2)

# Print out the list of matched words
print(result)

# --------> Problem 4 End <--------


# --------> Problem 5 Start <--------
'''A regular expression's split() function splits a string into an array of substrings based on a specified pattern.'''
# Use the split function to split the string by the "\s"
split_array = re.split("/s", str2)
split_array2 = re.split("/", str2)
split_array3 = re.split(" ", str2)

# The split_array contains all the substrings, split by whitespace characters
print('After split with /s', split_array)
print('After split with /', split_array2)
print("After split with space(' ')", split_array3)

# --------> Problem 5 End <--------


# --------> Problem 6 Start <--------
'''The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.'''
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, str2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 

# --------> Problem 6 End <--------


# --------> Problem 7 Start <--------
'''In the string s3, find whether the digit is present or not using the \d and search() function:'''
s3 = "House number- 1105"
isPresent = re.search("\d", s3)
if isPresent:
    print("Digit found")
else:
    print("Digit not found.")

# --------> Problem 7 End <--------


# --------> Problem 8 Start <--------
'''In the string replace_with_sub, replace the sub-string fox with bear using sub() function:'''
replace_with_sub= "The quick brown fox jumps over the lazy dog."

# Write your code below and press Shift+Enter to execute
pattern = r"fox"
replace_with = "bear"

after_replace = re.sub(pattern, replace_with, replace_with_sub, flags=re.IGNORECASE)

print(after_replace)

# Here in sub function fourth parameter is optional parameter.

# --------> Problem 8 End <--------


# --------> Problem 9 Start <--------
'''In the string findall_str find all the occurrences of woo using findall() function:'''
findall_str="How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"

results = re.findall('woo', findall_str)

print(results)

# --------> Problem 9 End <--------

