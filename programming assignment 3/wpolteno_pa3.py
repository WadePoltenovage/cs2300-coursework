# Wade Poltenovage Programming assignment 3
#11/21/2024
# The coding assignment is to write a program that reads in matrices from a file and then
#preforms the specified order of math operations on them for the Leontif input output model

import numpy

def read_matrices_from_file(filename):
    # Read in matrices from the file
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Extracting D (first 3 lines, each split into a list of floats)
        D = numpy.array([list(map(float, line.split())) for line in lines[:3]])
        # Extracting E (last line, split into a list of floats)
        E = numpy.array([float(line.strip()) for line in lines[3:]]).reshape(-1, 1)
    return D, E

def main():

    # Input file containing the matrices D and E
    print("Please input the name of the file you would like to read:")
    filename = input()

    # Read matrices D and E from the input file
    D, E = read_matrices_from_file(filename)

    # Create Identity matrix I
    I = numpy.identity(3)

    # Compute I - D
    I_minus_D = I - D

    # Compute the inverse of (I - D)
    try:
        I_minus_D_inv = numpy.linalg.inv(I_minus_D)
    except numpy.linalg.LinAlgError:
        raise ValueError("Matrix (I - D) is not invertible.")

    # Compute the output matrix X
    X = numpy.dot(I_minus_D_inv, E)

    # Round each element of X to the nearest tenth
    X = numpy.round(X, decimals = 1)

    # Step 3: Display the output matrix X
    print("Output matrix X:")
    print(X)

if __name__ == "__main__":
    main()
