#name=input("please \nenter \nyour \nname")
#check="hope you are okay"
#greetings="hello " + name + check
#print(greetings)

#functions in strings
confession="I love God"
print(confession.lower())
print(confession.upper())
print(confession.islower())
print(confession.upper().isupper())
print(len(confession))
print(confession[4])
print(confession.index("God"))

#numbers
#cool things to do with numbers
number=-50
print(str(number))

from math import*
print(abs(number))
print(pow(12,6))
print(max(5,83,86,25,9,100.193))
print(min(5,83,86,25,9,100.193))
print(sqrt(169))
print(round(54.6))
print(floor(54.6))
print(ceil(54.6))

#building a simple calculator
num1=input("Enter a number")
num2=input("Enter another number")
result=float(num1)+float(num2)
print("your result is: " + str(result))








