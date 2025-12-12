# Problem 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Explicit conversion to int

print(f"Hello {name}, You are {age} years old!")

# Problem 2 --> Ask the user to enter two integers and one float. Convert them all to floats and print their average
a = int(input("Enter first intiger number: "))  # Explicit conversion to int
b = int(input("Enter second intiger number: "))  # Explicit conversion to int
c = float(input("Enter third float number: "))  # Explicit conversion to float

average = (float(a) + float(b) + c) / 3  # Explicit conversion to float
print("The average of the 3 numbers is:", average)

# Problem 3 --> Write a program to swap values of two numbers entered by the user.
x = input("Enter first number (x): ")
y = input("Enter second number (y): ")

# Swapping using a temporary variable
temp = x
x = y
y = temp
print("After swapping:")
print("x =", x)
print("y =", y)