"""
Data Visualization Project - Main Module
"""
###############################################################################

__author__ = "Jared Winter"
__copyright__ = "Copyright 2020, jwinternet"
__credits__ = ""
__license__ = "GNU General Public License v3.0"
__version__ = "0.0.1"
__updated__ = "3/10/2020"
__email__ = "jaredwinter2015@outlook.com"
__status__ = "DEV"

###############################################################################

import matplotlib.pyplot as plt

###############################################################################

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)
plt.show()