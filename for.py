#for loop
# from operator import index


# names=["Elsa", "Arnold", "Anitah","Andrew","Arianah"]
# #for name in names:
# for name in range(len(names)):
#     print(names[name])

# #2d arrays/lists with nested for loop
# number_grid=[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# print(number_grid[1][2])

# for row in number_grid:
#     #print(row)
#     for col in row:
#         print(col)

#creating an exponential function
#def raise_a_power(base_num, power):
    #result=1
    #for index in range(power):
        #result=base_num*power
#print("result")
def show_stars(rows):

    for i in range(rows+1):
        for j in range(i):
            print( "*", end= " ")
        print("")

show_stars(5)