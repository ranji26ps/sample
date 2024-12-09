n = int(input("Enter the number of Fibonacci series terms: "))
f1, f2 = 0, 1

if n <= 0:
    print()
elif n == 1:
    print(f1)
elif n == 2:
    print(f1, f2)
else:
    print(f1, f2, end=" ")
    for i in range(3, n + 1):
        f3 = f1 + f2
        print(f3, end=" ")
        f1 = f2
        f2 = f3
