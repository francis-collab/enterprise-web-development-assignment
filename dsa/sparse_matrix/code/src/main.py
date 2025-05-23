def main():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
    try:
        choice = int(input("Enter choice: "))

        matrixA = SparseMatrix("/dsa/sparse_matrix/sample_inputs/matrixA.txt")
        matrixB = SparseMatrix("/dsa/sparse_matrix/sample_inputs/matrixB.txt")

        if choice == 1:
            result = add_matrices(matrixA, matrixB)
            write_matrix_to_file(result, "/dsa/sparse_matrix/sample_outputs/sum_matrix.txt")
        elif choice == 2:
            result = subtract_matrices(matrixA, matrixB)  # ✅ Fixed subtraction call
            write_matrix_to_file(result, "/dsa/sparse_matrix/sample_outputs/diff_matrix.txt")
        elif choice == 3:
            result = multiply_matrices(matrixA, matrixB)
            write_matrix_to_file(result, "/dsa/sparse_matrix/sample_outputs/prod_matrix.txt")
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
