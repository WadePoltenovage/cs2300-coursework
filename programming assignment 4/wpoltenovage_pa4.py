# Homework 7, Exercise 2
# Name Wade Poltenovage
# Date 12/14/2024
# Description of your program:
# This program calculates the least squares regression of a given set of points
# and the plots them out on a graph. The program additionally, outputs the linear equation
# of the given line. For this problem in particular the program is to find the "demand for a
# rechargeable power drill as a function of price." and is labeled as such.
# Thank you for the class

import numpy
# Make sure you have this installed, I had some trouble getting this working personally
import matplotlib.pyplot


# Reads in data file formated as x y on each line
def read_data(filename):
    with open(filename, 'r') as f:
        data = [tuple(map(float, line.split())) for line in f]
    return data


def least_squares_regression(data):
    x_vals = numpy.array([pair[0] for pair in data])
    y_vals = numpy.array([pair[1] for pair in data])

    # Calculate the least squares regression line: y = mx + b
    a = numpy.vstack([x_vals, numpy.ones(len(x_vals))]).T
    m, b = numpy.linalg.lstsq(a, y_vals, rcond=None)[0]

    return m, b


def plot_regression_line(data, m, b):
    x_vals = numpy.array([pair[0] for pair in data])
    y_vals = numpy.array([pair[1] for pair in data])

    # Plot the data points
    matplotlib.pyplot.scatter(x_vals, y_vals, color='blue', label='Data Points')

    # Plot the regression line
    x_line = numpy.linspace(min(x_vals), max(x_vals), 100)
    y_line = m * x_line + b
    matplotlib.pyplot.plot(x_line, y_line, color='red', label=f'Line: y = {m:.1f}x + {b:.1f}')

    # Add labels and title
    matplotlib.pyplot.xlabel('Price (in dollars)')
    matplotlib.pyplot.ylabel('Monthly Sales')
    matplotlib.pyplot.title('Least Squares Regression Line')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.show()


def main():
    print("Please input the name of the file you would like to read:")
    filename = input()
    data = read_data(filename)
    m, b = least_squares_regression(data)
    print(f'Linear Equation: y = {m:.1f}x + {b:.1f}')
    plot_regression_line(data, m, b)


if __name__ == '__main__':
    main()
