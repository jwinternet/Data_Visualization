"""
Data Visualization Project - mpl_squares
"""
###############################################################################

__author__ = "Jared Winter"
__copyright__ = "Copyright 2020, jwinternet"
__credits__ = ""
__license__ = "GNU General Public License v3.0"
__version__ = "0.0.3"
__updated__ = "3/10/2020"
__email__ = "jaredwinter2015@outlook.com"
__status__ = "DEV"

###############################################################################

import matplotlib.pyplot as plt

###############################################################################

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=28)
ax.set_xlabel("Value", fontsize=18)
ax.set_ylabel("Square of Value", fontsize=18)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()