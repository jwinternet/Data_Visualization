"""
Data Visualization Project - Die Visual Module
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

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

###############################################################################

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(
		title='Results of rolling a D6 and a D10 50000 times',
		xaxis=x_axis_config,
		yaxis=y_axis_config
		)
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d10.html')