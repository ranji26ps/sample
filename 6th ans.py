num = int(input("Enter a number here: "))
if num < 1:
    print("Please enter a positive integer.")
elif num == 1:
    print("It is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Check up to the square root of num
        if num % i == 0:
            print("It is not a prime number.")
            is_prime = False
            break
    if is_prime:
        print("It is a prime number.")
