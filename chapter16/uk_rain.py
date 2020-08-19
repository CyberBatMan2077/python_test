import csv
import pygal
from datetime import datetime

filename = 'uk_rain_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	rainfalls,dates =[],[]

	for row in reader:
		try:
			current_date = int(row[0])
			rainfall = int(row[1])
		except ValueError:
			print('Error')
		else:
			dates.append(current_date)
			rainfalls.append(rainfall)



	hist = pygal.Bar()

	hist.title = "UK Rainfalls in OCT-SEPT(mm)"
	hist.x_labels = dates
	hist.x_title = 'Years'
	hist.y_title = 'Rainfalls'
	hist.add('Rainfall(mm)',rainfalls)
	hist.render_to_file('Rainfall.svg')



