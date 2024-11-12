def find_closest_sum_to_zero(arr):
    if len(arr) < 2:
        return None
    arr.sort()

    left = 0
    right = len(arr) - 1
    closest_sum = float('inf')
    closest_pair = None
    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            closest_pair = (arr[left], arr[right])
        if current_sum < 0:
            left += 1  
        elif current_sum > 0:
            right -= 1  
        else:
            break  

    return closest_pair, closest_sum
arr = [-1, 2, 1, -4]
pair, sum_value = find_closest_sum_to_zero(arr)
print(f"The pair with the sum closest to zero is {pair} with a sum of {sum_value}.")
