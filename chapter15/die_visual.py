import pygal
from die import Die

die = Die()

results = []
#for roll_num in range(1000):
#	result = die.roll()
#	results.append(result)
results = [die.roll() for roll_num in range(1000)]

frequencies = []

#for value in range(1,die.num_sides+1):
#	frequency = results.count(value)
#	frequencies.append(frequency)

frequencies = [results.count(value) for value in range(1,die.num_sides+1)]
hist = pygal.Bar()

hist.title = "D6"
# homework 15-6
hist.x_labels = [str(x) for x in range(1,7)]
hist.x_title = 'Result'
hist.y_title = "Frequency"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
