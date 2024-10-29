str_input = input("Enter any string: ")
char_count = {}

for char in str_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Count of all characters in the entered string is:", char_count)
