#creating and writing in a text file using python
about=open("aboutme.txt", "w")
about.write("My name is Elsa\nI am 20 years old\nIam a girl\nI like dancing")
about.close()

#reading from a file
know_something=open("aboutme.txt", "r")
print(know_something.readable())
print(know_something.read())
print(know_something.readline())
know_something.readline()[0]
print(know_something.readlines())
know_something.close()

#appending to a file
# about=open("aboutme.txt", "a")
# about.write("\nI am a software engineering student")
# about.close()


