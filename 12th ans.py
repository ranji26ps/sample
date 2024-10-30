length = int(input("Enter a list length: "))
numbers_list = []

for i in range(length):
    temp = int(input("Enter a list item: "))
    numbers_list.append(temp)  # Move this line inside the loop

if len(numbers_list) < 2:
    print("List needs at least two distinct numbers.")
else:
    first_largest, second_largest = float('-inf'), float('-inf')

    for item in numbers_list:
        if item > first_largest:
            second_largest = first_largest
            first_largest = item
        elif item > second_largest and item != first_largest:  
            second_largest = item

    if second_largest == float('-inf'):
        print("There is no second largest number (all numbers might be the same).")
    else:
        print("Second largest number in the list:", second_largest)
