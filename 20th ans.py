def recursive_fibonacci(n):
    
    if n <= 1:
        return n
    
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def print_fibonacci_series(n_terms):
    
    if n_terms <= 0:
        print("Invalid input, please input a positive value.")
    else:
        print("Fibonacci series:")
        for i in range(n_terms):
            print(recursive_fibonacci(i), end=" ")


n_terms = 10
print_fibonacci_series(n_terms)
