#  Operators in Python

# Arithmetic Operators in Python --> +, -, *, /, //, %, **
a = 10
b = 3
print("Addition:", a + b)           # 13
print("Subtraction:", a - b)        # 7
print("Multiplication:", a * b)     # 30
print("Division:", a / b)           # 3.3333333333333335
print("Floor Division:", a // b)    # 3
print("Modulus:", a % b)            # 1
print("Exponentiation:", a ** b)

# Relational/Comparison Operators --> ==, !=, >, <, >=, <=
x = 5
y = 10
print("Equal to:", x == y)              # False
print("Not equal to:", x != y)          # True
print("Greater than:", x > y)           # False
print("Less than:", x < y)              # True
print("Greater than or equal to:", x >= y)  # False
print("Less than or equal to:", x <= y)     # True

# Assignment Operators --> =, +=, -=, *=, /=, %=
c = 5
c += 2  # c = c + 2
print("After += :", c)  # 7
c -= 3  # c = c - 3
print("After -= :", c)  # 4
c *= 4  # c = c * 4
print("After *= :", c)  # 16
c /= 2  # c = c / 2
print("After /= :", c)  # 8.0
c %= 3  # c = c % 3
print("After %= :", c)  # 2.0

# Logical Operators --> and, or, not
p = True
q = False
print("Logical AND:", p and q)  # False
print("Logical OR:", p or q)    # True
print("Logical NOT:", not p)     # False

print ((5 > 3) and (2 < 4))  # True
print ((5 > 3) or (2 > 4))   # True
print (not (5 > 3))          # False

# Bitwise Operators --> &, |, ^, ~, <<, >>
m = 5  # 0101 in binary
n = 3  # 0011 in binary
print("Bitwise AND:", m & n)   # 1 (0001 in binary)
print("Bitwise OR:", m | n)    # 7 (0111 in binary)
print("Bitwise XOR:", m ^ n)   # 6 (0110 in binary)
print("Bitwise NOT:", ~m)      # -6 (inverts bits)
print("Left Shift:", m << 1)   # 10 (1010 in binary)
print("Right Shift:", m >> 1)  # 2 (0010 in binary

# Membership Operators --> in, not in
my_list = [1, 2, 3, 4, 5]
print("Is 3 in list?", 3 in my_list)          # True
print("Is 6 not in list?", 6 not in my_list)  # True

# Identity Operators --> is, is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)          # True
print("a is c:", a is c)          # False
print("a is not c:", a is not c)  # True

# Operators Precedence --> (BODMAS)
"""
Operator Precedence in Python (from highest to lowest):
(),
**,
*, /, //, %,
+, -,
==, !=, >, <, >=, <=,
not,
and,
or
"""

"""
Same precedence level operators are evaluated from left to right.
"""

result = 3 + 5 * 2  # Multiplication has higher precedence than addition
print("Result of 3 + 5 * 2:", result)  # 13
result = (3 + 5) * 2  # Parentheses change the precedence
print("Result of (3 + 5) * 2:", result)  # 16
result = not True and False  # 'not' has higher precedence than 'and'
print("Result of not True and False:", result)  # False

# Same precedence level operators evaluated left to right
result = 10 - 2 + 3  # Both - and + have same precedence
print("Result of 10 - 2 + 3:", result)  # 11

# Type Conversion --> Compatible types can be converted
"""
Type Conversion in Python:
1. Implicit Type Conversion: Python automatically converts one data type to another without user intervention.
2. Explicit Type Conversion: User manually converts one data type to another using built-in functions like int(), float(), str(), etc.

Type Casting Functions:
- int(): Converts a value to an integer.
- float(): Converts a value to a floating-point number.
- str(): Converts a value to a string.
"""

# Type Conversion Examples --> Implicit Type Conversion
int_num = 10      # Integer
float_num = 2.5        # Float
result = int_num + float_num  # int is converted to float
print("Result of implicit conversion (int + float):", result)  # 12.5
print("Type of result:", type(result))  # <class 'float'>

# Type Casting Examples --> Explicit Type Conversion
str_num = "20"
int_converted = int(str_num)  # Convert string to integer
print("Converted string to integer:", int_converted)  # 20
float_converted = float(str_num)  # Convert string to float
print("Converted string to float:", float_converted)  # 20.0
str_converted = str(15.5)  # Convert float to string
print("Converted float to string:", str_converted)  # "15.5"

type_casting = int(5 + 10.0)  # Converts float to int (truncates decimal part) --> Developer's choice
type_conversion = 5 + 10.0  # Implicitly converts int to float
print("Type casting result:", type_casting)        # 15
print("Type conversion result:", type_conversion)    # 15.0

# Converting incompatible types will raise an error
# invalid_conversion = int("Hello")  # This will raise a ValueError 

# To avoid errors, ensure the data is compatible before conversion
valid_str_num = "30"
valid_int = int(valid_str_num)  # This works fine
print("Valid conversion of string to integer:", valid_int)  # 30

# User Input
a = input("Enter a number: ")  # Input is taken as string
b = input("Enter another number: ")
# To perform arithmetic, convert inputs to integers or floats --> Through user's choice
operator = input("Enter '+' to add the numbers: ")
if operator == '+':
    sum_result = int(a) + int(b)  # Explicit conversion to int
    print("Sum of the numbers is:", sum_result)
elif operator == '-':
    diff_result = float(a) - float(b)  # Explicit conversion to float
    print("Difference of the numbers is:", diff_result)
elif operator == '*':
    prod_result = int(a) * int(b)  # Explicit conversion to int
    print("Product of the numbers is:", prod_result)
elif operator == '/':
    div_result = float(a) / float(b)  # Explicit conversion to float
    print("Division of the numbers is:", div_result)
else:
    print("Unsupported operation.")


# Problem: Print the average of 2 numbers:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

average = float(num1) + float(num2) / 2  # Explicit conversion to float
print("Average of the two numbers is:", average)