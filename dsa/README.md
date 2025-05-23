# Enterprise Web Development - Sparse Matrix Assignment

## Description

This project implements operations on sparse matrices with a focus on memory efficiency and runtime optimization.  
The following operations are supported:

- ✔ Matrix Addition  
- ✔ Matrix Subtraction  
- ✔ Matrix Multiplication

## Folder Structure

```
code/src/         → Main source code files  
sample_inputs/    → Provided sparse matrix input files  
sample_outputs/   → Generated output files for results  
tests/            → Unit tests for validation  
```

## How to Run

```sh
# Run the main program
python3 -m dsa.sparse_matrix.code.src.main
```

Then, select an operation (addition, subtraction, multiplication).

## Testing the Code

```sh
python3 -m unittest discover dsa/sparse_matrix/tests/
```

This runs all unit tests to verify correctness.

