# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Name>
<Class>
<Date>
"""

import numpy as np
import cvxpy as cp

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x_vars = cp.Variable(3, nonneg=True)
    
    c = np.array([2, 1, 3])
    objective = cp.Minimize(c.T @ x_vars)

    constraints = [
        x_vars[0] + 2*x_vars[1] <= 3,
        x_vars[1] - 4*x_vars[2] <= 1,
        2*x_vars[0] + 10*x_vars[1] + 3*x_vars[2] >= 12
    ]

    problem = cp.Problem(objective, constraints)
    optimal_value = problem.solve()

    return x_vars.value, optimal_value


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n)
    objective = cp.Minimize(cp.norm(x, 1))
    constraints = [A @ x == b]
    problem = cp.Problem(objective, constraints)
    optimal_value = problem.solve()
    return x.value, optimal_value


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    p = cp.Variable(6, nonneg=True)
    
    costs = np.array([4, 7, 6, 8, 8, 9])
    
    objective = cp.Minimize(costs.T @ p)
    
    constraints = [
        # Supply constraints
        p[0] + p[1] <= 7,  # Supply from Center 1
        p[2] + p[3] <= 2,  # Supply from Center 2
        p[4] + p[5] <= 4,  # Supply from Center 3
        # Demand constraints
        p[0] + p[2] + p[4] == 5,  # Demand at Center 4
        p[1] + p[3] + p[5] == 8   # Demand at Center 5
    ]
    
    problem = cp.Problem(objective, constraints)
    optimal_value = problem.solve()
    
    return p.value, optimal_value


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    Q_matrix = np.array([[3., 2., 1.],
                         [2., 4., 2.],
                         [1., 2., 3.]])
    r_vector = np.array([3., 0., 1.])
    
    x_var = cp.Variable(3)
    
    objective = cp.Minimize(0.5 * cp.quad_form(x_var, Q_matrix) + r_vector.T @ x_var)
    problem = cp.Problem(objective)
    
    optimal_value = problem.solve()
    
    return x_var.value, optimal_value


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n)
    
    objective = cp.Minimize(cp.norm(A @ x - b, 2))
    
    constraints = [
        cp.sum(x) == 1,
        x >= 0
    ]
    
    problem = cp.Problem(objective, constraints)
    optimal_value = problem.solve()
    
    return x.value, optimal_value


# # Problem 6
# def prob6():
#     """Solve the college student food problem. Read the data in the file 
#     food.npy to create a convex optimization problem. The first column is 
#     the price, second is the number of servings, and the rest contain
#     nutritional information. Use cvxpy to find the minimizer and primal 
#     objective.
#
#     Returns (in order):
#         The optimizer x (ndarray)
#         The optimal value (float)
#     """	 
#     raise NotImplementedError("Problem 6 Incomplete")


if __name__ == "__main__":
    # print(prob1())
    # print(l1Min(np.array([[1, 2, 1, 1], [0, 3, -2, -1]]), np.array([7, 4])))
    # print(prob3())
    # print(prob4())
    pass
