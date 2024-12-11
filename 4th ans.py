s = int(input("Enter the needed fibonacci series"))
s1 = 0
s2 = 1
if s == 1:
    print(s1)
elif s == 2:
    print(s1," ",s2)
else:
    print(s1,s2,end=" ")
    for i in range(3,s+1):
        s3 = s1 + s2
        print(s3,end=" ")
        s1 = s2 
        s2 = s3