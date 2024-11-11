def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    largest = second_largest = float('-inf')  
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else -1



arr = [23, 12, 1, 10, 34, 13]
print(second_largest(arr))  

arr = [1, 1, 1, 1]
print(second_largest(arr))  

arr = [9]
print(second_largest(arr))  

