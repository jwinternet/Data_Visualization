"""
Data Visualization Project - Show Colors Scales Module
"""
###############################################################################

__author__ = "Jared Winter"
__copyright__ = "Copyright 2020, jwinternet"
__credits__ = ""
__license__ = "GNU General Public License v3.0"
__version__ = "0.0.1"
__updated__ = "3/15/2020"
__email__ = "jaredwinter2015@outlook.com"
__status__ = "DEV"

###############################################################################

import plotly

###############################################################################

for key in plotly.colors.PLOTLY_SCALES.keys():
	print(key)