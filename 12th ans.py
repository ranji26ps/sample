length = int(input("enter a list length:"))
numbers_list = []
for i in range(length):
  temp = int(input("Enter a list item: "))
numbers_list.append(temp)
first_largest,second_largest = numbers_list[0],numbers_list[0]
for item in numbers_list:
    if item > first_largest:
        second_largest = first_largest
        first_largest = item
    elif item > second_largest and item == first_largest:
                     second_largest = item
print ("second_largest number in a list :",second_largest)
