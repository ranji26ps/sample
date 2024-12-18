n=4

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
n= n-1
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()