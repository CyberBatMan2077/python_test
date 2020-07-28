#self-practice
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

a = ['helloworld']

i = 'hello'

if i in a:
	print('YES!')
else:
	print("NO!")

filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.strip()

print(pi_string)

if '1415' in pi_string:
	print("YES!")

#homework  10-1
with open('learning_python.txt') as lp:
	text = lp.read()
	print(text)

with open('learning_python.txt') as lp:
	for line in lp:
		print(line)
with open('learning_python.txt') as lp:
	text_1 = lp.readlines()

for i in text_1:
	print(i.strip())

#homework  10-2
print('/////////////////Homework 10-2//////////////////')
with open('learning_python.txt') as lp:
	text_1 = lp.readlines()

for i in text_1:
	print(i.replace('Python','C language'))

#homework  10-3
user_name = input("Input a user name :")
with open('guest.txt','w') as file_object:
	file_object.write(user_name)

#homework  10-4
guest_name = input("Input a guset name: ")
while guest_name != 'q':
	print('Hello ' + guest_name + ' !')
	with open('guest_book.txt','a') as file_object:
		file_object.write(guest_name + "\n")
		guest_name = input("Input a guset name: ")

#homework  10-5
#OMIT refer to homework 10-4

#homework  10-6
while True:
	a = input('input a number')
	if a == 'q':
		break
	b = input('input another number')
	if b == 'q':
		break
	try:

		c = int(a) + int(b)
		print(c)
	except ValueError:
		print("Not suitable input")

#homework  10-7
#OMIT:finished in 10-6

#homework  10-8
try:
	with open('dogs.txt') as file_object:
		dog_txt = file_object.read()
		print(dog_txt)
except FileNotFoundError:
	print("The file is not found")

#homework  10-9
try:
	with open('dogs_not_exist.txt') as file_object:
		dog_txt = file_object.read()
		print(dog_txt)
except FileNotFoundError:
	pass

#homework  10-10

#WARNING:This code can not calculate the number of words correctly
#because the function 'count' can not count precisely,for example,
#if you want to count 'the', the word 'there' counts,too

with open('Walden.txt') as file_object:
	text_walden = file_object.readlines()
	count = 0
	for line in text_walden:
		count += line.lower().count('the')
	print(count)

a="today to to To tomorrow"
print(a.lower().count('to'))


#homework  10-11
import json
fav_number = input('Input your favorite number and we will save it')
with open('number.json','w') as json_object:
	json.dump(fav_number,json_object)

with open('number.json') as json_object:
	fav_number_saved = json.load(json_object)
	print('I know your favorite number is ' + fav_number_saved)

#homework  10-12
print('/////////////////////////////HOMEWORK  10-12///////////////')
try:
	with open('number_new.json') as json_object:
		fav_number_saved = json.load(json_object)
		print('I know your favorite number is ' + fav_number_saved)
except FileNotFoundError:
	with open('number_new.json','w') as json_object:
		fav_number = input('Input your favorite number and we will save it')
		json.dump(fav_number, json_object)

#homework  10-13
def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input("What is your name?")
	filename = 'username.json'
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username

def greet_user():
	username = get_stored_username()
	if username:
		print('Your username is ' + username + '!' + 'It is you? <y/n>')
		user_name_input = input()
		if(user_name_input == 'y'):
			print("Welcome back " + username + "!")
		elif(user_name_input == 'n'):
			get_new_username()
	else:
		username = get_new_username()
		print("We'll remember you when you come back," + username + "!")

greet_user()
