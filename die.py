"""
Data Visualization Project - Die Module
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

from random import randint

###############################################################################

class Die:
	"""A class representing a single die."""

	def __init__(self, num_sides=6):
		"""Assume a six-sided die."""
		self.num_sides = num_sides

	def roll(self):
		""""Return a random value between 1 and number of sides."""
		return randint(1, self.num_sides)