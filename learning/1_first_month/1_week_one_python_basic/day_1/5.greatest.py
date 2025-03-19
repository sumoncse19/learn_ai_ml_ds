a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
c = int(input('Enter the third number:'))

if(a>b and a>c):
    print("First number is largest", a)
elif(b>a and b>c):
    print("Second number is largest", b)
elif(c>a and c>a):
    print("Third number is largest", c)
else:
    print("Both of them are equal")