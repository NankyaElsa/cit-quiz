# the try except function catches errors in your program
# try:
#     def error():
#         print("you made an error")
#     error()
# except SyntaxError:
#                      print("wrong syntax")



try:
    number=int(input("enter a number"))
except:
    print("enter a valid") 
print(number)                      