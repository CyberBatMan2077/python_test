import pygal
from die import Die

die = Die()

die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []

for value in range(2,die.num_sides*2+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "2D6"
hist.x_labels = [str(x) for x in range(2,13)]
hist.x_title = 'Result'
hist.y_title = "Frequency"

hist.add('2D6',frequencies)
hist.render_to_file('dice_visual.svg')
