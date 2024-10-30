def fizzbuzzfxn(lowerlimit=1, upperlimit=100):
    for i in range(lowerlimit, upperlimit + 1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:  
            print("buzz")
        else:
            print(i)

fizzbuzzfxn()
fizzbuzzfxn(4, 7)


