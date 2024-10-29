a = []
n = int (input ("enter the number of elements :"))
for i in range (n):
    element = int(input("enter element :"))
    a.append (element)
if n >1:
  temp = a [0]
a [0] = a [n-1]
a [n-1] = temp
print ("new list is : ",a)
