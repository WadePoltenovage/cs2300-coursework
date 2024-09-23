#Wade Poltenovage
#Part 3) Write a program named “name_p4” (based on the same naming scheme from the prior
#part), and using the NumPy library in Python, calculate the same A+B as you did in Part 2.
#Your output results should be identical to those found in Part 2. Produce files of the format
#“name_p3_outA12.txt”, ... etc, where the two digits specify which of the inputs were used to
#produce that output. You only need to create output files for those matrices that can be added.

import numpy

# Function to read a matrix from a file using NumPy
def read_matrix_from_file(filename):
    return numpy.loadtxt(filename, dtype=int)

# Function to write a matrix to a file using NumPy
def write_matrix_to_file(matrix, filename):
    numpy.savetxt(filename, matrix, fmt='%d')

# Function to check if two matrices have the same dimensions using NumPy
def matrices_have_same_dimensions(mata, matb):
    return mata.shape == matb.shape

# Main program logic
def main():
    # Prompt the user for matrix names
    mata_name = input("Enter the name of the first matrix file: ").strip().lower()
    matb_name = input("Enter the name of the second matrix file: ").strip().lower()

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

    #Read matrices from the files
    mata = read_matrix_from_file(mata_filename)
    matb = read_matrix_from_file(matb_filename)

    # Check if matrices have the same dimensions
    if not matrices_have_same_dimensions(mata, matb):
        print("Error: The matrices have different dimensions and cannot be added.")
        return

    # Compute the element-wise sum of the matrices using NumPy
    result_matrix = numpy.add(mata, matb)

    # Output file
    output_filename = "wpoltenovage_p3_out12.txt"

    # Write the result matrix to the output file
    write_matrix_to_file(result_matrix, output_filename)

    print("Matrix addition complete. The result has been saved to " + output_filename)

if __name__ == "__main__":
    main()