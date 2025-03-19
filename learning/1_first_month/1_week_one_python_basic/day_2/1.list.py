# String or tuple --> immutable
# Start List --> Mutable
marks = [94.4, 97.6, 92, 90.2, 84.2]
        # 0     1     2    3    4
        # -5   -4    -3   -2   -1

print(marks)
print(len(marks))
print(marks[0])
print(marks[1])
print(marks[-3:-1])         # [92, 90.2]
print(type(marks))

student = ['Sumon', 93.5, 22, 'Bangladesh']
print(student[0])
student[0] = 'Rahman'       # Mutable
print(student[0])
print(student[:2])          # ['Rahman', 93.5]
