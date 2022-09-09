# def outer_fun(a,b):
#     def inner_fun(c,d):
#         return c+d
#     return inner_fun(a,b)
# result=outer_fun(5,10)
# print(result)


# #number5
# def display(**kwargs):
#     for i in kwargs:
#         print(i)
# display(emp="Kelly",salary=9000)
# 

# def some_thing(number1,number2):
#     first_value=number1+8
#     second_value=number2-5
#     temp_value=other_thing(second_value)
#     return temp_value
# def other_thing(another_value):
#     return(another_value +5)*3
# some_thing(13,10)
# print(second_value)

# 
def outer_fun(a,b):
    def inner_fun(c,d):
        return c+d
    return inner_fun(a,b)
res=outer_fun(5,10)
print(res)

        

