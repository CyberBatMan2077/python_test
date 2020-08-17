import matplotlib.pyplot as plt
import pygal

from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

hist = pygal.XY(stroke=True)
hist.title = 'RandomWalk'
hist.add('DOTs', [(rw.x_values[i], rw.y_values[i]) for i in range(0, rw.num_points)])

hist.render_to_file('RandomWalk.svg')

