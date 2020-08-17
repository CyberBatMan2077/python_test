import pygal
from die import Die

die = Die()

die_1 = Die()
die_2 = Die()
die_3 = Die()
results = []
for roll_num in range(100000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)
frequencies = []

for value in range(3,die_1.num_sides*3+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "3D6"
hist.x_labels = [str(x) for x in range(3,19)]
hist.x_title = 'Result'
hist.y_title = "Frequency"

hist.add('3D6',frequencies)
hist.render_to_file('3d6_visual.svg')
