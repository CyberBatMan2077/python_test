#homework  8-1
def display_message() :
	"""我在学函数定义"""
	print("I'm learning how to define a function")

display_message()

#homework  8-2
def favorite_book(name):
	"""显示最喜欢的书本"""
	print("One of my favorite books is " + name.title())

favorite_book('priencess snow white')

#practice for myself
def describe_pet(pet_name,animal_type = 'dog'):
	"""显示宠物信息，默认值形参于后"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('Willie')
describe_pet('Jerry','Cat')
describe_pet('Duby',animal_type='Bird')

#homework  8-3
def make_shirt(size,slogan):
	"""定制T恤"""
	print("The shirt you want to make is " + size + " Size ")
	print("\nThe slogan on it: " + slogan)

make_shirt('XL','Just do it')
make_shirt(size = 'XL',slogan = 'Just do it')

#homework  8-4
def make_shirt(size,slogan = 'I Love Python'):
	"""定制T恤"""
	print("The shirt you want to make is " + size + " Size ")
	print("\nThe slogan on it: " + slogan)

make_shirt('L')
make_shirt('M')
make_shirt('M','Whatever')

#homework  8-5
def describe_city(name,country = 'China'):
	"""OMIT"""
	print(name + ' is in ' + country)

describe_city('Guangzhou')
describe_city('Shanghai')
describe_city('NewYork','USA')

#homework  8-6
def city_country(name,country):
	message = name + ' , ' + country
	return message

print('"' + city_country('GZ','China') + '"')
print('"' + city_country('SH','China') + '"')
print('"' + city_country('BJ','China') + '"')

#homework  8-7
def make_album(singer,album_name,song_num = ''):
	album = {'singer' : singer,
			 'albunm_name' : album_name,
			 }
	if song_num:
		album['song_num'] = song_num
	return album

print(make_album('Adam','AA'))
print(make_album('TS','23','7'))
print(make_album('Eason','DUO'))

#homework  8-8

singer = ''
album = ''
active = 1
while active:
	singer = input('input the name of singer')
	if singer != 'q':
		album = input('input the name of album')
		if album != 'q':
			print(make_album(singer, album))
		else:
			active = 0
	else:
		active = 0

print('Finishing input')

#homework  8-9
def show_magicians(names):
	print(names)
great_names = []
magicians = ['Jack','Rose','Ben','John']
show_magicians(magicians)

#homework  8-10
def make_great(original_name,great_names):
	while original_name:
		current_name = 'The Great ' + original_name.pop()
		great_names.append(current_name)
	return	great_names

#Two ways for function calls
#show_magicians(make_great(magicians))
make_great(magicians,great_names)
show_magicians(great_names)
show_magicians(magicians)

#homework  8-11
print("/////////////////////////HOMEWORK 8-11/////////////////////")
magicians = ['Jack','Rose','Ben','John']
make_great(magicians[:],great_names)
show_magicians(great_names)
show_magicians(magicians)

#homework  8-12
def make_sanwich(*toppings):
	print(toppings)

make_sanwich('Banana','Chicken','Beef')
make_sanwich('Banana','Chicken')
make_sanwich('Banana')

#homework  8-13
def build_profile(first,last,**user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('Zhou','Jielun',age='50',name_of_wife='Kunling',Music='Shuangjiegun')
print(user_profile)

#homework  8-14
def car_info(company,size,**other_info):
	car ={'company':company,
		  'size':size,
		  }
	for keys,values in other_info.items():
		car[keys] = values

	return car

car = car_info('subaru','outback',color = 'blue',tow_package = True)
print(car)

#homework  8-15
import printing_functions
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs,completed_models)
printing_functions.show_completed_models(completed_models)

#homework  8-16

#import disp_message
#disp_message.display_message()

#from disp_message import display_message
#display_message()

#from disp_message import display_message as dm
#dm()

#import disp_message as dm
#dm.display_message()

from disp_message import *
display_message()

#homework  8-17
#OMIT