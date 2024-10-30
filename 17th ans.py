def get_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print("Error: Please enter exactly the number of columns specified.")
            return None
        matrix.append(row)
    return matrix
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(result_row)
    return result
def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix1 = get_matrix(rows, cols)
    if matrix1 is None:
        return
    matrix2 = get_matrix(rows, cols)
    if matrix2 is None:
        return
    result = add_matrices(matrix1, matrix2)
    print("Resultant Matrix after Addition:")
    for row in result:
        print(" ".join(map(str, row)))
if __name__ == "__main__":
    main()
