age = int(input("Enter your age:"))

if(age >= 18):
    print("You can apply for license!")
elif(age >=16):
    print("You can drive!")
else:
    print("You are not eligable!")
    
marks = int(input("Enter your marks:"))
if(marks >= 90):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print("Grade B")
elif(marks >= 70):
    print("Grade C")
elif(marks < 70):
    print("Grade D")