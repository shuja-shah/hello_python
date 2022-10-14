''' This is main Func of The Fizz buzz Challange'''

def fizzy(lists):
    ''' This takes a list of Ints and returns either FIzz Or Buzz'''
    for i in lists:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

            