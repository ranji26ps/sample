def fizzbuzzfxn (lowerlimit=1, Upperlimit=100):
    for i in range(lowerlimit,Upperlimit +1):
     if i % 15 == 0 :
        print ("fizzbuzz")
     elif i % 3 == 0 :
        print ("fizz")
    else:
       print(i)
fizzbuzzfxn()
fizzbuzzfxn(4,7)

