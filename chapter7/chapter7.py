message = input('Tell me something, and I will repeat it back to you:')
print(message)

#homework  7-1
car = input("What kind of cars do you want to rent?")
print('Let me see if I can find you ' + car)

#homework  7-2
book = input('How many people?')
if int(book) > 8:
	print("No suitable table now.")
else:
	print('Please take a seat')

#homework  7-3
num = input('A number you want to try')
if int(num) % 10 == 0 :
	print('True')
else:
	print('False')

#homework  7-4
pizza = ''
while pizza != 'quit':
	pizza = input('pizza toppings you want to add')
	if pizza != 'quit':
		print('We will add ' + pizza + ' for you ')

#homework  7-5
age = input('input your age please')
if int(age) < 3:
	price = 0

elif int(age) >= 3 and int(age) <= 12:
	price = 10

elif int(age) > 12:
	price = 15

print('You should pay ' + str(price) )

#homework  7-6
active = True
while active:
	pizza = input('pizza toppings you want to add')
	if pizza != 'quit':
		print('We will add ' + pizza + ' for you ')
	else:
		break

#homework  7-7
#while 1:
#	print("I'm a fool and i dont know how to stop it !")

#homework  7-8
sandwich_order = ['Banana_sandwich','apple_sandwich','watermelon_sandwich']
finished_sandwich = []
while sandwich_order:
	current = sandwich_order.pop()
	print('I made you ' + current)
	finished_sandwich.append(current)
print('All finished')
print(finished_sandwich)

#homework  7-9
sandwich_order = ['Banana_sandwich',
				  'pastrami',
				  'apple_sandwich',
				  'watermelon_sandwich',
				  'pastrami',
				  'pastrami',
				  ]
print('pastrami is out of sale')
while 'pastrami' in sandwich_order:
	sandwich_order.remove('pastrami')
while sandwich_order:
	current = sandwich_order.pop()
	print('I made you ' + current)
	finished_sandwich.append(current)
print('All finished')
print(finished_sandwich)

#homework  7-10
place = 1
places = []
while place != 'quit':
	place = input('A place you want to go most')
	if place != 'quit':
		places.append(place)

print(places)
