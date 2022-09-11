
"""1.Create a 2-D array and slice out the second number in the second column"""
my_array=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print(my_array[1][1])

"""2.Write a python program to sort array element in the ascending/descending order"""

score=[47,26,69,90,75,34]
score.sort()
print(score)
my_friends=["maria","tonny","arianah","bashir","travor"]
my_friends.sort()
print(my_friends)
score2=[47,26,69,90,75,34]
score2.sort(reverse=True)
print(score2)

"""3.Write a python program to find the maximum and minimum value in a given 2-D array"""

import numpy as np
my_array=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print(np.min(my_array))
print(np.max(my_array))

"""4.Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
percentage less than 50 (Grade C)
percentage equal to 50 and less than 80 (Grade B)
percentage equal to 80 and more than 80 (Grade A)"""
sub_mark_counter=1
total_marks=0
while sub_mark_counter<=5:
    subject_mark=float(input("Enter a subject mark"))
    total_marks=total_marks+subject_mark
    sub_mark_counter +=1
print(total_marks)
percentage=(float(total_marks)/500)*100
print(percentage)
if percentage<50:
    print("grade is C")
elif percentage==50 or percentage<80:
    print("grade is B" )
else:
    print("grade is A")

"""5.Write a python program to fetch only Email ID from text file which include following fields -:
Name
Mobile Number
Roll Number
Email ID
"""
about_me=open("knowme.txt", "r")
read=about_me.readlines()
for line in read:
    if "@" in line:
         print(line)
about_me.close()


"""6.Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
"""
def check_speed(speed):
    if speed<70:
        print("ok")
    
    speed_limit=70
    total_km=0
    while speed_limit>70:
        km=float(input("enter number of km above speed limit"))
        demerit_point=0
        if km>=5:
            print("you have a demerit point")
            demerit_point +=1
        print("you are below speed limit")
    print(demerit_point)
    if demerit_point>11:
        print("licence cancelled")



"""7.Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****
"""
def show_stars(rows):

    for i in range(rows+1):
        for j in range(i):
            print( "*", end= " ")
        print("")

show_stars(5)

"""8.Write a program which will find all such numbers which are divisible
 by 7 but are not a multiple of 5 between 2000 and 3200 (both included). 
 The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
list=[x for x in range(2000,3201) if x%7==0 and x%5!=0]
print(list)

    
"""9.Write a program which accepts a sequence of comma-separated 
numbers from console and generate a list and a tuple which 
contains every number. Suppose the following input is supplied 
to the program: 34,67,55,33,12,98 Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
numbers=input("Enter comma-separated numbers")
list=numbers.split(",")
tuple=tuple(list)
print(list)
print(tuple)

"""10.Write a program that calculates and prints the value according 
to the given formula: Q = Square root of [(2 * C * D)/H] Following 
are the fixed values of C and H: C is 50. H is 30. D is the variable
 whose values should be input to your program in a comma-separated sequence. 
 Example Let us assume the following comma separated input sequence is
  given to the program: 100,150,180 The output of the program should be: 18,22,24
"""
from math import sqrt
D=input("enter a comma-seperated sequence of numbers")
list=[int(item) for item in D.split(",")]
for i in range(len(list)):
    Q=sqrt((2*50*i)/30)
    print(Q)

"""11.Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
try:
    def division(a,b):
        return(a/b)
    result=division(5,0)
    print(result)
except:
    print("zero division error")

"""12.Create a nesting list that prints out the color and the car brand.
"""
car_color_brand=[["blue","white","black"],["ranger","ford","vitz"]]
car_color=car_color_brand[0][1]
car_brand=car_color_brand[1][1]
print("The " + car_color + " car is a " + car_brand)
    
"""13.Bonus Question: 
Algorithm challenge: Create your own sorting algorithm.
"""
list=input("Enter a sequence of numbers seperated by commas")
new_list=[int(item) for item in list.split(",")]
for i in range(0,len(new_list)):
    for j in range(0,len(new_list)-i-1):
        if new_list[j] > new_list[j+1]:
            swap=new_list[j]
            new_list[j]=new_list[j+1]
            new_list[j+1]=swap
print(new_list)

    
    



    
  