for i in range(1,31,1):
    if not i % 15 == 0 and i % 3 == 0:
        print("fizz")
    elif not i % 15 == 0 and i % 5 == 0:
        print("buzz")
    elif i % 15 == 0:
        print("FizzBuss")
    else:
        print(i)
