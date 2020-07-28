#homework  6-1
info = {'first_name':'LEE',
		'last_name':'galon',
		'age':'28',
		'living_city':'Guangzhou',
		}
print(info['first_name'])
print(info['last_name'])
print(info['age'])
print(info['living_city'])

#homework  6-2
fav_num = {'Jack':'12',
		   'rose':'13',
		   'Ben':'15',
		   'Sam':'1223',
			}
print("Jack's fav number is " + fav_num['Jack'])
print("rose's fav number is " + fav_num['rose'])
print("Ben's fav number is " + fav_num['Ben'])
print("Sam's fav number is " + fav_num['Sam'])

#homework  6-3
code ={'for':'loop using word',
	   'print':'print something on the monitor',
	   'list':'change something into list',
	   'AAA':'just for completing the task',
	   'BBB':'just for finishing the task',
	   }
print("the word for means:" + '\n'+ code['for'])
print("the word print means:" + code['print'])
print("the word list means:" + code['list'])
print("the word AAA means:" + code['AAA'])
print("the word BBB means:" + code['BBB'])

#homework  6-4
for i,j in code.items():
	print('the word ' + i + ' means: ' + j)
code['CCC'] = 'CCC'
code['DDD'] = 'DDD'
code['EEE'] = 'EEE'
code['FFF'] = 'FFF'
code['GGG'] = 'GGG'
for i,j in code.items():
	print('the word ' + i + ' means: ' + j)

#homework  6-5
rivers = {'nile':'egypt',
		  'river_1':'country_1',
		  'huanghe':'china',
		  'changjiang':'china',
		  'river_2':'Country_2',
		  }
for i,j in rivers.items():
	print('The ' + i.title() + ' runs through' + j.title())
for i in rivers.keys():
	print(i.title())
for i in rivers.values():
	print(i.title())

#homework  6-6
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
peoples = ['jen','sarah','Liao','Jack']
for i in peoples:
	if i in favorite_languages.keys():
		print(i.title() + ', thanks for your participating!')
	else:
		print(i.title() + ', would you like to take a roll?')

#homework  6-7
info_1 = {'first_name':'JJ',
		  'last_name':'GG',
		  'age':'21',
		  'living_city':'JP',
		  }

info_2 = {'first_name':'MM',
		  'last_name':'YY',
		  'age':'20',
		  'living_city':'HK',
		  }

infos = [info, info_1 , info_2]

for i in infos:
	print(i)

#homework  6-8
cat = {'type':'small',
	   'host_name':'Jack',
	   }

dog = {'type':'big',
	   'host_name':'Rose',
	   }

bird = {'type':'tiny',
		'host_name':'bird_man',
		}

pets = [cat,dog,bird]
for i in pets:
	print(i)

#homework  6-9
favorite_places = {'Jack':['WC','Hotel','Bathroom'],
				   'Rose':['Sofa','Bed'],
				   'Me':['home','bed','cyberspace'],
				   }
for i,j in favorite_places.items():
	print(i + 's' + ' favorite place is')
	for z in j:
		print(z)

#homework  6-10
#OMIT refer to homework 6-9

#homework  6-11
cities = {'Guangzhou':
			  {'country':'china',
			   'population':'30000000',
		  		'facts':'many delicious food'
				},
		  'Xian':
			  {'country':'China',
			   'population':'unknown',
			   'facts':'many places of interest',
			   },
		  'Chongqing':
			  {'country':'China',
			   'population':'unknown',
			   'facts':'stranger buildings everywhere',
			   }
		  }
for i,j in cities.items():
	print('things about ' + i)
	for q,w in j.items():
		print(q + ' : ' + w)

#homework  6-12
#OMIT
