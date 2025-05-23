"""Unit testing file for CVXPY Intro lab"""


import cvxpy_intro
import numpy as np

def test_prob5():
    """
    Write at least one unit test for problem 5.
    """
    A_test = np.array([[1, 2, 1, 1],
                       [0, 3, -2, -1]])
    b_test = np.array([7, 4])
    
    expected_x_optimizer = np.array([0., 1., 0., 0.])
    expected_objective_val = 5.099 

    actual_x_optimizer, actual_objective_val = cvxpy_intro.prob5(A_test, b_test)
    
    # Check if the computed optimizer is close to the expected one
    assert np.linalg.norm(actual_x_optimizer - expected_x_optimizer) <= 1e-3, \
        f"Problem 5 minimizer is incorrect. Expected {expected_x_optimizer}, but got {actual_x_optimizer}."
    
    # Check if the computed objective value is close to the expected one
    assert abs(actual_objective_val - expected_objective_val) <= 1e-3, \
        f"Problem 5 optimal value is incorrect. Expected {expected_objective_val:.3f}, but got {actual_objective_val:.3f}."
    print("All tests passed for prob5!")


def test_l1Min():
    # Sets up the matrix and vector
    A = np.array([[1, 2, 1, 1],
                 [0, 3, -2, -1]])
    b = np.array([7, 4])

    # Runs the l1Min function on the matrix and vector
    x, ans = cvxpy_intro.l1Min(A, b)
    
    # Checks for the correct vector and minimum value
    assert np.linalg.norm(x - np.array([0.0, 2.571, 1.857, 0.0])) <= 1e-3, "Returned the wrong minimizer"
    assert abs(ans - 4.429) <= 1e-3, "Returned the wrong mimimum"


test_prob5()
