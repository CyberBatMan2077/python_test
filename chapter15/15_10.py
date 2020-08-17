import pygal
from die import Die
import matplotlib.pyplot as plt

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

x_values = [str(x) for x in range(1,7)]
y_values = frequencies
#plt.scatter(x_values,y_values)
plt.plot(x_values,y_values)
plt.show()
