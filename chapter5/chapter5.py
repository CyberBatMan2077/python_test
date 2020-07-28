#homework  5-1
pizza = 'hot'
print("Is this pizza == 'hot'? I say yes")
print(pizza == 'hot')
print("Is this pizza == 'Hot? I say no")
print(pizza == 'Hot')
print("Is this pizza == 'HOT? I say yes")
print(pizza.upper() == 'HOT')
print(5>4)
print(5>=4)
print(5<4)
print(5<=4)
print('Hello' == 'HELLO')
print('HALO'== 'Halo')
print('Halo '== 'Halo')
print('Halo'== 'Halo')

#homework  5-2
print('homework  5-2')
names = ['jack','Rose','Ben']
print('Ben' in names)
print('ben' in names)
print('ben' not in names)
print('jack' in names and 'Ben' in names)
print('jack' in names or 'Ben' in names)

#homework  5-3
alien_colors = ['green','yellow','red']
alien_color = 'green'
if alien_color == 'green':
	print('5 ps')
alien_color = 'red'
if alien_color == 'green':
	print('5 ps')

#homework  5-4
if alien_color == 'green':
	print('5 ps')
if alien_color != 'green':
	print('10 ps')

if alien_color == 'green':
	print('5 ps')
else:
	print('10ps')

#homework  5-5
for alien_color in alien_colors:
	if alien_color == 'green':
		print('5 ps')
	elif alien_color == 'yellow':
		print('10 ps')
	elif alien_color == 'red':
		print('15 ps')

#homework  5-6
age = 12
if age < 2:
	print('He is a baby')
elif age >= 2 and age < 4:
	print('He is learning how to walk')
elif age >= 4 and age < 13:
	print("He is a child")
elif age >= 13 and age < 20:
	print("He is a teen")
elif age >= 20 and age < 65:
	print("He is a adult")
elif age >= 65:
	print("He is a old man")

#homework  5-7
fruits = ['banana','apple','peach','orange']
if 'banana' in fruits:
	print('you really love banana! ')
if 'apple' in fruits:
	print('you really love apple! ')
if 'peach' in fruits:
	print('you really love peach! ')
if 'orange' in fruits:
	print('you really love orange! ')

#homework  5-8
names =['admin','Jack','Rose','Ben','Ken']
for name in names:
	if name == 'admin':
		print("Hello " + name + " , would you like to see a status report?")
	else:
		print("Hello " + name + ", thank you for logging in again")

#homework  5-9
names = []
if names:
	print(names)
else:
	print("We need to find some users!")

#homework  5-10
current_users = ['hacker','Captain','batman','WW','spider']
current_users_lower = []
#create a lower spell version of current users list
for current_user in current_users:
	current_users_lower.append(current_user.lower())
print(current_users_lower)
new_users = ['Bat','GunMan','Ironman','WW','Batman']
for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(new_user + " Not available name, please find another name")
	else:
		print("You can use this name " + new_user)

#homework  5-11
nums = list(range(1,10))
for num in nums:
	if num == 1:
		print(str(num) + 'st' + '\n')
	elif num == 2:
		print(str(num) + 'nd' + '\n')
	elif num == 3:
		print(str(num) + 'rd' + '\n')
	else:
		print(str(num) + 'th' + '\n')

#homework  5-12
#OMIT
#homework  5-13
#OMIT

