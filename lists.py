#lists are used to store a banch of items in a single variable or at the same place
#lists can be mae up of both numbers and strings

#fruits=["mango","orange", "quava", "lemon", "grapes"]
# marks=[40, 82, 47, 89,59]
# index=0
# total=0
# while index < len(marks):
#     total=total+marks[index]
#     index +=1
# print(total)

#adding the two lists together into one string
#fruits.extend(marks)
#print(fruits)

#other cool functions with lists
# marks.sort()
# print(marks)
# fruits.append(76)
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.reverse()
# print(fruits)

# #accessing elements in lists
# print(len(marks))
# print(fruits[4])
# print(fruits.index("quava"))
# fruits.insert(0,"jackfruit")
# print(fruits)
# fruits[4]="banana"
# print(fruits)
# list=[x for x in range(2000,3201) if x%7==0 and x%5!=0 ]
# print(list)
from math import sqrt
D=input("enter a comma-seperated sequence of numbers")
list=[int(item) for item in D.split(",")]
for i in range(len(list)):
    Q=2*50*i
    p=Q/30
    print(p)