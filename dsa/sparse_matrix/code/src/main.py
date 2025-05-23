# main.py

from src.ile_handler import read_matrix_from_file, write_matrix_to_file
from src.matrix_operations import add_matrices, subtract_matrices, multiply_matrices
import sys

def main():
    sample_inputs = [
        "easy_sample_01_2.txt",
        "easy_sample_01_3.txt",
        # Add more input files here manually if needed
    ]

    print("Available sample input files:")
    for i, fname in enumerate(sample_inputs, start=1):
        print(f"{i}. {fname}")

    try:
        idx1 = int(input("Select the first matrix file by number: ").strip())
        idx2 = int(input("Select the second matrix file by number: ").strip())
        if idx1 < 1 or idx1 > len(sample_inputs) or idx2 < 1 or idx2 > len(sample_inputs):
            print("Invalid file selection numbers.")
            return
        input_path_A = f"../../sample_inputs/{sample_inputs[idx1 - 1]}"
        input_path_B = f"../../sample_inputs/{sample_inputs[idx2 - 1]}"
    except ValueError:
        print("Invalid input; please enter valid numbers.")
        return

    print("Choose Matrix Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    choice = input("Enter choice (1/2/3): ").strip()

    try:
        print("Loading matrices...")
        matrixA = read_matrix_from_file(input_path_A)
        matrixB = read_matrix_from_file(input_path_B)
    except Exception as e:
        print(f"Error while reading input files: {e}")
        sys.exit(1)

    try:
        if choice == "1":
            result = add_matrices(matrixA, matrixB)
            output_file = "../../sample_outputs/sum_matrix.txt"
        elif choice == "2":
            result = subtract_matrices(matrixA, matrixB)
            output_file = "../../sample_outputs/diff_matrix.txt"
        elif choice == "3":
            result = multiply_matrices(matrixA, matrixB)
            output_file = "../../sample_outputs/prod_matrix.txt"
        else:
            print("Invalid choice.")
            return

        write_matrix_to_file(result, output_file)
        print(f"✅ Operation complete. Output saved to {output_file}")
    except Exception as e:
        print(f"Error during matrix operation: {e}")

if __name__ == "__main__":
    main()
