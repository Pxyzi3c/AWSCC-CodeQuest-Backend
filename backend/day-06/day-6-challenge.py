limit = int(input("Limit: "))
fizz = 3
buzz = 5

i = 1
while i <= limit:
    if (i % fizz == 0) and (i % buzz == 0):
        print("FizzBuzz!")
    elif i % fizz == 0:
        print("Fizz")
    elif i % buzz == 0:
        print("Buzz")
    else: 
        print(i)
    i += 1