# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name>
<Class>
<Date>
"""

import numpy as np
from cmath import sqrt
from scipy import linalg as la
from matplotlib import pyplot as plt
import os


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Qb, Rb = la.qr(A, mode="economic")
    rhs = Qb.T @ b
    x = la.solve_triangular(Rb, rhs)
    return x

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "housing.npy")
        housing_data = np.load(file_path)
    except FileNotFoundError:
        print("Error: 'housing.npy' not found.")
        return

    years = housing_data[:, 0]
    indices = housing_data[:, 1]

    # Construct the matrix A (col of 1s, col of years) and vector b (indices).
    A = np.column_stack((np.ones_like(years), years))
    b = indices

    # Solve for the coefficients [intercept, slope]
    solution = least_squares(A, b)
    intercept_c = solution[0]
    slope_m = solution[1]

    # Plot the original data and the least squares line.
    plt.scatter(years, indices, s=15, label='Data Points')
    x_line = np.linspace(np.min(years), np.max(years), 100)
    y_line = slope_m * x_line + intercept_c
    plt.plot(x_line, y_line, color='red', label=f'Fit: y={slope_m:.2f}x+{intercept_c:.2f}')

    plt.xlabel("Year (since 2000)")
    plt.ylabel("Housing Price Index")
    plt.title("Housing Price Index Linear Fit")
    plt.legend()
    plt.grid(True, alpha=0.5)
    plt.show()


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "housing.npy")
        housing_data = np.load(file_path)
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        return

    years = housing_data[:, 0]    # Independent variable (x)
    indices = housing_data[:, 1]  # Dependent variable (y)

    degrees_to_fit = [3, 6, 9, 12]
    num_plots = len(degrees_to_fit)

    # Create a 2x2 grid of subplots.
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.ravel() # Flatten the 2x2 array

    x_smooth = np.linspace(np.min(years), np.max(years), 400)

    for i, degree in enumerate(degrees_to_fit):
        A = np.vander(years, degree + 1)
        b = indices # Vector to approximate

        coefficients = la.lstsq(A, b)[0]

        polynomial = np.poly1d(coefficients)

        y_poly_smooth = polynomial(x_smooth)

        # Plot on the i-th subplot.
        ax = axes[i]
        ax.scatter(years, indices, s=10, alpha=0.6, label="Data Points") # Original data
        ax.plot(x_smooth, y_poly_smooth, color='red', label=f"Degree {degree} Fit") # Polynomial fit
        ax.set_title(f"Polynomial Fit (Degree {degree})")
        ax.set_xlabel("Year (since 2000)")
        ax.set_ylabel("Housing Price Index")
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.5)

    plt.suptitle("Housing Price Index: Polynomial Fits", fontsize=16, y=0.99)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


# def plot_ellipse(a, b, c, d, e):
#     """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
#     theta = np.linspace(0, 2*np.pi, 200)
#     cos_t, sin_t = np.cos(theta), np.sin(theta)
#     A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
#     B = b*cos_t + d*sin_t
#     r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)
#
#     plt.plot(r*cos_t, r*sin_t)
#     plt.gca().set_aspect("equal", "datalim")
#
# # Problem 4
# def ellipse_fit():
#     """Calculate the parameters for the ellipse that best fits the data in
#     ellipse.npy. Plot the original data points and the ellipse together, using
#     plot_ellipse() to plot the ellipse.
#     """
#     raise NotImplementedError("Problem 4 Incomplete")
#
#
# # Problem 5
# def power_method(A, N=20, tol=1e-12):
#     """Compute the dominant eigenvalue of A and a corresponding eigenvector
#     via the power method.
#
#     Parameters:
#         A ((n,n) ndarray): A square matrix.
#         N (int): The maximum number of iterations.
#         tol (float): The stopping tolerance.
#
#     Returns:
#         (float): The dominant eigenvalue of A.
#         ((n,) ndarray): An eigenvector corresponding to the dominant
#             eigenvalue of A.
#     """
#     raise NotImplementedError("Problem 5 Incomplete")
#
#
# # Problem 6
# def qr_algorithm(A, N=50, tol=1e-12):
#     """Compute the eigenvalues of A via the QR algorithm.
#
#     Parameters:
#         A ((n,n) ndarray): A square matrix.
#         N (int): The number of iterations to run the QR algorithm.
#         tol (float): The threshold value for determining if a diagonal S_i
#             block is 1x1 or 2x2.
#
#     Returns:
#         ((n,) ndarray): The eigenvalues of A.
#     """
#     raise NotImplementedError("Problem 6 Incomplete")

if __name__ == "__main__":
    A = np.array([
        [1., 2., 0.],
        [0., 1., 1.],
        [1., 0., 1.],
        [1., 1., 1.]
        ])
    b = np.array([3., 2., 2., 3.])
    print(least_squares(A, b))
    line_fit()
    polynomial_fit()
