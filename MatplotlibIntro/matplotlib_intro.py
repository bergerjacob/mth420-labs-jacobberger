# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name>
<Class>
<Date>
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    # Create the n x n array from standard normal distribution
    random_array = np.random.normal(size=(n, n))

    # Compute the mean of each row (axis=1)
    row_means = np.mean(random_array, axis=1)

    # Compute and return the variance of these means
    variance_of_means = np.var(row_means)
    return variance_of_means

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    # Define the sequence of n values
    n_values = np.arange(100, 1001, 100)

    # Calculate the variance for each n
    variances = np.array([var_of_means(n) for n in n_values])

    plt.plot(n_values, variances, marker='.')
    plt.xlabel("n")
    plt.ylabel("Variance of Row Means")
    plt.title("Variance of Row Means vs. Matrix Size (n x n)")
    plt.grid(True)

    plt.show()


# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    # Define domain
    x_values = np.linspace(-2 * np.pi, 2 * np.pi, 500)

    # Calculate values
    y_sin = np.sin(x_values)
    y_cos = np.cos(x_values)
    y_arctan = np.arctan(x_values)

    # Plot functions
    plt.plot(x_values, y_sin, label='sin(x)')
    plt.plot(x_values, y_cos, label='cos(x)')
    plt.plot(x_values, y_arctan, label='arctan(x)')

    # Add details
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Plot of sin(x), cos(x), and arctan(x)")
    plt.grid(True)
    plt.legend()

    plt.show()


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    points_per_side = 200 # Resolution for plotting

    # Domain [-2, 1)
    x_left = np.linspace(-2, 1, points_per_side, endpoint=False)
    y_left = 1 / (x_left - 1)

    # Domain (1, 6] - Ensure x=1 is not included
    # Create points from 1 to 6, then slice off the first point (x=1)
    x_right = np.linspace(1, 6, points_per_side + 1)[1:]
    y_right = 1 / (x_right - 1)

    # Plot left side
    plt.plot(x_left, y_left, color='magenta', linestyle='--', linewidth=4)
    # Plot right side
    plt.plot(x_right, y_right, color='magenta', linestyle='--', linewidth=4)

    # Set axis limits
    plt.xlim(-2, 6)
    plt.ylim(-6, 6)

    plt.show()


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    # Define domain
    x = np.linspace(0, 2 * np.pi, 400)

    # Calculate function values
    y1 = np.sin(x)
    y2 = np.sin(2 * x)
    y3 = 2 * np.sin(x)
    y4 = 2 * np.sin(2 * x)

    # Create 2x2 subplot grid
    fig, axs = plt.subplots(2, 2, figsize=(8, 8)) # Adjust figsize if needed
    fig.suptitle('Comparison of Sine Functions') # Overall figure title

    # Plot sin(x): Top-Left (axs[0, 0])
    axs[0, 0].plot(x, y1, color='green', linestyle='-')
    axs[0, 0].set_title('sin(x)')
    axs[0, 0].axis([0, 2 * np.pi, -2, 2]) # xmin, xmax, ymin, ymax

    # Plot sin(2x): Top-Right (axs[0, 1])
    axs[0, 1].plot(x, y2, color='red', linestyle='--')
    axs[0, 1].set_title('sin(2x)')
    axs[0, 1].axis([0, 2 * np.pi, -2, 2])

    # Plot 2sin(x): Bottom-Left (axs[1, 0])
    axs[1, 0].plot(x, y3, color='blue', linestyle='--')
    axs[1, 0].set_title('2sin(x)')
    axs[1, 0].axis([0, 2 * np.pi, -2, 2])

    # Plot 2sin(2x): Bottom-Right (axs[1, 1])
    axs[1, 1].plot(x, y4, color='magenta', linestyle=':') # Dotted linestyle
    axs[1, 1].set_title('2sin(2x)')
    axs[1, 1].axis([0, 2 * np.pi, -2, 2])

    # Adjust layout to prevent overlapping titles/labels
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Leave space for suptitle

    plt.show()


# # Problem 5
# def prob5():
#     """ Visualize the data in FARS.npy. Use np.load() to load the data, then
#     create a single figure with two subplots:
#         1. A scatter plot of longitudes against latitudes. Because of the
#             large number of data points, use black pixel markers (use "k,"
#             as the third argument to plt.plot()). Label both axes.
#         2. A histogram of the hours of the day, with one bin per hour.
#             Label and set the limits of the x-axis.
#     """
#     raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    # Define domain and grid
    resolution = 200 # Points along each axis
    x = np.linspace(-2 * np.pi, 2 * np.pi, resolution)
    y = np.linspace(-2 * np.pi, 2 * np.pi, resolution)
    X, Y = np.meshgrid(x, y)

    # Calculate Z = g(x, y), handling the limit at x=0 or y=0
    with np.errstate(divide='ignore', invalid='ignore'): # Avoid warnings
        # Calculate sin(t)/t for x and y separately
        term_x = np.ones_like(X) # Initialize with limit value 1
        term_y = np.ones_like(Y)
        non_zero_x = (X != 0)
        non_zero_y = (Y != 0)
        term_x[non_zero_x] = np.sin(X[non_zero_x]) / X[non_zero_x]
        term_y[non_zero_y] = np.sin(Y[non_zero_y]) / Y[non_zero_y]
        Z = term_x * term_y

    # Create figure and subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 5)) # 1 row, 2 columns
    cmap_name = 'viridis' # Non-default colormap
    num_contour_levels = 15 # Number of levels for contour plot

    # Subplot 1: Heat Map (using pcolormesh)
    heatmap = axs[0].pcolormesh(X, Y, Z, cmap=cmap_name, shading='gouraud')
    fig.colorbar(heatmap, ax=axs[0]) # Add colorbar
    axs[0].set_title('Heat Map g(x,y)')
    axs[0].axis('equal') # Ensure aspect ratio is equal
    axs[0].axis([-2 * np.pi, 2 * np.pi, -2 * np.pi, 2 * np.pi]) # Set limits

    # Subplot 2: Contour Map
    contour = axs[1].contour(X, Y, Z, levels=num_contour_levels, cmap=cmap_name)
    fig.colorbar(contour, ax=axs[1]) # Add colorbar
    axs[1].set_title('Contour Map g(x,y)')
    axs[1].axis('equal') # Ensure aspect ratio is equal
    axs[1].axis([-2 * np.pi, 2 * np.pi, -2 * np.pi, 2 * np.pi]) # Set limits

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    prob1()
    prob2()
    prob3()
    prob4()
    prob6()
