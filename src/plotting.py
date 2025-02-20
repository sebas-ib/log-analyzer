import matplotlib.pyplot as plt

"""@package docstring
Documentation for this module.

More details.
"""

def plot_against_time(data, column):
    """Documentation for a function.

    More details.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['ElapsedTime (Sec)'], data[column], label=column, color='r')
    plt.xlabel('Elapsed Time (Sec)')
    plt.ylabel('Value')
    plt.grid()
    plt.legend()
    plt.show()


def scatter_plot(data, x, y):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x], data[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid()
    plt.show()
