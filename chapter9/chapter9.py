#homework  9-1
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type

	def describe_restaurant(self):
		print("The name of restaurant is " + self.name.title())
		print("The type of cuisine is " + self.type.title())


	def open_restaurant(self):
		print("We are now opening,Welcome")

restaurant = Restaurant('KFC','fastfood')
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#homework  9-2
restaurant_1 = Restaurant('McDonald','fastfood')
restaurant_2 = Restaurant('Zen','Janpanese')
restaurant_3 = Restaurant('Beef_steakhouse','American')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

#homework  9-3
class User():
	def __init__(self,first_name,last_name,age,region):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.region = region

	def describe_user(self):
		print("User's name is " + self.first_name.title() + ' ' +
			  self.last_name.title() + ' ,age is ' + self.age +
			  ' user is from ' + self.region)

	def greet_user(self):
		print("Welcome, " + self.first_name.title() + ' ' +
			  self.last_name.title())

user_1 = User('LEE','GALON','23','China')
user_1.describe_user()
user_1.greet_user()
user_2 = User('Michael','Jackson','50','USA')
user_2.describe_user()
user_2.greet_user()

#homework  9-4
class Restaurant_new():
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The name of restaurant is " + self.name.title())
		print("The type of cuisine is " + self.type.title())


	def open_restaurant(self):
		print("We are now opening,Welcome")

	def number_change(self,served_number):
		self.number_served = served_number

	def increment_number_served(self,increment):
		self.number_served += increment




restaurant = Restaurant_new('KFC','fastfood')
print(restaurant.number_served)
restaurant.number_served = 1
print(restaurant.number_served)
restaurant.number_change(100)
print(restaurant.number_served)
restaurant.increment_number_served(50)
print(restaurant.number_served)

#homework  9-5
class User_new():
	def __init__(self,first_name,last_name,age,region):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.region = region
		self.login_attempts = 0

	def describe_user(self):
		print("User's name is " + self.first_name.title() + ' ' +
			  self.last_name.title() + ' ,age is ' + self.age +
			  ' user is from ' + self.region)

	def greet_user(self):
		print("Welcome, " + self.first_name.title() + ' ' +
			  self.last_name.title())

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user_3 = User_new('Lei','Hana',35,'USA')
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.increment_login_attempts()
print(user_3.login_attempts)
user_3.reset_login_attempts()
print(user_3.login_attempts)

#homework  9-6
class IceCreamStand(Restaurant_new):
	def __init__(self,restaurant_name,cuisine_type,*flavours):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavours

	def show_flavors(self):
		print(self.flavors)

ic = IceCreamStand('DQ','dessert','Juice','Apple')
ic.open_restaurant()
ic.show_flavors()

#homework  9-7
class Admin(User):
	def __init__(self,first_name,last_name,age,region,privileges):
		super().__init__(first_name,last_name,age,region)
		self.privileges = privileges

	def show_privileges(self):
		print(self.privileges)

admin_0 = Admin('Jay','Chow',50,'Taiwan','can add post')
admin_0.show_privileges()

#homewrok  9-8
class Privileges():
	def __init__(self,privileges = 'can add post'):
		self.privileges	= privileges

	def show_privileges(self):
		print(self.privileges)

class Admin_new(User):
	def __init__(self,first_name,last_name,age,region):
		super().__init__(first_name,last_name,age,region)
		self.privileges = Privileges()

admin_1 = Admin_new('Joy','Chaw',50,'Taiwan')
admin_1.privileges.show_privileges()

#Self_practice:improve homework 9-9,privileges can be genernated if a value
#is given when creating this object.Otherwiset the default value is 'can add'
class Privileges_new():
	def __init__(self,privileges):
		if privileges == '':
			self.privileges = 'can add post'
		else:
			self.privileges	= privileges

	def show_privileges(self):
		print(self.privileges)

class Admin_new_new(User):
	def __init__(self,first_name,last_name,age,region,privileges=''):
		super().__init__(first_name,last_name,age,region)
		self.privileges = Privileges_new(privileges)

admin_4 = Admin_new_new('Joy','Chaw',50,'Taiwan')
admin_4.privileges.show_privileges()
admin_5 = Admin_new_new('Joy','Chaw',50,'Taiwan','can delete post')
admin_5.privileges.show_privileges()

#homework  9-9
#OMIT

#homework  9-10
from restaurant import Restaurant_new_new
r = Restaurant_new_new('PandaFood','Chinese')
r.open_restaurant()

#homework  9-11
import user
a1 = user.Admin_new('Chen','Zhiling','50','Taiwan')
a1.privileges.show_privileges()

#homework  9-12
import admin
a2 = admin.Admin_new('Fenghuang','Chuanqi','40','China')
a2.privileges.show_privileges()

#homework  9-13
from collections import OrderedDict
code = OrderedDict()
for i,j in code.items():
	print('the word ' + i + ' means: ' + j)

code['CCC'] = 'CCC'
code['DDD'] = 'DDD'
code['EEE'] = 'EEE'
code['FFF'] = 'FFF'
code['GGG'] = 'GGG'
for i,j in code.items():
	print('the word ' + i + ' means: ' + j)

#homework  9-14
from random import randint
class Die():
	def __init__(self,sides=6):
		self.sides = sides

	def roll_die(self,number):
		i = 1
		while i <= number:
			print(randint(1,self.sides))
			i += 1
d1 = Die(6)
d1.roll_die(10)
print("///////////////////////////////////////////////")
d2 = Die(10)
d2.roll_die(10)
print("///////////////////////////////////////////////")
d3 = Die(20)
d3.roll_die(10)

#homework  9-15
#OMIT