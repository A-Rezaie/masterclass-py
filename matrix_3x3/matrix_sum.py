"""
This script takes a 3x3 matrix from the user and calculates 
the sum of each row and each column.
Author: A.R
"""

def main():
    matrix = []
    
    for j in range(3):
        while True:
            line = input("Enter row(3 int num): ")
            parts = line.split()
            if len(parts) != 3:
                print("Error! Enter 3 int nums for each row.")
                continue
            row = []
            try:
                for item in parts:
                    mem = int(item)
                    row.append(mem)
            except ValueError:
                print("just enter int num")
                continue
            matrix.append(row)
            break
    
    print("Matrix is: ")
    for row in matrix:
        print(*row)
    
    row_number = 1
    for row in matrix:
        row_sum = 0
        for item in row:
            row_sum = row_sum + item
        print(f"row {row_number}: {row_sum}")
        row_number += 1
    
    col_number = 1
    col_sum = 0
    for col_index in range(3):
        for row in matrix:
            col_sum += row[col_index]
        print(f"column {col_number}: {col_sum}")
        col_number += 1
        col_sum = 0

if __name__ == "__main__":
    main()
