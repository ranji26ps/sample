def centered_triangle_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i, i + i):
            print(j, end=" ")
        print()
centered_triangle_pattern(4)
