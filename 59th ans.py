a = int(input("enter a year"))
if a % 400 == 0:
    print("is a  leap")
elif a % 100 == 0:
    print("is a leap")
elif a  % 4 == 0:
    print("is a leap")
else:
    print("is a not leap")
