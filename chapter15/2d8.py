import pygal
from die import Die

die = Die()

die_1 = Die(8)
die_2 = Die(8)
results = []
for roll_num in range(1000000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
frequencies = []

for value in range(2,die_1.num_sides*2+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "2D8"
hist.x_labels = [str(x) for x in range(2,17)]
hist.x_title = 'Result'
hist.y_title = "Frequency"

hist.add('2D8',frequencies)
hist.render_to_file('2d8_visual.svg')
