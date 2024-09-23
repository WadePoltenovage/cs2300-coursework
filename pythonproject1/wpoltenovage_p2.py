#Wade Poltenovage
#Write a program named “name_p2” (based on the same naming scheme from the prior
#part), which will take the filenames for 2 distinct input matrices, say A and B (where A and B are
#different matrices), and an output filename. The program will read in the matrices from those
#two files and then compute and write A+B to the output file (i.e., the element-wise sum of the
#two matrices/arrays.) Have the program prompt the user for input file according to the matrix
#names in Part 1 above.

# Function to read a matrix from a file
def read_matrix_from_file(filename):
    with open(filename, "r") as f:
        return [list(map(int, line.split())) for line in f.readlines()]

# Function to write a matrix to a file
def write_matrix_to_file(matrix, filename):
    with open(filename, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

# Function to perform element-wise sum of two matrices
def add_matrices(mata, matb):
    rows = len(mata)
    cols = len(mata[0])
    return [[mata[r][c] + matb[r][c] for c in range(cols)] for r in range(rows)]

# Function to check if two matrices have the same dimensions
def matrices_have_same_dimensions(mata, matb):
    return len(mata) == len(matb) and len(mata[0]) == len(matb[0])

# Main program logic
def main():
    # Prompt the user for matrix names
    mata_name = input("Enter the name of the first matrix file: ").strip().lower()
    matb_name = input("Enter the name of the second matrix: ").strip().lower()

    # Construct filenames based on the format "wpoltenovage_matX.txt"
    mata_filename = str(mata_name)
    matb_filename = str(matb_name)

    # Check if files exist
    if not FileNotFoundError:
        print("Error: File " + str(mata_filename) + " does not exist.")
        return
    if not FileNotFoundError:
        print(f"Error: File " + str(matb_filename) + " does not exist.")
        return

    # Read matrices from the files
    mata = read_matrix_from_file(mata_filename)
    matb = read_matrix_from_file(matb_filename)

    # Check if matrices have the same dimensions
    if not matrices_have_same_dimensions(mata, matb):
        print("Error: The matrices have different dimensions and cannot be added.")
        return

    # Compute the element-wise sum of the matrices
    result_matrix = add_matrices(mata, matb)

    #Name file output, only compatible files are 1 and 2
    output_filename = "wpoltenovage_p2_out12.txt"

    # Write the result matrix to the output file
    write_matrix_to_file(result_matrix, output_filename)

    print("Matrix addition complete. The result has been saved to " + str(output_filename))

if __name__ == "__main__":
    main()
