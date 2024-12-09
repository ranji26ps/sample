num = int(input("enter a numpeer"))
if num == 1 :
    print("it is a not prime nummper")
if num > 1:
    for i in range (2,num):
        if num % i == 0:
            print("not a prime")
            break
        else:
            print("is a prime")
