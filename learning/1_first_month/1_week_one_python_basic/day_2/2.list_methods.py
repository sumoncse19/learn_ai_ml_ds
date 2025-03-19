list = [2, 1, 3]
list.append(4)
# print(list.append(4))     # It's return None, it only add.
print(list)         # [2, 1, 3, 4]

list.insert(1, 5)   # [2, 5, 1, 3, 4]
print(list)

list.sort()
print(list)         # [1, 2, 3, 4]

list.sort(reverse=True)
print(list)         # [4, 3, 2, 1]

listOfChar = ['a', 'beep', 'c', 'banana', 'b', 'f', 'e', 'd']
listOfChar.sort()
print(listOfChar)   # ['a', 'b', 'banana', 'beep', 'c', 'd', 'e', 'f']
listOfChar.reverse()
print(listOfChar)   # ['f', 'e', 'd', 'c', 'beep', 'banana', 'b', 'a']