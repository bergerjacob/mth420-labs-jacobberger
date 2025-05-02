# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name>
<Class>
<Date>
"""

import numpy as np


def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A = np.array([[3,-1, 4],
                  [1, 5, -9]])
    B = np.array([[2, 6,-5, 3],
                  [5,-8, 9, 7],
                  [9,-3,-2,-3]])
    return(A @ B)


def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A = np.array([[ 3, 1, 4],
                  [ 1, 5, 9],
                  [-5,3, 1]])
    return -1 * (A @ A @ A) + 9 * A @ A - 15 * A


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.triu(np.full((7,7),1))
    B = np.full((7,7),5) + np.tril(np.full((7,7),-6))
    print(A)
    print(B)
    return A @ B @ A


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    x = A.copy()
    mask = x < 0
    x[mask] = 0
    return x


def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array([[0, 2, 4], [1,3,5]])
    B = np.tril(np.full((3,3),3))
    C = np.diag([-2]*3)
    print('A', A)
    print('B', B)
    print('C', C)

    m, n = A.shape
    p, q = B.shape

    I = np.eye(n)

    Z_tl = np.zeros((n, q))
    Z_mc = np.zeros((m, m))
    Z_mr = np.zeros((m, n))
    Z_bc = np.zeros((p, m))

    block_matrix = np.block([
        [Z_tl, A.T, I],
        [A,    Z_mc, Z_mr],
        [B,    Z_bc, C]
    ])

    return block_matrix


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    A_float = np.asarray(A, dtype=float)

    row_sums = A_float.sum(axis=1, keepdims=True)

    safe_denominator = np.where(row_sums == 0, 1.0, row_sums)

    stochastic_matrix = A_float / safe_denominator

    return stochastic_matrix


# def prob7():
#     """ Given the array stored in grid.npy, return the greatest product of four
#     adjacent numbers in the same direction (up, down, left, right, or
#     diagonally) in the grid. Use slicing, as specified in the manual.
#     """
#     raise NotImplementedError("Problem 7 Incomplete")

if __name__ == "__main__":
    print(prob1())
    print("prob2:")
    print(prob2())
    print(prob3())
    print(prob4(np.array([-1,5,0,-10])))
    print(prob5())

    A_example = np.array([[1, 1, 0], [0, 1, 0], [1, 1, 1]])
    print("Problem 6 Example 1:\n", prob6(A_example))

    B_example = np.array([[1, 2, 3], [0, 0, 0], [2, 0, 2]])
    print("\nProblem 6 Example 2:\n", prob6(B_example))
