import pygal
from die import Die

die = Die()

die_1 = Die()
die_2 = Die(10)
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []

for value in range(2,die_1.num_sides+die_2.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "D6+D10"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14',
				 '15','16']
hist.x_title = 'Result'
hist.y_title = "Frequency"

hist.add('D6+D10',frequencies)
hist.render_to_file('different_dice.svg')
