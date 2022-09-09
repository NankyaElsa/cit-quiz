#lists are used to store a banch of items in a single variable or at the same place
#lists can be mae up of both numbers and strings

fruits=["mango","orange", "quava", "lemon", "grapes"]
marks=[40, 82, 47, 89,59]

#adding the two lists together into one string
#fruits.extend(marks)
#print(fruits)

#other cool functions with lists
marks.sort()
print(marks)
fruits.append(76)
print(fruits)
fruits.pop()
print(fruits)
fruits.reverse()
print(fruits)

#accessing elements in lists
print(len(marks))
print(fruits[4])
print(fruits.index("quava"))
fruits.insert(0,"jackfruit")
print(fruits)
fruits[4]="banana"
print(fruits)
