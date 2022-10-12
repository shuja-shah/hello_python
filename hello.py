from email import message


def greetings(name, message):
    print("Hello", name, message)

name=input("Please Enter Your Name: ")
message=input("Message: ")

greetings(name, message)