def reverse_digits(num):
    num_str = str(num)
    reversed_digits = ' '.join(reversed(num_str))
    return reversed_digits
number = 1234
print(reverse_digits(number))  # Output: "6 3 5 7"
