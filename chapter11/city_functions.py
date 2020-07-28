def country_city(city_name,country_name,population=''):
	"""城市和国家"""
	if population == '':
		full_name = city_name + ', ' + country_name
	else:
		full_name = city_name + ', ' + country_name + ' - ' + population
	return full_name.title()