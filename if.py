#if statements

is_late=False
is_good=True

if is_late:
    print("Arnold is late and is given a punishment")

#if else statement
if is_late:
    print("Arnold is late and he deserves a punishent")
else:
    print("Arnold doesnt deserve a punishment")

if is_late and is_good:
    print("Arnold is late but forgiven because he is a good student")
else:
    print("Arnold is either not late or not good or not both")

#elif statement
goto_school=False
stay_home=False
if goto_school:
    print("i will do my exercise")
elif stay_home:
    print("i will do house chores")
else:
    print("i go to the market")

#Improved calculator
option=input("please enter what you would like to do:enter;\nadd for addition\nsub for subtraction\nmul for multiplication\ndiv for division")
if option== "add":
    num1=input("enter a number")
    num2=input("enter another number")
    result=float(num1)+float(num2)
    print("your result is: "+ str(result))
elif option== "sub":
    num1=input("enter a number")
    num2=input("enter another number")
    result=float(num1)-float(num2)
    print("your result is: "+ str(result))
elif option== "mul":
    num1=input("enter a number")
    num2=input("enter another number")
    result=float(num1)*float(num2)
    print("your result is: "+ str(result))
elif option== "div":
    num1=input("enter a number")
    num2=input("enter another number")
    result=float(num1)/float(num2)
    print("your result is: "+ str(result))
else:
    print("please select and enter one of the above options")


