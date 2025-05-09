# drazin.py
"""Volume 1: The Drazin Inverse.
<Name>
<Class>
<Date>
"""

import numpy as np
from scipy import linalg as la


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    # Condition 1: A @ Ad == Ad @ A
    cond1 = np.allclose(A @ Ad, Ad @ A)

    # Condition 2: A**(k+1) @ Ad == A**k
    A_k = np.linalg.matrix_power(A, k)
    A_k_plus_1 = np.linalg.matrix_power(A, k + 1)
    cond2 = np.allclose(A_k_plus_1 @ Ad, A_k)

    # Condition 3: Ad @ A @ Ad == Ad
    cond3 = np.allclose(Ad @ A @ Ad, Ad)

    return cond1 and cond2 and cond3


# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    n = A.shape[0]

    f_nonzero = lambda x: abs(x) > tol
    T1, Q1, k1 = la.schur(A, sort=f_nonzero, output='complex')

    f_zero = lambda x: abs(x) <= tol
    T2, Q2, k2_unused = la.schur(A, sort=f_zero, output='complex')

    U_cols_M = Q1[:, :k1]
    U_cols_N = Q2[:, :(n - k1)]
    
    U = np.hstack((U_cols_M, U_cols_N))
    
    try:
        U_inv = np.linalg.inv(U)
    except np.linalg.LinAlgError:
        print("Warning: U matrix is singular or nearly singular.")
        U_inv = np.linalg.pinv(U)

    V = U_inv @ A @ U

    Z = np.zeros_like(A, dtype=complex if np.iscomplexobj(V) or np.iscomplexobj(A) else float)

    if k1 > 0:
        M_block = V[:k1, :k1]
        try:
            M_inv = np.linalg.inv(M_block)
            Z[:k1, :k1] = M_inv
        except np.linalg.LinAlgError:
            print(f"Warning: M_block (size {k1}x{k1}) is singular. Check tolerance.")

    Ad = U @ Z @ U_inv
    
    if not np.iscomplexobj(A) and np.iscomplexobj(Ad):
        if np.allclose(Ad.imag, 0, atol=tol):
            Ad = Ad.real
            
    return Ad


def laplacian(A):
    """Compute the Laplacian matrix of the adjacency matrix A,
    as well as the second smallest eigenvalue.

    Parameters:
        A ((n,n) ndarray) adjacency matrix for an undirected weighted graph.

    Returns:
        L ((n,n) ndarray): the Laplacian matrix of A
    """
    D = A.sum(axis=1) # The degree of each vertex (either axis).
    return np.diag(D) - A

# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    n = A.shape[0]
    if n == 0:
        return np.array([], dtype=float)
    
    L = laplacian(A)
    R = np.zeros((n, n), dtype=float)

    for j in range(n):
        Lj = L.copy()
        Lj[j, :] = 0.0 
        Lj[j, j] = 1.0
        
        LjD = drazin_inverse(Lj) 

        for i in range(n):
            if i == j:
                R[i, j] = 0.0
            else:
                if np.iscomplexobj(LjD[i,i]):
                    # .real probably not necessary but just in case we run into complex values
                    R[i, j] = LjD[i, i].real
                else:
                    R[i,j] = LjD[i,i]
    return R


# # Problems 4 and 5
# class LinkPredictor:
#     """Predict links between nodes of a network."""
#
#     def __init__(self, filename='social_network.csv'):
#         """Create the effective resistance matrix by constructing
#         an adjacency matrix.
#
#         Parameters:
#             filename (str): The name of a file containing graph data.
#         """
#         raise NotImplementedError("Problem 4 Incomplete")
#
#
#     def predict_link(self, node=None):
#         """Predict the next link, either for the whole graph or for a
#         particular node.
#
#         Parameters:
#             node (str): The name of a node in the network.
#
#         Returns:
#             node1, node2 (str): The names of the next nodes to be linked.
#                 Returned if node is None.
#             node1 (str): The name of the next node to be linked to 'node'.
#                 Returned if node is not None.
#
#         Raises:
#             ValueError: If node is not in the graph.
#         """
#         raise NotImplementedError("Problem 5 Incomplete"
#
#
#     def add_link(self, node1, node2):
#         """Add a link to the graph between node 1 and node 2 by updating the
#         adjacency matrix and the effective resistance matrix.
#
#         Parameters:
#             node1 (str): The name of a node in the network.
#             node2 (str): The name of a node in the network.
#
#         Raises:
#             ValueError: If either node1 or node2 is not in the graph.
#         """
#         raise NotImplementedError("Problem 5 Incomplete")

if __name__ == "__main__":
    print(is_drazin(np.array([[1, 3, 0, 0], [0, 1, 3, 0], [0, 0, 1, 3], [0, 0, 0, 0]]), np.array([[1, -3, 9, 81], [0, 1, -3, -18], [0, 0, 1, 3], [0, 0, 0, 0]]), 1))
    print(is_drazin(np.array([[1, 3, 0, 0], [0, 1, 3, 0], [0, 0, 1, 3], [0, 0, 0, 0]]), np.array([[1, -3, 9, 80], [0, 1, -3, -18], [0, 0, 1, 3], [0, 0, 0, 0]]), 1))
    A1 = np.array([[1, 3, 0, 0], [0, 1, 3, 0], [0, 0, 1, 3], [0, 0, 0, 0]], dtype=float)
    k_A1 = 1
    print(f"Test 1 (A1, k={k_A1}, expect True): {is_drazin(A1, drazin_inverse(A1, tol=1e-9), k_A1)}")
    print(drazin_inverse(A1, tol=1e-9))

    B1 = np.array([[1, 1, 3], [5, 2, 6], [-2, -1, -3]], dtype=float)
    k_B1 = 3
    print(f"Test 2 (B1, k={k_B1}, expect True): {is_drazin(B1, drazin_inverse(B1, tol=1e-4), k_B1)}")
    print(drazin_inverse(B1, tol=1e-4))

    print(f"Test 3 (A1, k=0, expect False): {is_drazin(A1, drazin_inverse(A1, tol=1e-9), 0)}")


    A_path_test = np.array([[0.,1.,0.],[1.,0.,1.],[0.,1.,0.]])
    R_computed_path = effective_resistance(A_path_test)
    print("Effective resistance for path graph 0-1-2:\n", R_computed_path)
