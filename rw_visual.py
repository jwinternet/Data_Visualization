"""
Data Visualization Project - Random Walk Visual Module
"""
###############################################################################

__author__ = "Jared Winter"
__copyright__ = "Copyright 2020, jwinternet"
__credits__ = ""
__license__ = "GNU General Public License v3.0"
__version__ = "0.0.2"
__updated__ = "3/10/2020"
__email__ = "jaredwinter2015@outlook.com"
__status__ = "DEV"

###############################################################################

import matplotlib.pyplot as plt
from random_walk import RandomWalk

###############################################################################

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk.
	rw = RandomWalk(50_000)
	rw.fill_walk()

	# Plot the points in the walk.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15, 9))
	point_numbers = range(rw.num_points)
	ax.scatter(
			rw.x_values,
			rw.y_values,
			c=point_numbers,
			cmap=plt.cm.Blues,
			edgecolors='none', s=15
			)

	# Emphasize the first and last points.
	ax.scatter(0, 0, c='green', edgecolors='none', s=100)
	ax.scatter(
			rw.x_values[-1],
			rw.y_values[-1],
			c='red',
			edgecolors='none',
			s=100
			)

	# Remove the axes.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break