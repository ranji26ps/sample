arr = [12,35,1,10,34,1]
lar = arr[0]
for i in range (1,len(arr)):
    if arr[i] > lar:
       lar = arr[i]
print(lar)