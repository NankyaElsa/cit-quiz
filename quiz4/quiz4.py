#number1
my_array=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print(my_array[1][1])

#number2
score=[47,26,69,90,75,34]
score.sort()
print(score)
my_friends=["maria","tonny","arianah","bashir","travor"]
my_friends.sort()
print(my_friends)

#number3
import numpy as np
my_array=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print(np.min(my_array))
print(np.max(my_array))

#number4
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

#number5
# about_me=open("knowme.txt", "w")
# about_me.write["Elsa\n+256-757291160\n354\nelsakayigwa@gmail.com"]
# about_me.close()

# about_me=open("knowme.txt", "r")
# print(about_me.readline()[-1])
# about_me.close()

#number7
def show_stars(rows):
    t=rows-1
    for i in range(0, rows):
        for j in range(0,t):
            print(end= " ")
        t-=1
        for j in range (0, i+1):
            print("*", end=' ')
        print("\n")

rows=int(input())
show_stars(5)

#number8


    
        
    

    
  