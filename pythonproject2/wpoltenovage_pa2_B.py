# Wade Poltenovage Programming assignment 2 part 1
# 10/30/2024
# Write a program that can solve a system of linear equations given a initial matrix
# The first part of this program is to solve the system without substituting in values to any given variables
# The 2nd part is to solve the system with user inputed variables and display what the result of the give solutions is


import numpy
from sympy import Matrix, Eq, linsolve, symbols

def main():

    #prints the output for B2.1 will also include this in a text file for grading later
    print("B2.1")
    print("x1 + x3 = 600")
    print("x1 - x2 - x4 = 0")
    print("x2 + x5 = 500")
    print("x3 + x6 = 600")
    print("x4 - x5 + x6 - x7 = 0")
    print("x7 = 500")

    print("B2.2")

    # Define the augmented matrix for the system of equations
    augmented_matrix = numpy.array([
        [1, 0, 1, 0, 0, 0, 0, 600],
        [1, -1, 0, -1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 500],
        [0, 0, 1, 0, 0, 1, 0, 600],
        [0, 0, 0, 1, 0, -1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 500],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ])

    # Convert the numpy array to a sympy Matrix
    matrix = Matrix(augmented_matrix)

    # Get the RREF of the matrix
    rref_matrix, _ = matrix.rref()

    #prints the RREF matrix as a deliverable
    print(numpy.array(rref_matrix))

    # Initialize the variables
    x = symbols('x1, x2, x3, x4, x5, x6, x7')

    # Define the equations based on the RREF matrix
    equations = [
        Eq(x[0], x[5]),
        Eq(x[1], x[6]),
        Eq(x[2] + x[5], 600),
        Eq(x[3] - x[5] + x[6], 0),
        Eq(x[4] + x[6], 500),
        Eq(x[6], 500 - x[4]),
    ]

    # Solve the equations using the variables
    solutions = linsolve(equations, x[0], x[1], x[2], x[3], x[4], x[5], x[6])
    # An object to help iterate through the solutions for printing
    solutions_tuple = next(iter(solutions))


    # Prints the output of the sequence of the linear equations,
    # combines the variables from the side of the linear equation,
    # and the solution that is outputted by my solutions above.
    print("Solutions to linear equations:")
    print(str(x[0]) + " = " + str(solutions_tuple[0]))
    print(str(x[1]) + " = " + str(solutions_tuple[1]))
    print(str(x[2]) + " = " + str(solutions_tuple[2]))
    print(str(x[3]) + " = " + str(solutions_tuple[3]))
    print(str(x[4]) + " = " + str(solutions_tuple[4]))
    print(str(x[5]) + " = " + str(solutions_tuple[5]))
    print(str(x[6]) + " = " + str(solutions_tuple[6]))

    print("\nPart B2.3")

    # Intialize the variables
    variables = [x[0], x[1], x[2], x[3], x[4], x[5], x[6]]

    # Prompt user to input values for each variable, or leave blank to keep it symbolic
    for i in range(len(variables)):
        value = input(f"Enter a value for x{i+1} (or press Enter to keep symbolic): ")
        if value:
            try:
                variables[i] = int(value)

            except ValueError:
                print(f"Invalid input for x{i+1}. Skipping.")

    # Define the equations based on the RREF matrix
    equations = [
        Eq(variables[0], variables[5]),
        Eq(variables[1], variables[6]),
        Eq(variables[2] + variables[5], 600),
        Eq(variables[3] - variables[5] + variables[6], 0),
        Eq(variables[4] + variables[6], 500),
        Eq(variables[6], 500 - variables[4]),
    ]

    # Solve the equations
    solutions = linsolve(equations, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6])
    # An object in order to iterate through the solutions for printing
    solutions_tuple = next(iter(solutions))


    # Prints the output of the sequence of the linear equations,
    # combines the variables from the side of the linear equation,
    # and the solution that is outputted by my solutions above.
    print("Solution to sequence of linear equations")
    print(str(variables[0]) + " = " + str(solutions_tuple[0]))
    print(str(variables[1]) + " = " + str(solutions_tuple[1]))
    print(str(variables[2]) + " = " + str(solutions_tuple[2]))
    print(str(variables[3]) + " = " + str(solutions_tuple[3]))
    print(str(variables[4]) + " = " + str(solutions_tuple[4]))
    print(str(variables[5]) + " = " + str(solutions_tuple[5]))
    print(str(variables[6]) + " = " + str(solutions_tuple[6]))

if __name__ == "__main__":
    main()