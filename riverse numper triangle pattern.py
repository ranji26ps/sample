def centre(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print("", end="")
        for j in range(i, n + 1):
            print(j, end="")
        print()

centre(4)
