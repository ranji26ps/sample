def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:  # Fixed here
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(sorted_list, target)
if result != -1:
    print(f"target found at index: {result}")
else:
    print("target not found")
