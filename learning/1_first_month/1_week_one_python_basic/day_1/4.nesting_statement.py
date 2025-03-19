age = int(input("Enter your age:"))

if(age%2==0):
    print("Age is even number")
else:
    print("Age is odd number")

if(age >= 16):
    if(age >= 18):
        print("You can apply for license")
    print("You can drive!")
else:
    print("You are not eligable!")