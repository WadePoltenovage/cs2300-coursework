# Wade Poltenovage Programming assignment 2 part 1
#10/30/2024
# Write a program that can encrypt and decrypt files that it reads and output the original messages
# The first version that reads/encrypts and then decrypts/prints is to demonstrate understanding
# The 2nd part is to decode an already encrypted file to make sure it can read correctly
import numpy
import re

# Convert hex to decimal
def hex_to_decimal(hex_value):
    return int(hex_value, 16)

# Convert a message into hex code and the convert to decimals
def message_to_unicode_decimals(message):
    decimal_values = []
    for char in message:
        unicode_hex = format(ord(char), "04X")
        decimal_value = hex_to_decimal(unicode_hex)
        decimal_values.append(decimal_value)
    return decimal_values

# Convert a linear sequence into a message
def unicode_decimal_to_message(decimal_values):
    message = ''.join(
        chr(value) if 32 <= value <= 126 else ''  # Remove out-of-bounds characters
        for value in decimal_values
    )
    return message

def part_a21():

    print("Part A2.1")

    # Input file name for testing
    print("Please input the name of the file you would like to read:")
    filename = input()
    try:
        with open(filename, 'r') as file:
            message = file.read()
            print(message)
    except FileNotFoundError:
        print("The file '" + str(filename) + "' does not exist.")
    except IOError:
        print("An error occurred while reading the file '" + str(filename) + " '.")

    # Convert the message to its unicode decimal values
    unicode_decimals = message_to_unicode_decimals(message)

    # Define matrix a (the encoding matrix)
    a = numpy.matrix([
        [1, -1, -1, 1],
        [2, -3, -5, 4],
        [-2, -1, -2, 2],
        [3, -3, -1, 2]
    ])

    # Reshape the message values to fit into matrix b
    rows = a.shape[0]
    cols = int(numpy.ceil(len(unicode_decimals) / rows))
    b = numpy.zeros((rows, cols), dtype=int)

    # Fill matrix b column by column
    for i, value in enumerate(unicode_decimals):
        col = i // rows
        row = i % rows
        b[row, col] = value

    # Invert matrix a
    inverse_a = numpy.linalg.inv(a)

    # Multiply matrix a by matrix b to get the encrypted message
    cipher_matrix_c = numpy.dot(a, b)

    # Decode the message by multiplying the inverse of a with the cipher matrix
    decoded_matrix = numpy.dot(inverse_a, cipher_matrix_c)

    # Round the decoded matrix to remove any floating-points
    decoded_matrix = numpy.round(decoded_matrix).astype(int)

    # Read the decoded values column by column to reconstruct the sequence correctly
    decoded_sequence = []
    for col in range(decoded_matrix.shape[1]):
        for row in range(decoded_matrix.shape[0]):
            decoded_sequence.append(decoded_matrix[row, col])

    # Convert the numeric sequence back into characters
    decoded_message = unicode_decimal_to_message(decoded_sequence)

    # Print the decoded message
    print("The decoded message is:")
    print(decoded_message)

def part_a22():

    print("\nPart A.22")

    # Input message for testing
    print("Please input the name of the file you want to read:")
    filename = input()
    with open(filename, 'r') as file:
        # Read the content of the file
        message = file.read()
        # Use regex to find all integers (including negative numbers)
        numbers = [int(num) for num in re.findall(r'-?\d+', message)]

    # Define matrix a (the encoding matrix)
    a = numpy.matrix([
        [1, -1, -1, 1],
        [2, -3, -5, 4],
        [-2, -1, -2, 2],
        [3, -3, -1, 2]
    ])

    # Define the number of rows and columns for matrix d based on matrix a
    rows = a.shape[0]
    cols = int(numpy.ceil(len(numbers) / rows))

    # Initialize matrix d with zeros
    d = numpy.zeros((rows, cols), dtype=int)

    # Fill matrix d column by column
    for i, value in enumerate(numbers):
        col = i // rows
        row = i % rows
        d[row, col] = value

    cipher_matrix_e = d

    # Invert Matrix a
    inverse_a = numpy.linalg.inv(a)

    # Decode the message by multiplying the inverse of a with the cipher matrix
    decoded_matrix = numpy.dot(inverse_a, cipher_matrix_e)

    # Round the decoded matrix to remove any floating-points
    decoded_matrix = numpy.round(decoded_matrix).astype(int)

    # Read the decoded values column by column
    decoded_sequence = []
    for col in range(decoded_matrix.shape[1]):
        for row in range(decoded_matrix.shape[0]):
            decoded_sequence.append(decoded_matrix[row, col])

    # Convert the linear sequence into a message
    decoded_message = unicode_decimal_to_message(decoded_sequence)

    # Print the results
    print("The decoded message is:")
    print(decoded_message)

def main():

    part_a21()

    part_a22()

if __name__ == "__main__":
    main()