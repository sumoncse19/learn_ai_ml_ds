str = 'Apna College'

str1 = 'apna'
len1 = len(str1)
print(len1)

str2 = 'college'
final_str = str1 + " " +str2
print(final_str)

print(len(final_str))


# Start indexing

"""
Apna_Colle g e
012345678910 11
"""

# Start Slicing
# str[strting_index:ending_index] --> ending index is not included
print(str[0:4])         # apna
print(str[5:12])        # 5 to last index of string
print(str[5:len(str)])  # 5 to last index of string
print(str[5:])          # 5 to last index of string --> [5:len(str)]
print(str[:4])          # start to before index 4 or till 4th index of string --> [0:4]
print(str[::2])         # It indicates every even indexed value or multiplier of ending value --> 0, 2, 4, 6, ...
print(str[::3])         # It indicates every even indexed value or multiplier of ending value --> 0, 3, 6, 9, ...
print(str[0:5:2])       # It indicates every even indexed value or multiplier of ending value from start_index(0) to "before end_index(5)" or "till index(4)"

# Slicing with negative index
"""
 A  p  p  l  e
-5 -4 -3 -2 -1
"""
negStr = "Apple"
print(negStr[-3:-1])   # pl
print(negStr[-5:-2])   # App

# Multiplied string
multStr = "Hello multiply "
print(3 * multStr)

# Adding blackslash
print("Md. sumon \n is best.")
print("Md. sumon \t is best.")
print("Md. sumon \ is best.")       # Output will be: Md. sumon \ is best.
print("Md. sumon \\ is best.")      # Output will be: Md. sumon \ is best.
print(r"Md. sumon \ is best.")      # Output will be: Md. sumon \ is best.


# String Function
str = "i am studying python from Apna College. This is the $ symbol, using like $99.99"
print(str.split())              # split the substring to list: ['i', 'am', 'studying', 'python', 'from', 'Apna', 'College.', 'This', 'is', 'the', '$', 'symbol,', 'using', 'like', '$99.99']
print(str.upper())
print(str.strip())
print(str.endswith("ege"))      # True or False
print(str.capitalize())         # Make upper the first letter.
print(str.replace("o", "a"))    # Replace a character or letter with another of a string.
print(str.replace("python", "javascript"))
print('Find character with st indexing point:', str.find("st"))   # Return the first index number of str. --> 2, if it is not available then i'll be return -1
print('Count a:', str.count("a"))   # Count How many exact character or letter has in this string?

print('Dollar count:', str.count("$"))
name = input("Your first name: ")
age = int(input("Enter your age: "))
print(f"Your name is: {name} and your age is: {age}")
print("Your name is: {} and your age is: {}".format(name, age))
print("Your name is: %s and your age is: %d"%(name, age))


## Additional capabilities
# F-strings are also able to evaluate expressions inside the curly braces, which can be very handy. For example:
x = 10
y = 20
print(f"The sum of x and y is {x+y}.")

## Raw String (r’’)
regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)
'''
It's output will be like this:
Regular String: C:
ew_folder
         ile.txt
'''
# If we want to as like as given string? then we have to use raw string like this:
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)